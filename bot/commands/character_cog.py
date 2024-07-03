from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

from bot.raiderIO import raiderIO

# import bot.raiderIO as raiderIO


class Character(commands.Cog, app_commands.GroupCog):

    character_group = app_commands.Group(name="character_group")

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

        print("Character cog is initializing...")

    @character_group.command(name="get_char")
    async def get_char(self, ctx, name: str, realm: Optional[str] = "Dalaran"):
        try:
            discord_user_id = ctx.author.id
            character_io = await raiderIO.get_character(name, realm)

            if character_io is None:
                await ctx.respond(f"Character {name}-{realm} does not exist")
                return

            else:
                await ctx.respond(f"Item level: {character_io.item_level}")

        except Exception as exception:
            print(exception)
            await ctx.respond("Something went wrong")


def setup(bot):
    bot.add_cog(Character(bot))
    print("Character cog has loaded successfully")
