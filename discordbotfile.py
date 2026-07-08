import discord
from discord.ext import commands

tufftoken = "MTUyMjMxNzA5NjgxNjc0MjU3MQ.Gaxt_h.qHwMuito41l1h8HsqpsycVLncT9rNGfkCIj59E"
channelid = 1524459268852551892

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("yo sus")
    channel = bot.get_channel(channelid)
    await channel.send("yo hello sus")

@bot.command()
async def sus(ctx, a, b):
    ts = a + b
    await ctx.send("ayo" + ts)

bot.run(tufftoken)

#sus where is my code
#ideas: reminds u to do stuff, tracking stuff outside of discord (like github or like yt), sends random stuff, idea gen
# reaction roles 
#lwk bot that acts like me drooling emoji ts js an llm
