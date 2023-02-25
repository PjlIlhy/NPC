# 0.4D
# New: fixed countdown
# Increased chance to 400
# Secret CODE
import discord
from discord.ext import commands
import asyncio
import random
from secrettoken import TOKEN,VERSION,SECRETCODE
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='J',intents=intents)
@bot.event
async def on_ready():
    print(f"Version: {VERSION}{SECRETCODE}")
    print(f"{bot.user} standing by")
@bot.command()
async def J(ctx):
    normalcoutdown = 1
    home = bot.get_channel(SECRET)
    work = bot.get_channel(SECRET)
    relax = bot.get_channel(SECRET)
    archiv = bot.get_channel(SECRET)
    entrance = bot.get_channel(SECRET)
    def rendom(a,b):
        nummer = random.randint(a,b)
        return nummer
    total = rendom(100,400)
    if total == 300:
        howmuch = 300//3
    else:
        howmuch = total//2
    def reportmaker():
        print("AD")
        f = open("work.txt", "r")
        a = f.read()
        f.close()
        return a
    async def d(work):
        randomwork = random.randint(1,2)
        if randomwork == 1:
            xy = 0
            time = int(reportmaker())
            message = await work.send("**Picks up a stack of documents and start signing**")
            await asyncio.sleep(5)
            while xy < howmuch:
                nummer = rendom(1,100000)
                await message.edit(content=f"**Signed the document under the number: {nummer}**")
                await asyncio.sleep(0.5)
                xy +=1
                print("Working.")
            await work.send("**Taking the report form and filling it out**")
            a = time + 1
            b = str(a)
            with open('work.txt','w') as f:
                f.write(b)
            await work.send("**Put in place with the reports**")
            embed=discord.Embed(title=f"Report {b}", color=0x000000)
            embed.add_field(name="The documents have been signed:", value=str(xy), inline=False)
            embed.add_field(name="Total:", value=str(str(total)), inline=False)
            embed.set_footer(text="Report on the work done")
            await archiv.send(embed=embed)
        elif randomwork == 2:
            xy = 0
            time = int(reportmaker())
            message = await work.send("**Takes a stack of documents and starts stamping**")
            await asyncio.sleep(5)
            while xy < howmuch:
                nummer = rendom(1,100000)
                await message.edit(content=f"**Stamped the document with a number: {nummer}**")
                await asyncio.sleep(0.5)
                xy +=1
                print("Working.")
            await work.send("**Taking the report form and filling it out**")
            await work.send("**Put in place with the reports**")
            a = time + 1
            b = str(a)
            with open('work.txt','w') as f:
                f.write(b)
            embed=discord.Embed(title=f"Report {time}", color=0x000000)
            embed.add_field(name="The documents have been signed:", value=str(xy), inline=False)
            embed.add_field(name="Total:", value=str(str(total)), inline=False)
            embed.set_footer(text="Report on the work done")
            await archiv.send(embed=embed)
    async def elevator():
        print("In elevetor...")
        xy = 0
        message = await work.send("**Riding in an elevator**")
        while xy < 1:
            await message.edit(content=f"**Riding in an elevator.**")
            await asyncio.sleep(13)
            await message.edit(content=f"**Riding in an elevator..**")
            await asyncio.sleep(13)
            await message.edit(content=f"**Riding in an elevator...**")
            await asyncio.sleep(13)
            xy +=1
            print(f"In elevetor... ")
    await home.send("**Wake up**")
    await asyncio.sleep(2)
    await home.send("**Started getting dressed and washing up**")
    await asyncio.sleep(20)
    await home.send("**Took the phone.**")
    await asyncio.sleep(normalcoutdown)
    await home.send("**Went to work**")
    print("Heading to the Work")
    await asyncio.sleep(100)
    await entrance.send("**Went to the bulletin board**")
    await asyncio.sleep(10)
    await entrance.send("**Gos to the turnstile and scan my ID card**")
    await asyncio.sleep(normalcoutdown)
    await entrance.send("**Pass through the turnstile and go to the elevator**")    
    await asyncio.sleep(normalcoutdown)
    await entrance.send("**Took the elevator**")  
    await elevator()
    await work.send("**Sitting in his workplace**")
    await work.send("**Got to work.**")
    await d(work)
    await work.send("So..")
    await work.send("Half done..")
    await asyncio.sleep(2)
    await work.send("I'm going to go get some rest...")
    await asyncio.sleep(normalcoutdown)
    await work.send("**Went to the break room**")
    print("Heading to the Restroom")
    await asyncio.sleep(5)
    await relax.send("**Took 1 euro**")
    await asyncio.sleep(normalcoutdown)
    await relax.send("**Put it in the coffee machine**")
    await relax.send("**Took Latte**")
    await asyncio.sleep(normalcoutdown)
    await relax.send("**Awaiting for the coffee**")
    await asyncio.sleep(60)
    await relax.send("**Took his coffee and went to the couch and sat down**")
    await relax.send("**Drinking coffee**")
    print("Drinking the Coffe")
    await asyncio.sleep(20)
    await relax.send("**Through an empty cup of coffee in the rubbish**")
    await relax.send("It's time to get back to work...")
    await relax.send("**Went to his workplace**")
    await asyncio.sleep(5)
    await work.send("**Sitting in his workplace**")
    await work.send("**Got to work.**")
    await d(work) #Final work
    if total >= 300:
        await work.send("Yeah, that's not half shit! I just did half of it now...")
        await work.send("All right, a breather..")
        print("AH!")
        await asyncio.sleep(normalcoutdown)
        await work.send("**Went to the break room**")
        print("Heading to the Restroom")
        await asyncio.sleep(5)
        await relax.send("**Took 1 euro**")
        await asyncio.sleep(normalcoutdown)
        await relax.send("**Put it in the soda machine**")
        await relax.send("**Picked a can of Coke**")
        await asyncio.sleep(normalcoutdown)
        await relax.send("**Took a can of Coke and went to sit on the couch**")
        await asyncio.sleep(normalcoutdown)
        print("Drinking a Cola")
        await relax.send("**Пью колу**")
        await asyncio.sleep(60)
        await relax.send("**Threw a can of Coke in the trash**")
        await relax.send("Пора дальше работать..")
        await relax.send("**Went to his workplace**")
        await asyncio.sleep(5)
        await work.send("**Sitting in his workplace**")
        await work.send("**Got to work.**")
        await d(work) #Final work
    print("End of the work")
    await work.send("The report is submitted... The plan for today is done...")
    await work.send("**Got up from his desk**")
    await entrance.send("**Took the elevator**")  
    await elevator()
    await entrance.send("**I go to the turnstile and scan my ID card**")
    await asyncio.sleep(normalcoutdown)
    await entrance.send("**Pass through the turnstile and go to the exit**")    
    await asyncio.sleep(normalcoutdown)
    print("Heading to the House")
    await asyncio.sleep(100)
    await home.send("**Opened the door with a fingerprint**")
    await asyncio.sleep(normalcoutdown)
    print("Сhanging clothes")
    await home.send("**Started changing into home clothes**")
    await asyncio.sleep(20)
    baken = 13.33
    print("Cooking")
    # If you want to cook
    await asyncio.sleep(normalcoutdown)
    await home.send("**Going to bed.**")
    await asyncio.sleep(normalcoutdown)
    print("Watching a videos")
    await home.send("**lay down on the bed and watch HeTube**")
    await asyncio.sleep(120)
    await home.send("**Put the phone on the charger and went to bed**")
bot.run(TOKEN)