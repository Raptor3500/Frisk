import discord
from discord.ext import commands
import youtube_dl

class music():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def play(self, ctx, *, url):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        try:
            if players[server.id].is_playing():
                player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

            if server.id in queues:
                queues[server.id].append(player)
            else:
                queues[server.id] = [player]
                await bot.say('Video queued.')
                        
def setup(bot):
    bot.add_cog(music(bot))
