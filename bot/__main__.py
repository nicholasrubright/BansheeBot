import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents(guilds=True)
intents.guilds = True

bot = discord.Bot(
    intents=intents,
    activity=discord.Activity(
        type=discord.ActivityType.watching, name="for slash commands!"
    ),
)

cogs_list = [
    "bot.commands.general_cog",
    "bot.commands.admin_cog",
    "bot.commands.guild_cog",
    "bot.commands.character_cog",
    "bot.commands.announcement_cog",
]


def load_extensions():
    """Load the cogs from the cogs_list"""
    for cog in cogs_list:
        bot.load_extension(cog)


def main():
    load_extensions()
    bot.run(TOKEN)


main()
