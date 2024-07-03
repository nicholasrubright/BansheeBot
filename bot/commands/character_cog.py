from typing import Optional

import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

import bot.raiderIO as raiderIO


class Character(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Character cog is initializing...")

    character = SlashCommandGroup(
        name="character", description="All commands related to characters"
    )

    @character.command(name="get_char")
    async def get_char(self, ctx, name: str, realm: str = "Dalaran"):
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
