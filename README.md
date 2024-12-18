# Discord Chat Bot

This repository contains a simple Discord bot that leverages OpenAI's API to provide intelligent responses to user queries via slash commands. The bot uses `discord.py` for interacting with Discord and supports dynamic message responses.

## Features
- Slash command `/chat` to interact with the bot.
- Responses are generated using OpenAI's API.
- Clean and dynamic message formatting using Discord embeds.

## Requirements

- Python 3.8 or higher
- Dependencies:
  - Discord.py
  - OpenAI
- A Discord Bot Token
- An OpenAI API Key

## Setup

### Prerequisites
1. **Create a Discord Bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application.
   - Navigate to the "Bot" tab and click "Add Bot."
   - Copy the bot token from the "Token" section.

2. **OpenAI API Key**:
   - Obtain an API key from [OpenAI](https://platform.openai.com/signup/).

3. **Install Python and Dependencies**:
   Ensure you have Python 3.8 or higher installed on your system.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/1337haxx0r/DiscordGPT.git
   cd DiscordGPT
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install openai
   pip install discord
   pip install discord.py
   ```

4. Set up environment variables:
   ```bash
   main.py: discord_token = ''
   OpenAI.py: openai_api_key = ("")
   ```

### Running the Bot
1. Start the bot:
   ```bash
   python main.py
   ```

2. The bot should now be online and ready to accept commands in your Discord server.

## Adding the Bot to a Discord Server
1. Go to the [OAuth2 URL Generator](https://discord.com/developers/applications) for your application.
2. Under the "OAuth2" tab, navigate to "URL Generator."
3. Select the following scopes:
   - `bot`
   - `applications.commands`
4. Under "Bot Permissions," select the permissions your bot needs (e.g., `Send Messages`, `Embed Links`, etc.).
5. Copy the generated URL and open it in your browser.
6. Select a server to add the bot to and click "Authorize."

## Usage

1. Invite the bot to a server as described above.
2. Use the `/chat` slash command to interact with the bot:
   ```
   /chat prompt: What is the capital of France?
   ```
3. The bot will respond with a helpful answer, using the OpenAI API to generate its response.

## Code Structure

### `main.py`
The main bot logic:
- Initializes the Discord bot.
- Formats responses using Discord embeds.

### OpenAI Integration
The `generate_response` function in `bot.py` interacts with OpenAI's API to generate a response to user input. Be sure to set your OpenAI API key in the `.env` file.

## Example Output
- **User Input**:
  `/chat prompt: Tell me a joke.`
- **Bot Response**:
  "You said: Tell me a joke."
  "Assistant: Why did the scarecrow win an award? Because he was outstanding in his field!"
