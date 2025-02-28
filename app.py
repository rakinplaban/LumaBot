import os
import hmac
import hashlib
import aiohttp
import uvicorn
import jwt
import requests
import time
from fastapi import FastAPI, Request, Header, HTTPException
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import sansio
from dotenv import load_dotenv


load_dotenv(verbose=True)

# GitHub App Credentials
APP_ID = os.getenv("APP_ID")  # Set in environment variables
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")  # Set in environment variables
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH")  # Path to your .pem file
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 

# print(f"APP_ID: {APP_ID}")
# print(f"WEBHOOK_SECRET: {WEBHOOK_SECRET}")
# print(f"PRIVATE_KEY_PATH: {PRIVATE_KEY_PATH}")

app = FastAPI()


# Verify the webhook signature
def verify_signature(payload, signature):
    mac = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={mac}", signature)


with open(PRIVATE_KEY_PATH, "rb") as key_file:
    private_key = key_file.read()



def installation_id_retriever(headers):
    url = "https://api.github.com/app/installations"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        installations = response.json()
        if installations:
            installation_id = installations[0]["id"]  # Extract the first installation ID
            print(f"Installation ID: {installation_id}")
            return installation_id
        else:
            print("No installations found.")
    else:
        print(f"Error: {response.status_code} - {response.json()}")


async def get_installation_token():
    """Generates a JWT and fetches an installation token for LumaBot"""
    payload = {
        "iat": int(time.time()),  # Issued at time
        "exp": int(time.time()) + 600,  # Expiration time (max 10 minutes)
        "iss": APP_ID,  # GitHub App ID
    }

    # Load private key from file
    # private_key = load_private_key()

    # Create JWT
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256")
    print("Generated JWT:", jwt_token)

    # url = f"https://api.github.com/app/installations/60287794/access_tokens"
    headers = {"Authorization": f"Bearer {jwt_token}", "Accept": "application/vnd.github+json"}
    installation_id = installation_id_retriever(headers)
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"

    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()["token"]



@app.post("/")
async def webhook_handler(request: Request, x_hub_signature_256: str = Header(None)):
    body = await request.body()
    secret = WEBHOOK_SECRET.encode()  # Convert to bytes
    if not verify_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Invalid signature")

    event = sansio.Event.from_http(request.headers, body, secret=secret.decode() if isinstance(secret, bytes) else secret)

    async with aiohttp.ClientSession() as session:
        # 🔥 Fetch LumaBot's token dynamically
        GITHUB_TOKEN = await get_installation_token()
        # private_key = load_private_key()
        # decoded = jwt.decode(GITHUB_TOKEN, private_key, algorithms=["RS256"], options={"verify_signature": False})
        # print("Decoded JWT:", decoded)

        gh = gh_aiohttp.GitHubAPI(session, "LumaBot", oauth_token=GITHUB_TOKEN)

        if event.event == "issues" and event.data["action"] == "opened":
            issue = event.data["issue"]
            repo = event.data["repository"]
            comment_url = f"/repos/{repo['owner']['login']}/{repo['name']}/issues/{issue['number']}/comments"

            # ✅ LumaBot now posts comments (not your account)
            await gh.post(
                comment_url,
                data={"body": f"Hey @{issue['user']['login']}! Thank you for opening this issue! 💖 I'll make sure it's seen!"},
                accept="application/vnd.github+json",
            )

            # ✅ LumaBot reacts with ❤️
            reaction_url = f"/repos/{repo['owner']['login']}/{repo['name']}/issues/{issue['number']}/reactions"
            await gh.post(
                reaction_url,
                data={"content": "heart"},
                accept="application/vnd.github.squirrel-girl-preview+json",
            )

    return {"message": "Webhook received"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
    


