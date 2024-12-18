import discord
from discord import app_commands
from discord.ext import commands
from OpenAI import generate_response


# Accept discord token via environment variable
discord_token = ''

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='/',  # Prefix is still required but won't be used for slash commands
            intents=discord.Intents.default()
        )

    async def setup_hook(self):
        # Sync commands with Discord
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name='chat')
@app_commands.describe(prompt='Your message to the bot')
async def chat(interaction: discord.Interaction, prompt: str):
    # Defer the response if processing might take longer than 3 seconds
    await interaction.response.defer()

    response = generate_response(prompt)

    # Create an embed for a richer presentation
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(name="You said:", value=prompt, inline=False)
    embed.add_field(name="Assistant:", value=response, inline=False)

    user_mention = interaction.user.mention
    # Send the follow-up message
    await interaction.followup.send(f'{user_mention}, {response}')


bot.run(discord_token)
