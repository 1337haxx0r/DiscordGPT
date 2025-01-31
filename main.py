import os
import discord
from discord import app_commands
from discord.ext import commands
from OpenAI import generate_response  # Ensure this is the updated generator
from dotenv import load_dotenv
load_dotenv()

# Set your Discord bot token
token = os.getenv('DISCORD_TOKEN')


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='/',
            intents=discord.Intents.default()
        )

    async def setup_hook(self):
        await self.tree.sync()


bot = MyBot()


@bot.tree.command(name='chat')
@app_commands.describe(prompt='Your message to the bot')
async def chat(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    user_mention = interaction.user.mention

    try:
        # Send initial message
        message = await interaction.followup.send(f"{user_mention}, Generating response...")

        buffer = ""
        for chunk in generate_response(prompt):
            buffer += chunk

            # Edit message every 3 characters to avoid rate limits
            if len(buffer) % 3 == 0:
                await message.edit(content=f"{user_mention}, {buffer}")

        # Final update to show complete message
        await message.edit(content=f"{user_mention}, {buffer}")

    except Exception as e:
        await interaction.followup.send(f"Error: {str(e)}")


bot.run(token)