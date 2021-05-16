import discord
import time
import random
import nacl
import os
from discord.ext import commands
from keep_alive import keep_alive
import asyncio

#client = discord.Client()

global clr
clr = 0x525252
global emergency
emergency=False
global emoji
emoji=['🟦','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']

def err(mess):
    errembed = discord.Embed(title="Error", description=str("Error: "+mess), color=discord.Color.red())
    return errembed

bot = commands.Bot(command_prefix='%', description="This is a trash bot")
bot.remove_command('help')

@bot.command()
async def wave(ctx):
    await ctx.send('hi')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_reaction_add(reaction, user):
    #print('hi')
    #print(reaction)
    if reaction.emoji == "1️⃣" :
        reacted.append(user.id)
        print(user," reacted")

@bot.command()
async def hi(ctx):
    await ctx.send('Pork is bad and i agree!')

@bot.command()
async def join(ctx):
    author = ctx.author
    #print("author: ",author)
    if author.voice is None:
      return await ctx.send(embed=err("user not in any voice channels."))
    global channel
    channel = author.voice.channel
    global ctoc
    ctoc = await channel.connect()
    #await change_voice_state(channel,True,True)
    print("i'm in the voice channel ",channel)

@bot.command()
async def dc(ctx):
    if not 'ctoc' in globals():
        return await ctx.send(embed=err("bot in undefined channel."))
    await ctoc.disconnect()
    print("disconnected from ",channel)

@bot.command()
async def checksleep(ctx,*lst):
        if ctx.author.voice is None:
          return await ctx.send(embed=err("user not in any voice channels."))
        #create reaction embed
        channel = ctx.author.voice.channel
        if (len(lst)<1):
            desc = "React :one: in 30 secs to prevent get kicked from channel " + str(channel)
        elif (not lst[0].isnumeric()):
            return await ctx.channel.send(embed=err(str(lst[0]+' is not a number.')))
        else:
            desc = "React :one: in "+lst[0]+" secs to prevent get kicked from channel " + str(channel)
        reactembed = discord.Embed(title="Sleep detect", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=desc, color=clr)
        global reactmessage
        reactmessage = await ctx.channel.send(embed=reactembed);
        global reacted
        reacted = []
        await reactmessage.add_reaction("1️⃣")
        if (len(lst)<1):
            await asyncio.sleep(30)
        else:
            await asyncio.sleep(int(lst[0]))
        await reactmessage.add_reaction("1️⃣")
        #delete users
        #newname = "Kicked-users-"+str(random.randint(69,69420))
        #kickchannel = await message.guild.create_voice_channel(newname)
        #global lst
        #lst = channel.members
        invc = channel.voice_states.keys()
        cnt=0
        for i in invc:
            #print(i," ",i.id," ",client.user.id)
            #if i.id == client.user.id:
            #    continue
            if i in reacted:
                print(i," replied")
            else:
                print(i," not replied")
                cnt+=1
                sleptuser = await ctx.guild.fetch_member(i)
                await sleptuser.move_to(None)
        #await kickchannel.delete
        reactembed = discord.Embed(title="Sleep detect done", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=str('Kicked '+str(cnt)+' user(s).'), color=clr)
        await ctx.channel.send(embed=reactembed);

@bot.command()
async def spam(message,*lst):
        if (len(lst)<2):
            return await message.channel.send(embed=err('not enough parameter'))
        if (not lst[-1].isnumeric()):
            return await message.channel.send(embed=err(str(lst[-1]+' is not a number.')))
        #print(lst[1])
        prntstr=""
        for i in range(0,len(lst)-1):
            prntstr+=" "+lst[i]
        for i in range(int(lst[-1])):
            if emergency:
                return await message.channel.send(embed=err("force stopped"))
            await asyncio.sleep(1)
            await message.channel.send(prntstr)
        
        
@bot.command()
async def pyramid(message,*lst):
    if (len(lst)<2):
        return await message.channel.send(embed=err('not enough parameter'))
    if (not lst[-1].isnumeric()):
        return await message.channel.send(embed=err(str(lst[-1]+' is not a number.')))
    #print(lst[1])
    prntstr=""
    for i in range(0,len(lst)-1):
        prntstr+=" "+lst[i]
    mes="";
    for i in range(int(lst[-1])):
        if emergency:
            return await message.channel.send(embed=err("force stopped"))
        mes=mes+prntstr
        await asyncio.sleep(1)
        await message.channel.send(mes)

