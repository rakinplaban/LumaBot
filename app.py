import os
import hmac
import hashlib
import aiohttp
import uvicorn
from fastapi import FastAPI, Request, Header, HTTPException
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import sansio
from dotenv import load_dotenv


load_dotenv(verbose=True)

# GitHub App Credentials
APP_ID = os.getenv("APP_ID")  # Set in environment variables
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")  # Set in environment variables
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH")  # Path to your .pem file


# print(f"APP_ID: {APP_ID}")
# print(f"WEBHOOK_SECRET: {WEBHOOK_SECRET}")
# print(f"PRIVATE_KEY_PATH: {PRIVATE_KEY_PATH}")

app = FastAPI()


# Verify the webhook signature
def verify_signature(payload, signature):
    mac = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={mac}", signature)

@app.post("/")
async def webhook_handler(
    request: Request, x_hub_signature_256: str = Header(None)
):
    print(f"Received Webhook Secret: {WEBHOOK_SECRET}")
    body = await request.body()

    # Verify the webhook secret
    if not verify_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Invalid signature")

    # Parse GitHub event
    event = sansio.Event.from_http(request.headers, body)

    async with aiohttp.ClientSession() as session:
        gh = gh_aiohttp.GitHubAPI(session, "LumaBot")

        if event.event == "issues" and event.data["action"] == "opened":
            issue = event.data["issue"]
            repo = event.data["repository"]

            # Comment on the issue
            comment_url = f"/repos/{repo['owner']['login']}/{repo['name']}/issues/{issue['number']}/comments"
            await gh.post(comment_url, data={"body": f"Thank you @{issue['user']['login']} for opening this issue! ❤️"})

            # React with ❤️ emoji
            reaction_url = f"/repos/{repo['owner']['login']}/{repo['name']}/issues/{issue['number']}/reactions"
            await gh.post(
                reaction_url,
                data={"content": "heart"},
                accept="application/vnd.github.squirrel-girl-preview+json",
            )

            


    return {"message": "Webhook received"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    


