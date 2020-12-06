import discord
from discord.ext import commands
import os
import re


client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

#@client.command()
#async def clear(ctx, amount=3) :
#    await ctx.channel.purge(limit=amount)

@client.command()
async def on_message(message):
    matched = re.match("sa|s.a.|selamın aleyküm|Selamın aleyküm", message)
    if bool(matched):
        msg = 'who'.format(message)
        await message.channel.send('go away lucas')
    await bot.process_commands(message)

    
    
   
client.run(token)
