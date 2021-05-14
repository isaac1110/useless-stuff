import discord
import time
import random
import nacl
import os

client = discord.Client()

def err(chn,mess):
    errembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=str("Error: "+mess), color=discord.Color.blue())
    return errembed

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_reaction_add(reaction, user):
    #print(reaction)
    if reaction.emoji == "1️⃣" :
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
          return await message.channel.send(embed=err(message.channel,"user not in any voice channels."))
        global channel
        channel = message.author.voice.channel
        global ctoc
        ctoc = await channel.connect()
        #await change_voice_state(channel,True,True)
        print("i'm in the voice channel ",channel)


    elif message.content.startswith('!dc'):
        #author = message.author
        #print("author: ",author)
        #if message.author.voice is None:
          #return await message.channel.send("You are not in a voice channel")
        channel = message.author.voice.channel
        #print("ctoc: ",ctoc)
        await ctoc.disconnect()
        #await change_voice_state(channel,True,True)
        print("disconnected from ",channel)


    elif message.content.startswith('!checksleep'):
        lst=message.content.split()
        if message.author.voice is None:
          return err(message.channel,"user not in any voice channels.")
        #create reaction embed
        channel = message.author.voice.channel
        desc = "React :one: to prevent get kicked from channel " + str(channel)
        reactembed = discord.Embed(title="Sleep detect", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=desc, color=discord.Color.blue())
        global reactmessage
        reactmessage = await message.channel.send(embed=reactembed);
        global reacted
        reacted = []
        await reactmessage.add_reaction("1️⃣")
        if (len(lst)<2):
            time.sleep(30)
        elif (not lst[1].isnumeric()):
            return await message.channel.send(embed=err(message.channel,str(lst[2]+' is not a number.')))
        else:
            time.sleep(int(lst[1]))
        await reactmessage.add_reaction("1️⃣")
        #delete users
        #newname = "Kicked-users-"+str(random.randint(69,69420))
        #kickchannel = await message.guild.create_voice_channel(newname)
        #global lst
        #lst = channel.members
        lst = channel.voice_states.keys()
        cnt=0
        for i in lst:
            #print(i," ",i.id," ",client.user.id)
            #if i.id == client.user.id:
            #    continue
            if i in reacted:
                print(i," replied")
            else:
                print(i," not replied")
                cnt+=1
                sleptuser = await message.guild.fetch_member(i)
                await sleptuser.move_to(None)
        #await kickchannel.delete
        reactembed = discord.Embed(title="Sleep detect done", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=str('Kicked '+str(cnt)+' user(s).'), color=discord.Color.blue())
        await message.channel.send(embed=reactembed);
    elif message.content.startswith('!spam'):
        lst=message.content.split();
        if (len(lst)<3):
            return await message.channel.send(embed=err(message.channel,'not enough parameter'))
        if (not lst[2].isnumeric()):
            return await message.channel.send(embed=err(message.channel,str(lst[2]+' is not a number.')))
        print(lst[1])
        for i in range(int(lst[2])):
            time.sleep(1)
            await message.channel.send(lst[1])
    elif message.content.startswith('!pyramid'):
        lst=message.content.split();
        if (len(lst)<3):
            return await message.channel.send(embed=err(message.channel,'not enough parameter'))
        if (not lst[2].isnumeric()):
            return await message.channel.send(embed=err(message.channel,str(lst[2]+' is not a number.')))
        print(lst[1])
        mes="";
        for i in range(int(lst[2])):
            mes=mes+lst[1]
            time.sleep(1)
            await message.channel.send(mes)


    elif message.content=="!help":
        helpembed = discord.Embed(title="Commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=0x525252)
        helpembed.add_field(name="!join", value="```usage: !join\nfunction: joins the message user's channel```", inline=False)
        helpembed.add_field(name="!dc", value="```usage: !dc\nfunction: bot will leave its channel```", inline=False)
        helpembed.add_field(name="!checksleep", value="```usage: !checksleep [time]\nfunction: bot kick inactive users from channel after [time] seconds (30 by default)```", inline=False)
        helpembed.add_field(name="!spam", value="```usage: !spam {content} {count}\nfunction: send {content} {count} times```", inline=False)
        helpembed.add_field(name="!pyramid", value="```usage: !pyramid {content} {size}\nfunction: send {content} as a pyramid of size {size}```", inline=False)
        helpembed.add_field(name="!slowpower", value="```usage: !slowpower {base} {power}\nfunction: calculate {base}^{power}```", inline=False)
        helpembed.add_field(name="!pingme", value="```usage: !pingme\nfunction: ping user once```", inline=False)
        await message.channel.send(embed=helpembed)
        #reactmessage = await message.channel.send(embed=reactembed);


    elif message.content=="solve()":
        testembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="use ```sort()``` instead.", color=discord.Color.blue())
        await message.channel.send(embed=testembed)
    elif message.content=="sort()":
        testembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Please use ```#include<bits/stdc++.h>```", color=discord.Color.blue())
        await message.channel.send(embed=testembed)
    elif message.content.startswith("#include"):
        testembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="This is not c++.", color=discord.Color.blue())
        await message.channel.send(embed=testembed)
    elif message.content.startswith('!slowpower'):
        lst=message.content.split()
        if (len(lst)<3):
            return await message.channel.send(embed=err(message.channel,'not enough parameter'))
        if (not lst[2].isnumeric()):
            return await message.channel.send(embed=err(message.channel,str(lst[2]+' is not a number.')))
        if (not lst[1].isnumeric()):
            return await message.channel.send(embed=err(message.channel,str(lst[1]+' is not a number.')))
        testembed = discord.Embed(title="Slow power bot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=str(lst[1]+" ^ "+lst[2]+" = "+str(int(lst[1])**int(lst[2]))), color=discord.Color.blue())
        await message.channel.send(embed=testembed)
    elif message.content.startswith('!pingme'):
        await message.channel.send('{} This is a ping test'.format(message.author.mention))

        


    elif message.content.startswith('!options'):
        options = discord.Embed(title="Ur options", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="1: die\n2: die\n3: die\n", color=discord.Color.blue())
        await message.channel.send(embed=options);

client.run("YOUR TOKEN HERE")
