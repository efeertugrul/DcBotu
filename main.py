import discord
from discord.ext import commands
import os
import re
import random

def switch(value):
    cases = {0:'Aleyküm selam ya müslüman!',
            1:'ALLAHU EKBER!!!!',
            2:'ilahi mi açtın mübarek?'}
    return cases[value]

seriatOn = True
client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")


if token == None:
    print("Za")
    f = open("token","r")
    token = f.readline()
    print(token)
else:
    print(token)


@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command()
async def seriat(ctx):
    if seriatOn:
        seriatOn = False
        await ctx.send(f"Şeriatı kaldırdık!")
    else:
        seriatOn = True
        await ctx.send(f"Şeriat yükleniyor...")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message):
    if seriatOn:
        matchlist = ["s.a|sa|s.a.|selamın aleyküm|Selamın aleyküm", "TEKBİR|tekbir", "-p"]

        count = 0
        for x in matchlist:
            matched = re.match(x, message.content)
            if(bool(matched)):
                response = switch(count)
                if count == 2:
                    if random.randint(0, 100)%11!=0:
                        break
                await message.channel.send(response)
                break
            count += 1
    await client.process_commands(message)

    
    
   
client.run(token)
