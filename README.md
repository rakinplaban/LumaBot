# LumaBot

LumaBot is a GitHub bot built with FastAPI and gidgethub that interacts with issue creators by thanking them and reacting with a love emoji. It is designed to enhance community engagement while maintaining a simple and efficient workflow.

## Meet Luma (ルマ)! 🌸
Konnichiwa!~ 💕 I'm Luma (ルマ), your friendly GitHub assistant! I'm here to make sure every issue creator feels appreciated. I'll drop by with a sweet "Thank you!" and a little love. Let's make GitHub a warm and happy place together! (≧◡≦) 💖

<!-- ![Luma-chan]() -->
<img src="destination/luma.png" alt="Luma-chan" height="400" width="400">

## Features
- Automatically comments "Thank you @user" on new issues.
- Reacts to issues with a ❤️ emoji.
- Built using Python with FastAPI and gidgethub.
- Lightweight and efficient for GitHub repositories.

## How It Works
1. LumaBot listens for new issue events on a GitHub repository.
2. When a new issue is created, it comments with a thank-you message.
3. It also adds a ❤️ reaction to the issue.

## How to configure
Follow this link 👉🏼 https://github.com/apps/luma-bot-1 and click install.

## Installation
### Prerequisites
- Python 3.8+
- GitHub App credentials (Client ID, Client Secret, Webhook Secret, Private Key)

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/rakinplaban/LumaBot.git
   cd LumaBot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```sh
   export GITHUB_APP_ID=your_app_id
   export GITHUB_WEBHOOK_SECRET=your_webhook_secret
   export GITHUB_PRIVATE_KEY="your_private_key"
   ```
4. Run the bot:
   ```sh
   uvicorn app:app --host 0.0.0.0 --port 3000 --reload
   ```

## Deployment
LumaBot can be deployed on platforms like Vercel, Railway, or a personal server using Docker.

### Deploy with Docker
1. Build the Docker image:
   ```sh
   docker build -t lumabot .
   ```
2. Run the container:
   ```sh
   docker run -d -p 8000:8000 --env-file .env lumabot
   ```

## Configuration
LumaBot's behavior can be customized by modifying its response messages or extending its features to support additional GitHub events.

## Roadmap
- [ ] Support for PR events.
- [ ] Customizable responses.
- [ ] More reaction options.

## License
This project is licensed under the MIT License.

---

✨ **LumaBot is part of the 'Star 🌟 This Repo' anime magic!** ✨

![Anime](https://animemagic.vercel.app/anime-image?t=123456)



<!-- # LumaBot

LumaBot is a GitHub bot built with FastAPI and gidgethub that interacts with issue creators by thanking them and reacting with a love emoji. It is designed to enhance community engagement while maintaining a simple and efficient workflow.

## Features
- Automatically comments "Thank you @user" on new issues.
- Reacts to issues with a ❤️ emoji.
- Built using Python with FastAPI and gidgethub.
- Lightweight and efficient for GitHub repositories.

## How It Works
1. LumaBot listens for new issue events on a GitHub repository.
2. When a new issue is created, it comments with a thank-you message.
3. It also adds a ❤️ reaction to the issue.

## Installation
### Prerequisites
- Python 3.8+
- GitHub App credentials (Client ID, Client Secret, Webhook Secret, Private Key)

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/lumabot.git
   cd lumabot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```sh
   export GITHUB_APP_ID=your_app_id
   export GITHUB_WEBHOOK_SECRET=your_webhook_secret
   export GITHUB_PRIVATE_KEY="your_private_key"
   ```
4. Run the bot:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Deployment
LumaBot can be deployed on platforms like Vercel, Railway, or a personal server using Docker.

### Deploy with Docker
1. Build the Docker image:
   ```sh
   docker build -t lumabot .
   ```
2. Run the container:
   ```sh
   docker run -d -p 8000:8000 --env-file .env lumabot
   ```

## Configuration
LumaBot's behavior can be customized by modifying its response messages or extending its features to support additional GitHub events.

## Roadmap
- [ ] Support for PR events.
- [ ] Customizable responses.
- [ ] More reaction options.

## License
This project is licensed under the MIT License.

---

✨ **LumaBot is part of the 'Star 🌟 This Repo' anime magic!** ✨ -->
