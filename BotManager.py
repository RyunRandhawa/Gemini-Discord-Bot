import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil

import asyncio
import discord
from discord.ext import commands
from cogs.GeminiCog import GeminiAgent

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!",intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("Bot is online...")

@bot.event
async def on_member_join(member):
    print('New Member is Joining...')
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}! Please read the rules and enjoy your stay!")

@bot.command(aliases=["about"])
async def help(ctx):
    embed = discord.Embed(
        title="🤖 MLSC Bot Commands",
        description="Here are all the commands you can use!",
        color=discord.Color.purple()
    )
    # AI Commands
    embed.add_field(
        name="🧠 AI Commands",
        value=(
            "**!query** — Ask a question to the Gemini AI.\n"
            "**!pm** — Start a private DM conversation with the bot."
        ),
        inline=False
    )
    # Fun Commands
    embed.add_field(
        name="🎉 Fun Commands",
        value=(
            "`hi` — Bot greets you 👋\n"
            "`joke` — Bot tells a random joke 😂\n"
            "`roast me` — Get roasted 🔥\n"
            "`random` — Random funny GIF 🎞️\n"
            "`cat pls` — Random cat image 🐱"
        ),
        inline=False
    )
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKQw4N0kdAQYkdtyOwmjfkCyVQnnZ7EWxF6A&s")
    embed.set_footer(text="Made by Ryun Randhawa👑")

    await ctx.send(embed=embed)

@bot.command()
@commands.check(discordUtil.is_me)
async def unloadGemini(ctx):                #Stops the bot from responding to messages
    await bot.remove_cog('GeminiAgent')

@bot.command()
@commands.check(discordUtil.is_me)
async def reloadGemini(ctx):                #Starts the bot from responding to messages
    await bot.add_cog(GeminiAgent(bot))

async def startcogs():
    await bot.add_cog(GeminiAgent(bot))

asyncio.run(startcogs())
bot.run(defaultConfig.DISCORD_TOKEN)