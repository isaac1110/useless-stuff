import discord
import time
import random
import nacl
import os

#raibotite version 1.0.0

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_reaction_add(reaction, user):
    #print(reaction)
    if reaction.emoji == "1️⃣" :
        global reacted
        reacted = []
        reacted.append(user.id)
        print(user," reacted")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hi'):
        await message.channel.send('Pork is bad and i agree!')
    elif message.content.startswith('!join'):
        author = message.author
        #print("author: ",author)
        if message.author.voice is None:
          return await message.channel.send("You are not in a voice channel")
        global channel
        channel = message.author.voice.channel
        global ctoc
        ctoc = await channel.connect()
        #await change_voice_state(channel,True,True)
        print("i'm in the voice channel ",channel)
    elif message.content.startswith('!dc'):
        author = message.author
        #print("author: ",author)
        if message.author.voice is None:
          return await message.channel.send("You are not in a voice channel")
        channel = message.author.voice.channel
        #print("ctoc: ",ctoc)
        await ctoc.disconnect()
        #await change_voice_state(channel,True,True)
        print("disconnected from ",channel)
    elif message.content.startswith('!checksleep'):
        #create reaction embed
        channel = message.author.voice.channel
        desc = "React :one: to prevent get kicked from channel " + str(channel)
        reactembed = discord.Embed(title="Sleep detect", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=desc, color=discord.Color.blue())
        global reactmessage
        reactmessage = await message.channel.send(embed=reactembed);
        await reactmessage.add_reaction("1️⃣")
        time.sleep(5)
        await reactmessage.add_reaction("1️⃣")
        #delete users
        #newname = "Kicked-users-"+str(random.randint(69,69420))
        #kickchannel = await message.guild.create_voice_channel(newname)
        global lst
        #lst = channel.members
        lst = channel.voice_states.keys()
        global reacted
        for i in lst:
            #print(i," ",i.id," ",client.user.id)
            #if i.id == client.user.id:
            #    continue
            if i in reacted:
                print(i," replied")
            else:
                print(i," not replied")
                sleptuser = await message.guild.fetch_member(i)
                await sleptuser.move_to(None)
        #await kickchannel.delete


    elif message.content.startswith('!options'):
        options = discord.Embed(title="Ur options", url="chrome://dino", description="1: die\n2: die\n3: die\n", color=discord.Color.blue())
        await message.channel.send(embed=options);

client.run("YOUR TOKEN HERE")
