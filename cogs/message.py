import discord
import requests
import json

user = 'rZuTJlFKDZF5oi0T'
key = 'jiaN5JDdXrvjRNFng4t9rlMF47pjazst'

class message():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if 'thank you everyone' in message.content:
            await self.bot.send_message(message.channel, "This message is from Giovanni ^w^ he wanted to say thank you to everyone that means everyone in this server he honestly cares for you all but he doesnt wanna sound gay towards D'Shaun -.- but he loves him too as a friend of course. HEY GET THOSE THOUGHTS OUT OF YOUR HEAD I KNOW YOUR THINKING THEM! .............. Anyways... These are his words exactly 'I love you all thank you, you guys have no idea how much hapiness youve brought me so this is a sever I've made for us since a lot of us have switched to discord. I want us to stay friends so please dont leave. I hope our friendships last forever!' anyways those were his words unless you count mine as well since he coded this")
            
        if not message.author.bot and (message.server == None or self.bot.user in message.mentions):
            await self.bot.send_typing(message.channel)
            txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
            r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'claire', 'text':txt}).text)
            if r['status'] == 'success':
                await self.bot.send_message(message.channel, r['response'] )
                



print('Starting CleverBot...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'claire'})
def setup(bot):
    bot.add_cog(message(bot))