@bot.command()
async def forcestop(message):
    global emergency
    emergency=True
    enableembed = discord.Embed(title="Function disabled" , description='Stopping commands', color=discord.Color.red())
    await message.channel.send(embed=enableembed)

@bot.command()
async def enable(message):
    global emergency
    emergency=False
    enableembed = discord.Embed(title="Function enabled" , description='Enabling commands', color=discord.Color.green())
    await message.channel.send(embed=enableembed)

    '''elif message.content=="!help":
        helpembed = discord.Embed(title="Commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=0x525252)
        helpembed.add_field(name="!join", value="```usage: !join\nfunction: joins the message user's channel```", inline=False)
        helpembed.add_field(name="!dc", value="```usage: !dc\nfunction: bot will leave its channel```", inline=False)
        helpembed.add_field(name="!checksleep", value="```usage: !checksleep [time]\nfunction: bot kick inactive users from channel after [time] seconds (30 by default)```", inline=False)
        helpembed.add_field(name="!spam", value="```usage: !spam {content} {count}\nfunction: send {content} {count} times```", inline=False)
        helpembed.add_field(name="!pyramid", value="```usage: !pyramid {content} {size}\nfunction: send {content} as a pyramid of size {size}```", inline=False)
        helpembed.add_field(name="!slowpower", value="```usage: !slowpower {base} {power}\nfunction: calculate {base}^{power}```", inline=False)
        helpembed.add_field(name="!pingme", value="```usage: !pingme\nfunction: ping user once```", inline=False)
        await message.channel.send(embed=helpembed)
        #reactmessage = await message.channel.send(embed=reactembed);'''


    '''elif message.content=="solve()":
        testembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="use ```sort()``` instead.", color=discord.Color.blue())
        await message.channel.send(embed=testembed)
    elif message.content=="sort()":
        testembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Please use ```#include<bits/stdc++.h>```", color=discord.Color.blue())
        await message.channel.send(embed=testembed)
    elif message.content.startswith("#include"):
        testembed = discord.Embed(title="Error", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="This is not c++.", color=discord.Color.blue())
        await message.channel.send(embed=testembed)'''

