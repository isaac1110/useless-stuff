import discord
import time
import random
import nacl
import os
from discord.ext import commands
from keep_alive import keep_alive
import asyncio
import math

#client = discord.Client()

global clr
clr = 0x525252
global rainbow
rainbow=[15474944,16751617,16706817,36659,92671,8987285]
global emergency
emergency={}
global emoji
emoji=['🟦','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
global content
content=["ion name",'ion formula (without charges/"ion")',"charges","colour"]
global ionlst
# [name,formula(without charges/"ion"),charges,colour] USE SOURCE CODE GENERATOR
ionlst=[["sodium","Na","1+","colourless"],["potassium","K","1+","colourless"],["copper(I)","Cu","1+","colourless"],["silver","Ag","1+","colourless"],["mercury(I)","Hg","1+","colourless"],["hydrogen","H","1+","colourless"],["ammonium","NH4","1+","colourless"],["magnesium","Mg","2+","colourless"],["calcium","Ca","2+","colourless"],["barium","Ba","2+","colourless"],["lead(II)","Pb","2+","colourless"],["iron(II)","Fe","2+","pale green",9620397],["cobalt(II)","Co","2+","pink",16208197],["nickel(II)","Ni","2+","green",4107149],["manganese(II)","Mn","2+","very pale pink",15381459],["copper(II)","Cu","2+","copperII",40930],["zinc","Zn","2+","colourless"],["mercury(II)","Hg","2+","colourless"],["aluminium","Al","3+","colourless"],["iron(III)","Fe","3+","ironIII",16630795],["chromium(III)","Cr","3+","green",4160817],["hydride","H","1-","colourless"],["chloride","Cl","1-","colourless"],["bromide","Br","1-","colourless"],["iodide","I","1-","colourless"],["hydroxide","OH","1-","colourless"],["nitrate","NO3","1-","colourless"],["nitrite","NO2","1-","colourless"],["hydrogencarbonate","HCO3","1-","colourless"],["hydrogensulphate","HSO4","1-","colourless"],["cyanide","CN","1-","colourless"],["permanganate","MnO4","1-","purple",16711848],["chlorate","ClO3","1-","colourless"],["hypochlorite","ClO","1-","colourless"],["oxide","O","2-","colourless"],["sulphide","S","2-","colourless"],["sulphate","SO4","2-","colourless"],["sulphite","SO3","2-","colourless"],["silicate","SiO3","2-","colourless"],["carbonate","CO3","2-","colourless"],["chromate","CrO4","2-","yellow",16630795],["dichromate","Cr2O7","2-","orange",16029465],["nitride","N","3-","colourless"],["phosphide","P","3-","colourless"],["phosphate","PO4","3-","colourless"]]

def err(mess):
    errembed = discord.Embed(title="Error", description=str("Error: "+mess), color=discord.Color.red())
    return errembed

def prntion(ion):
    global clr
    if len(ion)>4:
        clr=ion[4]
    else:
        clr=0x525252
    if ion[0]=="copper(II)":
        ionembed=discord.Embed(title="copper(II) ion",description="Formula:```Cu```\nCharge:```2+```\nColour:```blue or green```",colour=clr)
    elif ion[0]=="iron(III)":
        ionembed=discord.Embed(title="iron(III) ion",description="Formula:```Fe```\nCharge:```3+```\nColour:```yellow or brown```",colour=clr)
    else:
        ionembed=discord.Embed(title=ion[0]+" ion",description=f"Formula:```{ion[1]}```\nCharge:```{ion[2]}```\nColour:```{ion[3]}```",colour=clr)
    return ionembed

bot = commands.Bot(command_prefix='%', description="This is a trash bot",status=discord.Status.online, activity=discord.Game("with bugs!"))
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
        if (int(lst[-1]))>15:
                warnembed = discord.Embed(title="Warning",description="%spam limited to 15 message.", color=discord.Color.orange())
                await message.channel.send(embed=warnembed)
        #print(lst[1])
        prntstr=""
        for i in range(0,len(lst)-1):
            prntstr+=" "+lst[i]
        for i in range(min(int(lst[-1]),15)):
            if emergency[message.guild.id]:
                return await message.channel.send(embed=err("force stopped"))
            await message.channel.send(prntstr)
            await asyncio.sleep(1)
        
        
@bot.command()
async def pyramid(message,*lst):
    if (len(lst)<2):
        return await message.channel.send(embed=err('not enough parameter'))
    if (not lst[-1].isnumeric()):
        return await message.channel.send(embed=err(str(lst[-1]+' is not a number.')))
    if (int(lst[-1]))>15:
            warnembed = discord.Embed(title="Warning",description="%spam limited to 15 message.", color=discord.Color.orange())
            await message.channel.send(embed=warnembed)
    #print(lst[1])
    prntstr=""
    for i in range(0,len(lst)-1):
        prntstr+=" "+lst[i]
    if (len(prntstr)*min(int(lst[-1]),15)>1900):
        return await message.channel.send(embed=err("message too long"))
    mes="";
    for i in range(min(int(lst[-1]),15)):
        if emergency[message.guild.id]:
            return await message.channel.send(embed=err("force stopped"))
        mes=mes+prntstr
        await message.channel.send(mes)
        await asyncio.sleep(1)

@bot.command()
async def forcestop(message):
    global emergency
    emergency[message.guild.id]=True
    enableembed = discord.Embed(title="Function disabled" , description='Stopping commands', color=discord.Color.red())
    await message.channel.send(embed=enableembed)

@bot.command()
async def enable(message):
    global emergency
    emergency[message.guild.id]=False
    enableembed = discord.Embed(title="Function enabled" , description='Enabling commands', color=discord.Color.green())
    await message.channel.send(embed=enableembed)

@bot.command()
async def ping(message):
    pingembed = discord.Embed(title="Ping test" , description=str('Ping: '+str(bot.latency*1000)+' ms'), color=discord.Color.green())
    await message.channel.send(embed=pingembed)

@bot.command()
async def pingwars(message):
    pingembed = discord.Embed(title="Ping wars" , description=str('Ping: '+str(bot.latency*1000)+' ms'), color=discord.Color.green())
    await message.channel.send(embed=pingembed)
    await message.channel.send("$ping")

    '''elif message.content=="!help":
        helpembed = discord.Embed(title="Commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='raibotite commands help', color=0x525252)
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

async def tacogame(isemoji,message,*act):
    #print(message,act)
    #await message.send(embed=err("testing"))
    if (isemoji):
        act=act[0]
    if (len(act)<1):
        return await message.channel.send(embed=err("not enough parameters."))
    elif act[0]=="build":
        if (len(act)<3):
            return await message.channel.send(embed=err("not enough parameters."))
        elif not act[1].isnumeric():
            return await message.channel.send(embed=err(act[1]+" is not a number."))
        elif not act[2].isnumeric():
            return await message.channel.send(embed=err(act[2]+" is not a number."))
        else:
            if (int(act[1])*int(act[2])>175):
                warnembed = discord.Embed(title="Warning",description="Board is too large and may not display correctly.", color=discord.Color.orange())
                await message.channel.send(embed=warnembed)
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
            await message.channel.send(embed=boardembed)
            flipcnt[message.author]=0
    elif act[0]=="print":
        if (not message.author in boards.keys()):
            return await message.channel.send(embed=err(str(message.author)+" doesnt have a tacoyaki board."))
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
        await message.channel.send(embed=boardembed)
    elif act[0]=="flip":
        if len(act)<3:
            return await message.channel.send(embed=err("not enough parameters."))
        elif not act[1].isnumeric():
            return await message.channel.send(embed=err(act[1]+" is not a number."))
        elif not act[2].isnumeric():
            return await message.channel.send(embed=err(act[2]+" is not a number."))
        elif (not message.author in boards.keys()):
            return await message.channel.send(embed=err(str(message.author)+"doesnt have a tacoyaki board."))
        elif int(act[1])>len(boards[message.author]):
            return await message.channel.send(embed=err("invalid coordinates."))
        elif int(act[2])>len(boards[message.author][0]):
            return await message.channel.send(embed=err("invalid coordinates."))
        elif int(act[1])*int(act[2])==0:
            return await message.channel.send(embed=err("invalid coordinates."))
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
        await message.channel.send(embed=boardembed)
        if won:
            winembed = discord.Embed(title=str(str(message.author)+" won the game!"), url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Flips: "+str(flipcnt[message.author])+"\n```%taco random``` to try again!", color=clr)
            await message.channel.send(embed=winembed)
    elif act[0]=="random":
        if (not message.author in boards.keys()):
            return await message.channel.send(embed=err(str(message.author)+"doesnt have a tacoyaki board."))
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
            #print(tmpx,tmpy)
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
        await message.channel.send(embed=boardembed)
    else:
        return await message.channel.send(embed=err("invalid command."))


@bot.command()
async def taco(message,*act):
    await tacogame(False,message,*act)

async def fp(bse,tme):
    if tme==1:
        return bse
    nnum=await fp(bse,tme//2)
    if not isinstance(nnum, (float, int)):
        return nnum
    #print(math.log10(nnum))
    if math.log10(nnum)>2000:
        return err("number too big, fast power force stopped")
    #print(tme)
    #print(nnum*nnum)
    if (tme%2==0):
        return nnum*nnum
    else:
        return nnum*nnum*bse


@bot.command()
async def calc(message,*oipt):
    ipt="".join(oipt)
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
            rtrn=await fp(num2,int(num1))
            #print(rtrn)
            if not isinstance(rtrn, (float, int)):
                return await message.channel.send(embed=err("fast power force broken"))
            if int(num1)>10000:
                return await message.channel.send(embed=err("number too big"))
            stk2.append(rtrn)
            #stk2.append(float(num2**num1))
        else:
            stk2.append(i)
    fres=stk2.pop()
    if math.log10(fres)<1500:
        resembed = discord.Embed(title="Calculate result", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=ipt+" = "+str(fres), color=clr)
    else:
        restr=str(fres)
        pstr=restr[0]+"."+restr[1:10]+"e+"+str(int(math.log10(fres)))
        resembed = discord.Embed(title="Calculate result", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description=ipt+" = "+pstr, color=clr)
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
        if emergency[message.guild.id]:
            return await message.channel.send(embed=err("force stopped"))
        if (cnum%2)==1:
            cnum=cnum*3+1
        else:
            cnum=cnum//2
        await message.send("-> "+str(cnum))
    #recur(message.channel,int(num))
        
@bot.command()
async def status(message,*content):
    if message.author.id!=640864059763326976:
        return await message.channel.send(embed=err("you're not the bot's creator."))
    elif len(content)<1:
        return await message.channel.send(embed=err("not enough parameters."))
    if content[0]=="listening":
        game = discord.Activity(type=discord.ActivityType.listening, name=' '.join(content[1:]))
        resembed = discord.Embed(title="Changed status", description="Changed status to listening "+' '.join(content[1:]), color=clr)
    elif content[0]=="watching":
        game = discord.Activity(type=discord.ActivityType.watching, name=' '.join(content[1:]))
        resembed = discord.Embed(title="Changed status", description="Changed status to watching "+' '.join(content[1:]), color=clr)
    elif content[0]=="playing":
        game = discord.game(name=' '.join(content[1:]))
        resembed = discord.Embed(title="Changed status", description="Changed status to playing "+' '.join(content[1:]), color=clr)
    else:
        game = discord.Game(' '.join(content))
        resembed = discord.Embed(title="Changed status", description="Changed status to playing "+' '.join(content), color=clr)
    await bot.change_presence(status=discord.Status.online, activity=game)
    await message.send(embed=resembed)

global ans
ans={}

@bot.command()
async def ions(message,*arg):
    #print(arg)
    if (len(arg)<1):
        return await message.channel.send(embed=err("not enough parameters."))
    elif arg[0]=="random":
        randion=random.choice(ionlst)
        #randion=ions[1]
        await message.channel.send(embed=prntion(randion))
    elif arg[0]=="show":
        if len(arg)<2:
            return await message.channel.send(embed=err("not enough parameters."))
        if (arg[1]=="answer"):
            if (not message.author in ans.keys()):
                return await message.channel.send(embed=err(str(message.author)+"doesnt have a ongoing quiz."))
            opt=""
            for i in ans[message.author]:
                opt+=" "
                opt+=i
            ionembed = discord.Embed(title="Quiz answer(s)", description="Answer(s): "+' '.join(ans[message.author]), color=clr)
            return await message.channel.send(embed=ionembed)
        corr=False
        for ion in ionlst:
            if (ion[0].lower()==arg[1].lower() or ion[1].lower()==arg[1].lower()):
                corr=True
                await message.channel.send(embed=prntion(ion))
        if (corr==False):
            return await message.channel.send(embed=err("unknown ion."))
    elif arg[0]=="quiz":
        if len(arg)<2:
            given=random.randint(0,1)
        elif arg[1]=="name":
            given=0
        elif arg[1]=="formula":
            given=1
        else:
            given=random.randint(0,1)
        if len(arg)<3:
            anstype=random.randint(0,3)
            while(anstype==given):
                anstype=random.randint(0,3)
        elif arg[2]=="name":
            anstype=0
        elif arg[2]=="formula":
            anstype=1
        elif arg[2]=="charge":
            anstype=2
        elif arg[2]=="colour" or arg[2]=="color":
            anstype=3
        else:
            anstype=random.randint(0,3)
            while(anstype==given):
                anstype=random.randint(0,3)
        if given==anstype:
            return await message.channel.send(embed=err("bruh dont expect i will give u ans."))
        #print(len(ionlst))
        randion=random.choice(ionlst)
        if (anstype==3 and randion[3]=="colourless"):
            randion=random.choice(ionlst)
        if (anstype==3 and randion[3]=="colourless"):
            randion=random.choice(ionlst)
        #print(randion)
        ans[message.author]=[]
        for ion in ionlst:
            if (randion[given]==ion[given]):
                if ion[anstype]=="copperII":
                    ans[message.author].append("blue")
                    ans[message.author].append("green")
                elif ion[anstype]=="ironIII":
                    ans[message.author].append("yellow")
                    ans[message.author].append("brown")
                else:
                    ans[message.author].append(ion[anstype].lower())
                    if (ion[anstype]=="colourless"):
                        ans[message.author].append("colorless")
                    elif (ion[anstype]=="1+"):
                        ans[message.author].append("+")
                    elif (ion[anstype]=="1-"):
                        ans[message.author].append("-")
        print(ans[message.author])
        ionembed=discord.Embed(title="Ions quiz for "+str(message.author), description='What is the '+content[anstype]+" of "+randion[given]+" ion?\n use ```%ions answer {your answer}``` to answer.", color=clr)
        await message.channel.send(embed=ionembed)
    elif arg[0]=="answer":
        if (not message.author in ans.keys()):
            return await message.channel.send(embed=err(str(message.author)+"doesnt have a ongoing quiz."))
        if len(arg)<2:
            return await message.channel.send(embed=err("please use ```%ion answer {your answer}```"))
        yrans=" ".join(arg[1:])
        if yrans.lower() in ans[message.author]:
            winembed = discord.Embed(title=str(str(message.author)+" answered the quiz correctly!"), description="```use %ions quiz``` to try again!", color=clr)
            await message.channel.send(embed=winembed)
            ans.pop(message.author,None)
        else:
            await message.channel.send("Wrong :( Try again")
    elif arg[0]=="reset":
        if (not message.author in ans.keys()):
            return await message.channel.send(embed=err(str(message.author)+"doesnt have a ongoing quiz."))
        ans.pop(message.author,None)
    else:
        return await message.channel.send(embed=err("invalid command."))

@bot.command()
async def heart(message):
    pingembed = discord.Embed(title="Get trolled lol" , description='I wont make a quiz because someone told me to do so lol (or maybe yes)', color=discord.Color.orange())
    return await message.channel.send(embed=pingembed)

#global stklvl,curr,gd
stklvl=0
curr=0
gd=0

@bot.command()
async def cmd(message,*args):
    if message.author.id!=640864059763326976:
        return await message.channel.send(embed=err("you're not the bot's creator."))
    global stklvl,curr,gd
    if args[0]=="cd":
        if args[1]=="..":
            if stklvl==0:
                return await message.channel.send(embed=err("Alread at root directory"))
            elif stklvl==1:
                #global stklvl
                stklvl=0
            elif stklvl==2:
                #global stklvl,cur
                #global stklvl
                #global curr
                curr=gd
                stklvl=1
            return
        elif stklvl==0:
            for guild in bot.guilds:
                if guild.name==" ".join(args[1:]):
                    #global gd,curr,stklvl
                    #global stklvl
                    #global curr
                    #global gd
                    stklvl=1
                    curr=guild
                    gd=guild
                    #print(stklvl)
                    #print("sucess go ",guild.name)
                    return
            return await message.channel.send(embed=err("Server not found"))
        elif stklvl==1:
            for channel in curr.text_channels:
                if channel.name==args[1]:
                    #global stklvl,curr
                    #global stklvl
                    #global curr
                    stklvl=2
                    curr=channel
                    return
            return await message.channel.send(embed=err("Channel not found"))
        else:
            return await message.channel.send(embed=err("Cannot go further"))
    elif args[0]=="dir":
        cont=""
        if (stklvl==0):
            for guild in bot.guilds:
                cont=cont+str(guild)+"\n"
        elif stklvl==1:
            for channel in curr.text_channels:
                cont=cont+str(channel)+"\n"
        else:
            cont="At leaf, no contents."
        pingembed = discord.Embed(title="Directory contents" , description=cont, color=discord.Color.green())
        return await message.channel.send(embed=pingembed)
    elif args[0]=="send":
        if stklvl==2:
            await curr.send(" ".join(args[1:]))
        else:
            return await message.channel.send(embed=err("Not in channel"))
    else:
        return await message.channel.send(embed=err("Wrong command"))

@bot.event
async def on_message_delete(message):
    #print("detected")
    #print(message.content)
    if "<@!640864059763326976>" in message.content or "<@640864059763326976>" in message.content:
        pingembed = discord.Embed(title=f"{str(message.author)} ghost pinged Raigonite" , description=f'User {str(message.author)} deleted message "{str(message.content)}".', color=discord.Color.orange())
        return await message.channel.send(embed=pingembed)
    elif "<@" in message.content:
        pingembed = discord.Embed(title=f"{str(message.author)} is sus" , description=f'User {str(message.author)} deleted message "{str(message.content)}".', color=discord.Color.orange())
        return await message.channel.send(embed=pingembed)
@bot.command()
async def help(message,*content):
    if len(content)<1:
        helpembed = discord.Embed(title="Commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%help enumeration", value="```Show enumeration commands```", inline=False)
        helpembed.add_field(name="%help vc", value="```Show voice channel commands```", inline=False)
        helpembed.add_field(name="%help util", value="```Show utility commands (eg.testing)```", inline=False)
        helpembed.add_field(name="%help math", value="```Show math commands```", inline=False)
        helpembed.add_field(name="%help taco", value="```Show tacoyaki game commands```", inline=False)
        helpembed.add_field(name="%help chem", value="```Show chemistry commands```", inline=False)
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
        helpembed.add_field(name="%wave", value="```usage: %wave\nfunction: say hi to the bot!```", inline=False)
        helpembed.add_field(name="%pingme", value="```usage: %pingme\nfunction: ping user once```", inline=False)
        helpembed.add_field(name="%forcestop", value="```usage: %forcestop\nfunction: stops all running functions```", inline=False)
        helpembed.add_field(name="%enable", value="```usage: %enable\nfunction: able to use all functions again```", inline=False)
        helpembed.add_field(name="%ping", value="```usage: %ping\nfunction: check bot latency```", inline=False)
    elif content[0]=="math":
        helpembed = discord.Embed(title="Math commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%calc", value="```usage: %calc {expression}\nfunction: calculate {expression}\nIMPORTANT: float and non positive numbers not supported```", inline=False)
        helpembed.add_field(name="%tnpo", value="```usage: %tnpo {value}\nfunction: 3n+1 problem starting at {value}```", inline=False)
    elif content[0]=="taco" or content[0]=="🌮":
        helpembed = discord.Embed(title="Tacoyaki commands help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%taco build", value="```usage: %taco build {row} {column}\nfunction: build a board with size {row}*{column}\nIMPORTANT: use build command before using other tacoyaki commands```", inline=False)
        helpembed.add_field(name="%taco print", value="```usage: %taco print\nfunction: print user's current tacoyaki board```", inline=False)
        helpembed.add_field(name="%taco flip", value="```usage: %taco flip {row} {column}\nfunction: flip the cell {row},{column} and its adjacent cells```", inline=False)
        helpembed.add_field(name="%taco random", value="```usage: %taco random\nfunction: randomize a new board```", inline=False)
    elif content[0]=="chem":
        helpembed = discord.Embed(title="Chemistry commands help",  description='Raibotite commands help', color=clr)
        helpembed.add_field(name="%ions random", value="```usage: %ions random\nfunction: prints a random ion```", inline=False)
        helpembed.add_field(name="%ions show", value='```usage: %ions show {ion name|ion formula|"answer"}\nfunction: shows information of ion/show quiz answer\nexamples: %ions show iron(II)\n%ions show Cr2O7```', inline=False)
        helpembed.add_field(name="%ions quiz", value='```usage: %ions quiz [given type] [answer type]\nfunction: generates a random quiz\n[given type] can be name,formula or random (default by random)\n[answer type] can be name,formula,charge,colour or random (default by random)```', inline=False)
        helpembed.add_field(name="%ions answer", value="```usage: %ions answer {answer}\nfunction: answer the generated quiz```", inline=False)
        helpembed.add_field(name="%ions reset", value="```usage: %ions reset\nfunction: reset quiz```", inline=False)
    else:
        return await message.channel.send(embed=err("invalid category"))
    await message.channel.send(embed=helpembed)

@bot.event
async def on_command_error(error, ctx):
    #print(str(error),str(ctx))
    if isinstance(ctx, commands.CommandNotFound):
        await error.message.channel.send(embed=err("command not found. use %help"))
    else:
        await error.message.channel.send(embed=err(str(ctx)))
        #raise error
    
@bot.event
async def on_message(message):
    #print(message.author.id)
    if (not message.guild.id in emergency.keys()):
        emergency[message.guild.id]=False
    #print(message.channel.id)
    global mention
    mention = f'<@!{bot.user.id}>'
    if message.author.id == bot.user.id:
        return
    '''if message.mention_everyone:
        pingembed = discord.Embed(title="Dont ping @everyone or @here" , description='@everyone and @here is forbidden.', color=discord.Color.orange())
        return await message.channel.send(embed=pingembed)'''
    #print(message.content)
    if "<@!834714836163756064>" in message.content or "<@834714836163756064>" in message.content:
        #print(message.author)
        global raigonite
        raigonite = await message.guild.fetch_member(640864059763326976)
        pingembed = discord.Embed(title="Dont ping me" , description='Ping {} instead.'.format(raigonite.mention), color=discord.Color.orange())
        return await message.channel.send(embed=pingembed)
        #return await message.channel.send('{} wake up'.format(raigonite.mention))
    if len(message.content)<1:
        return
    if message.channel.id==682168643596976226 and message.content[0]=="%":
        pingembed = discord.Embed(title="Dont use raibotite here" , description='READ ANNOUNCEMENT\n> Since @raigonite ‘s @Raibotite is so useless it is now banned in #bot-commands and must be used in #spam ', color=discord.Color.orange())
        return await message.channel.send(embed=pingembed)
    if message.content[0]=="%" and "@" in message.content:
        pingembed = discord.Embed(title="Commands with ping is currently disabled." , description='Your command is blocked because "@" is detected', color=discord.Color.orange())
        return await message.channel.send(embed=pingembed)
    lst=message.content.split()
    #print(lst[0])
    global clr
    #clr=random.choice(rainbow)
    clr=random.randint(0,256**3)
    #print(clr)
    if (len(lst)<1):
        return
    if (lst[0]=="%🌮"):
        await tacogame(True,message,lst[1:])
        return
    await bot.process_commands(message)

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)

'''UPDATE LOG
1.0 release
New commands:
!join !dc !checksleep !hi

1.1 update
New commands:
!spam !pyramid !help
Improved commands:
!checksleep can now specify length

1.2 update
New commands:
%wave %pingme %calc %taco(multiple commands)
Improved commands:
%help now seperated according to category
Changed prefix to %

1.2.1 update
New commands:
%forcestop %enable %tnpo
Improved commands:
%taco now prints row and column number

1.2.1.1 bug fix
Fixed leaked bot TOKEN

1.2.2 update
New commands:
%ping
Improved commands:
%help util now shows %wave
unknown command now shows %help error message
redirects bot ping to @raigonite

1.2.3 update:
Improved commands:
%taco supports taco emoji
%help supports taco emoji
now shows status

1.2.3.1 qol update:
Improved commands:
bot owner can change status
changed status included watching and listening
moved change status code out of on_ready
ping owner actually works

1.2.4 pride month update
Improved commands:
embed now have random colour
taco wrong commands shows invalid command error
fixed taco random not choosing border to flip

1.3 chemistry UPDATE
New commands:
%ions(multiple commands)

1.3.1 update
Improved commands:
quiz on colour will less likely have answer of colourless (~45% chance of colourless)
ions with colour now have correct colour in embed
now supports "color" "colorless" "-" and "+"
forcestop and enable is server independent

1.3.2 bug fix
Improved commands:
@ in message blocked
forcestop will be slightly quicker
spam and pyramid limited to 15 message

1.3.3 small update
Improved commands:
ping bot now wont ping owner anymore to prevent abusing
message that are too long using %pyramid will be blocked

1.3.4 bug fix
New commands:
%cmd for owner
Improved commands:
ping detector improved

1.3.4.1 bug fix
Improved commands:
moved power calculation to async thread and force break too large numbers
numbers larger than 1e1500 uses scientific notation
%calc supports space

1.3.5 small update
Improved commands:
detects ghost ping
---github version split---
'''
