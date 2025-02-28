**Story: Resolving the JWT Issue with GitHub App Authentication**  

I encountered an issue while retrieving the JWT token from GitHub. Despite having a valid private key and the correct app ID, my authentication attempts kept failing. The root cause was that I was passing the **app ID** instead of the **installation ID** when making API requests.  

To resolve this, I followed these steps:  

1️⃣ **Verify the JWT Token**  
   - I first checked if my JWT was valid by running:  
   ```bash
   curl -H "Authorization: Bearer jwt_token" \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/app
   ```
   - If this returned **401 Unauthorized**, it meant my JWT was invalid.  

2️⃣ **Retrieve the Installation ID**  
   - Since the issue was likely related to the installation ID, I fetched it using:  
   ```bash
   curl -H "Authorization: Bearer jwt_token" \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/app/installations
   ```
   - If the response contained `[]`, it meant the app wasn't installed anywhere. However, since my app was installed, I successfully retrieved the installation ID.  

3️⃣ **Obtain the Correct API Endpoint**  
   - With the correct installation ID, I generated an access token using:  
   ```bash
   curl -H "Authorization: Bearer jwt_token" \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/app/installations/INSTALLATION_ID/access_tokens
   ```
   - This gave me a valid access token, allowing my bot to authenticate properly.  

Thanks to this approach, I was able to overcome the **invalid/expired JWT issue** and run my bot locally without issues. 🚀  

