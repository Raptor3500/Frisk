import discord
from discord.ext import commands

class music():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def play(self, ctx, *, url):
