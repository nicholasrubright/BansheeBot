import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from importlib.util import resolve_name

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents(guilds=True)
intents.guilds = True

bot = commands.Bot(command_prefix=">", intents=intents)

cogs_list = [
    "bot.commands.character_cog",
]


async def load_extensions():
    """Load the cogs from the cogs_list"""
    for cog in cogs_list:
        await bot.load_extension(resolve_name(cog, __package__))


async def main():
    await load_extensions()
    bot.run(TOKEN)


asyncio.run(main())