@bot.command()
async def slowpower(message,*lst):
    if (len(lst)<2):
        return await message.channel.send(embed=err('not enough parameter'))
    if (not lst[0].isnumeric()):
        return await message.channel.send(embed=err(str(lst[0]+' is not a number.')))
    if (not lst[1].isnumeric()):
        return await message.channel.send(embed=err(str(lst[1]+' is not a number.')))
    testembed = discord.Embed(title="Slow power bot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=str(lst[0]+" ^ "+lst[1]+" = "+str(int(lst[0])**int(lst[1]))), color=clr)
    await message.channel.send(embed=testembed)

@bot.command()
async def pingme(message):
    await message.channel.send('{} This is a ping test'.format(message.author.mention))

global boards
boards={}
global flipcnt
flipcnt={}

@bot.command()
async def taco(message,*act):
    if (len(act)<1):
        return await message.send(embed=err("not enough parameters."))
    elif act[0]=="build":
        if (len(act)<3):
            return await message.send(embed=err("not enough parameters."))
        elif not act[1].isnumeric():
            return await message.send(embed=err(act[1]+" is not a number."))
        elif not act[2].isnumeric():
            return await message.send(embed=err(act[2]+" is not a number."))
        else:
            if (int(act[1])*int(act[2])>175):
                warnembed = discord.Embed(title="Warning",description="Board is too large and may not display correctly.", color=discord.Color.orange())
                await message.send(embed=warnembed)
            boards[message.author] = []
            tmplst=[]
            tmpboard=[]
            for i in range(int(act[2])):
                tmplst.append(False)
            for i in range(int(act[1])):
                tmpboard.append(tmplst)
            boards[message.author]= [[0 for i in range(int(act[2]))]for j in range(int(act[1]))]
            boardstring=""
            if (int(act[1])<=10 and int(act[2])<=10):
                boardstring+=emoji[0]
            if (int(act[2])<=10):
                for i in range(int(act[2])):
                    boardstring+=emoji[i+1]
                boardstring+="\n"
            cnt=1
            for i in range(int(act[1])):
                if (int(act[1])<=10):
                    boardstring+=emoji[cnt]
                    cnt+=1
                for j in range(int(act[2])):
                    if (boards[message.author][i][j]):
                        boardstring+="🟡"
                        print("Y",end="")
                    else:
                        boardstring+="🔴"
                        print("N",end="")
                boardstring+="\n"
                print()
            boardembed = discord.Embed(title=str(str(message.author)+"'s tacoyaki board"), url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=boardstring, color=clr)
            await message.send(embed=boardembed)
            flipcnt[message.author]=0
    elif act[0]=="print":
        if (not message.author in boards.keys()):
            return await message.send(embed=err(str(message.author)+" doesnt have a tacoyaki board."))
        boardstring=""
        if (len(boards[message.author])<=10 and len(boards[message.author][0])<=10):
            boardstring+=emoji[0]
        if len(boards[message.author][0])<=10:
            for i in range(len(boards[message.author][0])):
                boardstring+=emoji[i+1]
            boardstring+='\n'
        cnt=1
        for i in boards[message.author]:
            if (len(boards[message.author])<=10):
                boardstring+=emoji[cnt]
                cnt+=1
            for j in i:
                if j:
                    boardstring+="🟡"
                    #print("Y",end="")
                else:
                    boardstring+="🔴"
                    #print("N",end="")
            boardstring+="\n"
            #print()
        boardembed = discord.Embed(title=str(str(message.author)+"'s tacoyaki board"), url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=boardstring, color=clr)
        await message.send(embed=boardembed)
    elif act[0]=="flip":
        if len(act)<3:
            return await message.send(embed=err("not enough parameters."))
        elif not act[1].isnumeric():
            return await message.send(embed=err(act[1]+" is not a number."))
        elif not act[2].isnumeric():
            return await message.send(embed=err(act[2]+" is not a number."))
        elif (not message.author in boards.keys()):
            return await message.send(embed=err(str(message.author)+" doesnt have a tacoyaki board."))
        elif int(act[1])>len(boards[message.author]):
            return await message.send(embed=err("invalid coordinates."))
        elif int(act[2])>len(boards[message.author][0]):
            return await message.send(embed=err("invalid coordinates."))
        elif int(act[1])*int(act[2])==0:
            return await message.send(embed=err("invalid coordinates."))
        boards[message.author][int(act[1])-1][int(act[2])-1]=not boards[message.author][int(act[1])-1][int(act[2])-1]
        if (int(act[1])>1):
            boards[message.author][int(act[1])-1-1][int(act[2])-1]=not boards[message.author][int(act[1])-1-1][int(act[2])-1]
        if (int(act[1])<len(boards[message.author])):
            boards[message.author][int(act[1])+1-1][int(act[2])-1]=not boards[message.author][int(act[1])+1-1][int(act[2])-1]
        if (int(act[2])>1):
            boards[message.author][int(act[1])-1][int(act[2])-1-1]=not boards[message.author][int(act[1])-1][int(act[2])-1-1]
        if (int(act[2])<len(boards[message.author][0])):
            boards[message.author][int(act[1])-1][int(act[2])+1-1]=not boards[message.author][int(act[1])-1][int(act[2])+1-1]
        flipcnt[message.author]+=1
        print(boards[message.author])
        boardstring="Flip "+str(flipcnt[message.author])+" :\n"
        won=True
        if (len(boards[message.author])<=10 and len(boards[message.author][0])<=10):
            boardstring+=emoji[0]
        if len(boards[message.author][0])<=10:
            for i in range(len(boards[message.author][0])):
                boardstring+=emoji[i+1]
            boardstring+="\n"
        cnt=1
        for i in boards[message.author]:
            if (len(boards[message.author])<=10):
                boardstring+=emoji[cnt]
                cnt+=1
            for j in i:
                if j:
                    boardstring+="🟡"
                    #print("Y",end="")
                else:
                    boardstring+="🔴"
                    #print("N",end="")
                    won=False
            boardstring+="\n"
            #print()
        boardembed = discord.Embed(title=str(str(message.author)+"'s tacoyaki board"), url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=boardstring, color=clr)
        await message.send(embed=boardembed)
        if won:
            winembed = discord.Embed(title=str(str(message.author)+" won the game!"), url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Flips: "+str(flipcnt[message.author])+"\n```%taco random``` to try again!", color=clr)
            await message.send(embed=winembed)
    elif act[0]=="random":
        if (not message.author in boards.keys()):
            return await message.send(embed=err(str(message.author)+" doesnt have a tacoyaki board."))
        flipcnt[message.author]=0
        boardstring="New random board: \n"
        for i in range(len(boards[message.author])):
            for j in range(len(boards[message.author][0])):
                boards[message.author][i][j]=1
        for i in range(len(boards[message.author])*len(boards[message.author][0])):
            tmpx=random.randint(0,len(boards[message.author])-1)
            tmpy=random.randint(0,len(boards[message.author][0])-1)
            boards[message.author][tmpx][tmpy]^=1
            if (tmpx>=1):
                boards[message.author][tmpx-1][tmpy]^=1
            if (tmpx<len(boards[message.author])-1):
                boards[message.author][tmpx+1][tmpy]^=1
            if (tmpy>=1):
                boards[message.author][tmpx][tmpy-1]^=1
            if (tmpy<len(boards[message.author][0])-1):
                boards[message.author][tmpx][tmpy+1]^=1
            print(tmpx,tmpy)
        if (len(boards[message.author])<=10 and len(boards[message.author][0])<=10):
            boardstring+=emoji[0]
        if len(boards[message.author][0])<=10:
            for i in range(len(boards[message.author][0])):
                boardstring+=emoji[i+1]
            boardstring+='\n'
        cnt=1
        for i in boards[message.author]:
            if (len(boards[message.author])<=10):
                boardstring+=emoji[cnt]
                cnt+=1
            for j in i:
                if j:
                    boardstring+="🟡"
                    #print("Y",end="")
                else:
                    boardstring+="🔴"
                    #print("N",end="")
            boardstring+="\n"
        #boardstring+="Please note that this might be unsolvable."
        boardembed = discord.Embed(title=str(str(message.author)+"'s tacoyaki board"), url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=boardstring, color=clr)
        await message.send(embed=boardembed)

@bot.command()
async def calc(message,ipt):
    postord=[]
    stk=[]
    cnum=0
    for i in ipt:
        if i.isnumeric():
            cnum*=10
            cnum+=int(i)
            continue
        if cnum>0:
            postord.append(cnum)
            cnum=0
        if i=='(':
            stk.append('(')
            continue
        elif i==')':
            bad=True
            while (len(stk)>0):
                sttop=stk.pop()
                if sttop=='(':
                    bad=False
                    break
                else:
                    postord.append(sttop)
            if bad:
                return await message.send(embed=err("invalid expression"))
            continue
        elif i=='+' or i=='-':
            while(len(stk)>0):
                sttop=stk.pop()
                if not sttop=='(':
                    postord.append(sttop)
                else:
                    stk.append(sttop)
                    break
            stk.append(i)
        elif i=='*' or i=='/':
            while(len(stk)>0):
                sttop=stk.pop()
                if sttop=='^' or sttop=='*'or sttop=='/':
                    postord.append(sttop)
                else:
                    stk.append(sttop)
                    break
            stk.append(i)
        elif i=='^':
            stk.append(i)
        else:
            return await message.send(embed=err("invalid expression"))
    if cnum>0:
        postord.append(cnum)
    while len(stk)>0:
        postord.append(stk.pop())
    print(postord)
    stk2=[]
    for i in postord:
        if i=='+':
            if len(stk2)<2:
                return await message.send(embed=err("invalid expression"))
            num1=stk2.pop()
            num2=stk2.pop()
            stk2.append(num1+num2)
        elif i=='-':
            if len(stk2)<2:
                return await message.send(embed=err("invalid expression"))
            num1=stk2.pop()
            num2=stk2.pop()
            stk2.append(num2-num1)
        elif i=='*':
            if len(stk2)<2:
                return await message.send(embed=err("invalid expression"))
            num1=stk2.pop()
            num2=stk2.pop()
            stk2.append(num2*num1)
        elif i=='/':
            if len(stk2)<2:
                return await message.send(embed=err("invalid expression"))
            num1=stk2.pop()
            num2=stk2.pop()
            if num1==0:
                return await message.send(embed=err("division by 0"))
            stk2.append(float(num2/num1))
        elif i=='^':
            if len(stk2)<2:
                return await message.send(embed=err("invalid expression"))
            num1=stk2.pop()
            num2=stk2.pop()
            stk2.append(float(num2**num1))
        else:
            stk2.append(i)
    resembed = discord.Embed(title="Calculate result", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=ipt+" = "+str(stk2.pop()), color=clr)
    await message.send(embed=resembed)

def recur(chn,cnum):
    chn.send("-> "+str(cnum))
    if cnum==1:
        return
    if cnum%2 ==0:
        recur(chn,cnum/2)
    else:
        recur(chn,cnum*3+1)

@bot.command()
async def tnpo(message,num):
    if not num.isnumeric():
        return await message.send(embed=err(num+" is not a number."))
    cnum=int(num)
    await message.send("-> "+num)
    while(cnum!=1):
        await asyncio.sleep(1)
        if emergency:
            return await message.channel.send(embed=err("force stopped"))
        if (cnum%2)==1:
            cnum=cnum*3+1
        else:
            cnum=cnum//2
        await message.send("-> "+str(cnum))
    #recur(message.channel,int(num))
        
@bot.command()
async def help(message,*content):
    if len(content)<1:
        helpembed = discord.Embed(title="Commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%help enumeration", value="```Show enumeration commands```", inline=False)
        helpembed.add_field(name="%help vc", value="```Show voice channel commands```", inline=False)
        helpembed.add_field(name="%help util", value="```Show utility commands (eg.testing)```", inline=False)
        helpembed.add_field(name="%help math", value="```Show math commands```", inline=False)
        helpembed.add_field(name="%help taco", value="```Show tacoyaki game commands```", inline=False)
    elif content[0]=="enumeration":
        helpembed = discord.Embed(title="Enumeration commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%spam", value="```usage: %spam {content} {count}\nfunction: send {content} {count} times```", inline=False)
        helpembed.add_field(name="%pyramid", value="```usage: %pyramid {content} {size}\nfunction: send {content} as a pyramid of size {size}```", inline=False)
    elif content[0]=="vc":
        helpembed = discord.Embed(title="Voice channel commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%join", value="```usage: %join\nfunction: joins the message user's channel```", inline=False)
        helpembed.add_field(name="%dc", value="```usage: %dc\nfunction: bot will leave its channel```", inline=False)
        helpembed.add_field(name="%checksleep", value="```usage: %checksleep [time]\nfunction: bot kick inactive users from channel after [time] seconds (30 by default)```", inline=False)
    elif content[0]=="util":
        helpembed = discord.Embed(title="Utility commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%pingme", value="```usage: %pingme\nfunction: ping user once```", inline=False)
        helpembed.add_field(name="%forcestop", value="```usage: %forcestop\nfunction: stops all running functions```", inline=False)
        helpembed.add_field(name="%enable", value="```usage: %enable\nfunction: able to use all functions again```", inline=False)
    elif content[0]=="math":
        helpembed = discord.Embed(title="Math commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%calc", value="```usage: %calc {expression}\nfunction: calculate {expression}\nIMPORTANT: float and non positive numbers not supported```", inline=False)
        helpembed.add_field(name="%tnpo", value="```usage: %tnpo {value}\nfunction: 3n+1 problem starting at {value}```", inline=False)
    elif content[0]=="taco":
        helpembed = discord.Embed(title="Tacoyaki commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%taco build", value="```usage: %taco build {row} {column}\nfunction: build a board with size {row}*{column}\nIMPORTANT: use build command before using other tacoyaki commands```", inline=False)
        helpembed.add_field(name="%taco print", value="```usage: %taco print\nfunction: print user's current tacoyaki board```", inline=False)
        helpembed.add_field(name="%taco flip", value="```usage: %taco flip {row} {column}\nfunction: flip the cell {row},{column} and its adjacent cells```", inline=False)
        helpembed.add_field(name="%taco random", value="```usage: %taco random\nfunction: randomize a new board```", inline=False)
    else:
        return await message.channel.send(embed=err("invalid category"))
    await message.channel.send(embed=helpembed)
    
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
