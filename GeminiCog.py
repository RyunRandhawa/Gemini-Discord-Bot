import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil
from discord.ext import commands
import google.generativeai as genai
import random


genai.configure(api_key=defaultConfig.GEMINI_SDK)

DISCORD_MAX_MESSAGE_LENGTH = 2000
PLEASE_TRY_AGAIN_ERROR_MESSAGE = 'There was an issue with your question please try again...'

class GeminiAgent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.model = genai.GenerativeModel('gemini-2.5-pro')

    @commands.Cog.listener()
    async def on_message(self, msg):
        try:
            content = msg.content.strip().lower()

            # Fun
            # 1. Friendly Greeting
            if content in ["hi", "hello", "hey", "yo", "sup"]:
                await msg.channel.send(f"Hey {msg.author.mention}! 👋")
                return

            # 2. Random Jokes
            if content == "joke":
                jokes = [
                    "Why don’t skeletons fight? They don’t have the guts 💀",
                    "I tried to catch fog yesterday... I mist 😭",
                    "Why was the math book sad? Too many problems 📘",
                    "I told my computer I needed a break… now it won’t stop sending vacation ads 😭"
                    "Why can’t a bicycle stand on its own? It’s two-tired 🚲",
                    "What do you call fake spaghetti? An impasta! 🍝",
                    "Why did the scarecrow win an award? He was outstanding in his field 🐦‍⬛",
                    "I told my computer💻 I needed a break... and now it won’t stop sending me KitKat ads 🍫",
                ]
                await msg.channel.send(random.choice(jokes))
                return

            # 5. Roast Mode
            if content == "roast me":
                roasts = [
                    "You’re not stupid… you just have bad luck thinking 😭",
                    "I’d roast you but nature already did 😮‍💨",
                    "Bro runs on 2 brain cells and one is on break 💀",
                    "Your brain's wifi signal is 0 bars 📶",
                    "You have a face that would make onions cry 🧅",
                    "I look at you and think, “Two billion years of evolution🧬, for this? 🤦",
                    "If laughter is the best medicine💊, your face must be curing the world 🤣",
                    "I was thinking about you today. It reminded me to take out the trash 🗑️",
                    "Don’t worry, the first 40 years of childhood are always the hardest 👶",
                ]
                await msg.channel.send(random.choice(roasts))
                return

            # 7. Random GIF
            if content == "random":
                random_gifs = [
                    "https://tenor.com/view/idk-meme-random-memes-gif-6162206282193369777",
                    "https://tenor.com/view/cat-ruffles-chips-eat-snacks-gif-17892130245513954826",
                    "https://tenor.com/view/rock-one-eyebrow-raised-rock-staring-the-rock-gif-22113367",
                    "https://tenor.com/view/trump-dance-gif-4473210455873429452",
                    "https://tenor.com/view/spidey-gif-17595485508541868367",
                    "https://tenor.com/view/sadhguru-dance-india-gif-15175327419003503672",
                    "https://tenor.com/view/mr-bean-mrbean-bean-mr-bean-holiday-mr-bean-holiday-movie-gif-3228235746377647455",
                    "https://tenor.com/view/huh-bean-face-gif-8925947080554849417",
                    "https://tenor.com/view/mr-bean-mrbean-mister-bean-misterbean-bean-gif-3614564162247595211",
                    "https://tenor.com/view/john-cena-sad-gif-2401481686233028452",
                ]
                await msg.channel.send(random.choice(random_gifs))
                return

            # 9. Random Cat Image
            if content == "cat pls":
                cats = [
                    "https://cataas.com/cat",
                    "https://cataas.com/cat/cute",
                    "https://cataas.com/cat/sleep",
                    "https://cataas.com/cat/funny",
                ]
                await msg.channel.send(random.choice(cats))
                return

            # Imp
            if content == 'ping gemini-agent':
                await msg.channel.send('Agent is Connected')
                return

        except Exception as e:
            await msg.channel.send(PLEASE_TRY_AGAIN_ERROR_MESSAGE + str(e))

    @commands.command()
    async def query(self, ctx, *, question):
        try:
            print('query received')
            response = await self.gemini_generate_content(question)
            await ctx.send(response.text)
        except Exception as e:
            await ctx.send(PLEASE_TRY_AGAIN_ERROR_MESSAGE + str(e))

    @commands.command()
    async def pm(self, ctx):
        dmchannel = await ctx.author.create_dm()
        await dmchannel.send('Hi, how can I help you?')

    async def gemini_generate_content(self, content):
        try:
            return await self.model.generate_content_async(content)
        except Exception as e:
            return PLEASE_TRY_AGAIN_ERROR_MESSAGE + str(e)