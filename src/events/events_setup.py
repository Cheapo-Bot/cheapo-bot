import discord
from discord.ext import commands

from src.events.on_message import reward_every_ten_message


def event_setup(bot: commands.Bot):
    @bot.event
    async def on_message(message: discord.Message):
        await reward_every_ten_message(message, bot)
