import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql
import string
from discord.utils import get

playerList1 = []
playerList2 = []
playerList3 = []
uplay1 = []
uplay2 = []
uplay3 = []

war = []
war1 = []
war2 = []
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
status = cycle(['.help for help', 'BETA Version', 'Rainbow Six Siege'])
print('bot launching')


@client.event
async def on_ready():
    change_status.start()
    print('Bot is Ready.')


# @client.event
# async def on_member_join(member):
   #  print(f'{member} has joined the server.')


# @client.event
# async def on_member_remove(member):
  #   print(f'{member} has left the server.')


# @client.command(aliases=['8ball', 'test'])
# async def _8ball(ctx,*,question):
  #   responses = [1,2,3,4,5,6,7,8,9,10,11,22]
   #  await ctx.send(f'Question: {question}\n answer: {random.choice(responses)}')


@client.command()
async def on_command_error(ctx, error):
    pass


@client.command(aliases=['c', 'C'])
@commands.has_permissions(administrator=True)
async def clear(ctx):
    global playerList1
    global uplay1
    msg_lst = []
    embed = discord.Embed(
        title='PA help', description=f'Queue Reset ', colour=discord.Colour.red())
    await ctx.send(embed=embed)
    for i in playerList1:
        msg_lst.append(i.mention)
    await ctx.send(msg_lst)
    playerList1 = []
    uplay1 = []


@client.command()
async def report(ctx, *, elreport):

    report = ctx.guild.get_channel(765963956560199700)

    await report.send(f'report: {elreport}')
    botMSG1 = await ctx.send('thank you for your report')
    await asyncio.sleep(2)
    await botMSG1.delete()
    await ctx.message.delete()


# @client.command(aliases = ['sug'])
# async def suggest(ctx,*,elsuggest):

#     suggest = ctx.guild.get_channel(726550277355733094)

#     await suggest.send(f'Suggestion: {elsuggest}')
#     botMSG2 = await ctx.send('thank you for your suggestion ')
#     await asyncio.sleep(3)
#     await botMSG2.delete()
#     await ctx.message.delete()


@client.command(aliases=['PLAYER'])
async def player(ctx, *, Argument=None):
    if ctx.channel.id == 765219179372216361 or ctx.channel.id == 726537235477823528:
        if Argument != None:
            pass
        else:
            myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
            async with myDB.cursor() as cur:
                await cur.execute("SELECT name FROM test1.whatever ")
                PlayerID = await cur.fetchall()
                feWa7d = 0
                for i in PlayerID:
                    if (f'{ctx.author.id}',) == i:
                        feWa7d = feWa7d+1

                if feWa7d == 0:
                    Bembed = discord.Embed(
                        title='WELCOME!', description=None, colour=discord.Colour.blue())
                    Bembed.add_field(name="🖊", value=f"Register", inline=True)
                    # Bembed.add_field(name="l", value=f"l", inline=True)
                    # Bembed.add_field(name="🏛 ", value=f"Create A Team", inline=True)
                    PbotMSG = await ctx.author.send(embed=Bembed)
                    await PbotMSG.add_reaction('🖊')
                    # await PbotMSG.add_reaction('🏛')
                else:
                    Bembed = discord.Embed(
                        title='Player menu:', description=None, colour=discord.Colour.blue())
                    Bembed.add_field(
                        name="📄", value=f"Change uplay name", inline=True)
                    # Bembed.add_field(name="l", value=f"l", inline=True)
                    # Bembed.add_field(name="🏛 ", value=f"Create A Team", inline=True)
                    PbotMSG = await ctx.author.send(embed=Bembed)
                    await PbotMSG.add_reaction('📄')
                    # await PbotMSG.add_reaction('🏛')
    else:
        embed = discord.Embed(
            title='PA help', description=f'{ctx.author.mention} , You can use .player only in Register channel', colour=discord.Colour.red())
        botMSG1 = await ctx.send(embed=embed)
        await asyncio.sleep(15)
        await botMSG1.delete()
        await ctx.message.delete()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


Qsize = 10


Maps = ['Coastline!https://cdn.discordapp.com/attachments/726400773122162730/757707782572081152/CoastlineOverheadView.png', 'Oregon!https://cdn.discordapp.com/attachments/726400773122162730/757707989934407761/Oregon_Rework.jpg', 'Club house!https://cdn.discordapp.com/attachments/726400773122162730/757708443145470093/Siege_Clubhouse_Thumbnail.jpg', 'Villa!https://cdn.discordapp.com/attachments/726400773122162730/757699063490805830/534px-R6S_map_villa.jpg',
        'Consulate!https://cdn.discordapp.com/attachments/726400773122162730/757708687518466149/Siege_Consulate_Thumbnail.PNG.png', 'Kafe Dostoyevsky!https://cdn.discordapp.com/attachments/726400773122162730/757708942309589082/maxresdefault_1.jpg', 'Chalet!https://cdn.discordapp.com/attachments/424327908761403392/822612749313507379/ChaletReworkRainbowSix.png']
PMaps = []


@client.command(aliases=['q', 'Q', 'QUEUE'])
async def queue(ctx, argument=None):

    global Maps
    global PMaps
    global playerList1
    global playerList2
    global playerList3
    global uplay1
    global uplay2
    global uplay3
    picked = 0
    shbab = []
    mwjod = 0
    myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB.cursor() as cur:
        await cur.execute(f"SELECT `name` FROM `whatever`")
        await myDB.commit()
        up = await cur.fetchall()
        for i in up:
            i = ''.join(i)
            shbab.append(i)
        for i in shbab:
            if i == f'{ctx.author.id}':
                mwjod = 1
    if mwjod != 1:
        embed = discord.Embed(
            title="PA help", description=f"{ctx.author.mention} ,You need to register using .player ", colour=discord.Colour.red())
        await ctx.send(embed=embed)
    else:
        myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='game id')
        async with myDB.cursor() as cur:
            await cur.execute("SELECT `Team 1` FROM `games` WHERE won = 0")
            data = await cur.fetchall()
            await cur.execute("SELECT `Team 2` FROM `games` WHERE won = 0")
            data1 = await cur.fetchall()
            data2 = []
            for i in data:
                i = ''.join(i)
                data2.append(i)
            for j in data1:
                j = ''.join(j)
                data2.append(j)
            jwa = 0
            for k in data2:
                if k == str(ctx.author.id):
                    jwa = jwa + 1
            if jwa != 0:
                embed = discord.Embed(
                    title="Queue help", description=f"{ctx.author.mention} , You must finish your game first ", colour=discord.Colour.red())
                await ctx.send(embed=embed)
            else:

                myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
                if ctx.message.channel.id == 765220691888832542 or ctx.message.channel.id == 765974936929042452:  # -------------------------------pc
                    if argument in ['join', 'j', 'J']:
                        if ctx.author in playerList1:

                            embed = discord.Embed(
                                title="Queue help", description=f"{ctx.author.mention} , You are already in the Queue ", colour=discord.Colour.green())
                            await ctx.send(embed=embed)

                        else:
                            async with myDB.cursor() as cur:
                                await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
                                uplai = await cur.fetchall()
                                for i in uplai:
                                    i = ''.join(i)
                                uplay1.append(i)
                                playerList1.append(ctx.author)
                                embed = discord.Embed(
                                    title="Queue help", description=f"{ctx.author.mention} has joined the queue\n there are {len(playerList1)} Players out of 10 ", colour=discord.Colour.green())
                                await ctx.send(embed=embed)

                    elif argument in ['l', 'leave', 'L']:
                        if ctx.author in playerList1:
                            async with myDB.cursor() as cur:
                                await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
                                uplao = await cur.fetchall()
                                for i in uplao:
                                    i = ''.join(i)
                                if i in uplay1:
                                    uplay1.remove(i)
                                else:
                                    pass
                                playerList1.remove(ctx.author)
                                embed = discord.Embed(
                                    title="Queue help", description=f"{ctx.author.mention} , has left the queue ", colour=discord.Colour.red())
                                await ctx.send(embed=embed)

                        else:
                            embed = discord.Embed(
                                title="Queue help", description=f"{ctx.author.mention} , you are not in the Queue ", colour=discord.Colour.red())
                            await ctx.send(embed=embed)

                    elif argument == None:
                        embed = discord.Embed(
                            title="Queue help", description=f"{len(playerList1)} Players out of 10 ", colour=discord.Colour.blue())
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            title=f'Queue help', description=f"{ctx.author.mention}, USE (.q j) to join OR (.q L) to leave", colour=discord.Colour.blurple())
                        await ctx.send(embed=embed)

                    if len(playerList1) >= Qsize:
                        Team1 = []
                        Team2 = []

                        n = 0
                        if len(PMaps) == 7:
                            PMaps = []

                        while picked == 0:
                            M = random.choice(Maps)
                            if M in PMaps:
                                pass
                            else:
                                PMaps.append(M)
                                M = M.split("!")
                                elmap = M[0]
                                elurl = M[1]
                                elurl = elurl.replace(" ", "")
                                elurl = elurl.replace("'", "")
                                picked = 1

                        myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='game id')
                        async with myDB.cursor() as cur:
                            await cur.execute("SELECT `Game_id` FROM `games`")
                            data = await cur.fetchall()
                            data2 = []
                            for i in data:
                                i = ''.join(i)
                                data2.append(i)  # getting all game id names
                            gen_id = []
                            for i in range(0, len(data2) + 1):
                                rn = random.randint(0, 9)
                                rl = random.choice(string.ascii_letters)
                                GameID = f"{rl}-{rn}"
                                gen_id.append(GameID)
                            for i in gen_id:
                                for t in data2:
                                    if t != i:
                                        GameID = i

                            while n < Qsize/2:
                                n = n+1
                                chosenP = random.choice(playerList1)
                                Team1.append(chosenP.mention)
                                playerList1.remove(chosenP)
                                chosenP1 = random.choice(playerList1)
                                Team2.append(chosenP1.mention)
                                playerList1.remove(chosenP1)
                                await cur.execute(f"INSERT INTO `games` (`Team 1`, `Team 2`, `Game_id`, `Won`, `sign`) VALUES ('{chosenP.id}','{chosenP1.id}','{GameID}', 0, 0)")
                                await myDB.commit()

                        embed = discord.Embed(
                            title=f'Map: {elmap}', description=f"{GameID}", colour=discord.Colour.blue())
                        count = 1
                        orange_player_string = ""
                        for i in Team1:
                            orange_player_string = f"{orange_player_string}" + \
                                f"{count} - " + f"{i}" + "\n"
                            count = count + 1
                        count1 = 1
                        Blue_player_string = ""
                        for i in Team2:
                            Blue_player_string = f"{Blue_player_string}" + \
                                f"{count1} - " + f"{i}" + "\n"
                            count1 = count1 + 1

                        embed.add_field(
                            name="Orange Team ", value=f"{orange_player_string}", inline=True)
                        embed.add_field(
                            name="Blue Team ", value=f"{Blue_player_string}", inline=True)
                        embed.add_field(name='Uplay Names:',
                                        value=f'{uplay1}', inline=True)
                        embed.set_image(url=f'{elurl}')
                        await ctx.send(embed=embed)
                        await ctx.send(Team1 + Team2)

                        results = ctx.guild.get_channel(765969729910997023)
                        botMSG4 = await results.send(f'Match : {GameID}')
                        await botMSG4.add_reaction('🟧')
                        await botMSG4.add_reaction('🟦')
                        await botMSG4.add_reaction('✖')
                        uplay1 = []
                        await ctx.send(f'{chosenP.mention} you are the host')

            # elif ctx.message.channel.id == 728640805102682165 : #-----------------------------------ps4
            #     if argument in ['join','j'] :
            #         if ctx.author in playerList2:

            #             await ctx.send(f'{ctx.author.mention}, you are already in the Queue')

            #         else:
            #             async with myDB.cursor() as cur:
            #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
            #                 uplai = await cur.fetchall()
            #                 for i in uplai:
            #                     i = ''.join(i)
            #                 uplay2.append(i)
            #                 playerList2.append(ctx.author)
            #                 await ctx.send(f'{ctx.author.mention} has joined the queue')
            #                 await ctx.send(f'there are {len(playerList2)} Players out of 10')

            #     elif argument in ['l','leave']:
            #         if ctx.author in playerList2:
            #             async with myDB.cursor() as cur:
            #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = '{ctx.author.id}'")
            #                 uplai = await cur.fetchall()
            #                 for i in uplai:
            #                     i = ''.join(i)
            #                 uplay2.remove(i)
            #                 playerList2.remove(ctx.author)
            #                 await ctx.send(f'{ctx.author.mention} has left the queue')

            #         else:
            #             await ctx.send(f'{ctx.author.mention} you are not in the Queue')

            #     elif argument == None:
            #         await ctx.send(f'{len(playerList2)} Players out of 10')
            #     else :
            #         await ctx.send('Invalid Argument')

            #     if len(playerList2)  >= Qsize:
            #         Team12 = []
            #         Team22 = []

            #         n = 0

            #         myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
            #         async with myDB.cursor() as cur:
            #             await cur.execute("SELECT `Game_id` FROM `games`")
            #             data = await cur.fetchall()
            #             data2 = []
            #             for i in data:
            #                 i = ''.join(i)
            #                 data2.append(i)     #getting all game id names
            #             gen_id = []
            #             for i in range(0, len(data2) + 1):
            #                 rn = random.randint(0,9)
            #                 rl = random.choice(string.ascii_letters)
            #                 GameID = f"{rl}-{rn}"
            #                 gen_id.append(GameID)
            #             for i in gen_id :
            #                 for t in data2:
            #                     if t != i :
            #                         GameID = i

            #             while n<Qsize/2 :
            #                 n = n+1
            #                 chosenP2 = random.choice(playerList2)
            #                 Team12.append(chosenP2.mention)
            #                 playerList2.remove(chosenP2)
            #                 chosenP3 = random.choice(playerList2)
            #                 Team22.append(chosenP3.mention)
            #                 playerList2.remove(chosenP3)
            #                 await cur.execute(f"INSERT INTO `games` (`Team 1`, `Team 2`, `Game_id`, `Won`, `sign`) VALUES ('{chosenP2.id}','{chosenP3.id}','{GameID}', 0, 0)")
            #                 await myDB.commit()

            #         await ctx.send(f'Orange Team  : {Team12}')
            #         await ctx.send(f'Blue Team  : {Team22}')
            #         await ctx.send(f'Map: {random.choice(Maps)}')
            #         await ctx.send(f'Match ID : {GameID}')
            #         await ctx.send(f'uplay names: {uplay2}')
            #         uplay2 = []
            #         await ctx.send(f'{chosenP2.mention} you are the host')
            #         results = ctx.guild.get_channel(728759249064427580)
            #         botMSG4 = await results.send(f'Match : {GameID}')
            #         await botMSG4.add_reaction('🟧')
            #         await botMSG4.add_reaction('🟦')
            #         await botMSG4.add_reaction('✖')

            # elif ctx.message.channel.id == 728640828934979664 : #-----------------------------------XBOX
            #     if argument in ['join','j'] :
            #         if ctx.author in playerList3:

            #             await ctx.send(f'{ctx.author.mention}, you are already in the Queue')

            #         else:
            #             async with myDB.cursor() as cur:
            #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = {ctx.author.id}")
            #                 uplai = await cur.fetchall()
            #                 for i in uplai:
            #                     i = ''.join(i)
            #                 uplay3.append(i)
            #                 playerList3.append(ctx.author)
            #                 await ctx.send(f'{ctx.author.mention} has joined the queue')
            #                 await ctx.send(f'there are {len(playerList3)} Players out of 10')

            #     elif argument in ['l','leave']:
            #         if ctx.author in playerList3:
            #             async with myDB.cursor() as cur:
            #                 await cur.execute(f"SELECT `uplay` FROM `whatever` WHERE name = {ctx.author.id}")
            #                 uplai = await cur.fetchall()
            #                 for i in uplai:
            #                     i = ''.join(i)
            #                 uplay3.remove(i)
            #                 playerList3.remove(ctx.author)
            #                 await ctx.send(f'{ctx.author.mention} has left the queue')

            #         else:
            #             await ctx.send(f'{ctx.author.mention} you are not in the Queue')

            #     elif argument == None:
            #         await ctx.send(f'{len(playerList3)} Players out of 10')
            #     else :
            #         await ctx.send('Invalid Argument')

            #     if len(playerList1)  >= Qsize:
            #         Team13 = []
            #         Team23 = []

            #         n = 0

            #         myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
            #         async with myDB.cursor() as cur:
            #             await cur.execute("SELECT `Game_id` FROM `games`")
            #             data = await cur.fetchall()
            #             data2 = []
            #             for i in data:
            #                 i = ''.join(i)
            #             data2.append(i)     #getting all game id names
            #             gen_id = []
            #             for i in range(0, len(data2) + 1):
            #                 rn = random.randint(0,9)
            #                 rl = random.choice(string.ascii_letters)
            #                 GameID = f"{rl}-{rn}"
            #                 gen_id.append(GameID)
            #             for i in gen_id :
            #                 for t in data2:
            #                     if t != i :
            #                         GameID = i

            #             while n<Qsize/2 :
            #                 n = n+1
            #                 chosenP4 = random.choice(playerList3)
            #                 Team13.append(chosenP4.mention)
            #                 playerList3.remove(chosenP4)
            #                 chosenP5 = random.choice(playerList3)
            #                 Team23.append(chosenP5.mention)
            #                 playerList3.remove(chosenP5)
            #                 await cur.execute(f"INSERT INTO `games` (`Team 1`, `Team 2`, `Game_id`, `Won`, `sign`) VALUES ('{chosenP4.id}','{chosenP5.id}','{GameID}', 0, 0)")
            #                 await myDB.commit()

            #         await ctx.send(f'Orange Team  : {Team13}')
            #         await ctx.send(f'Blue Team  : {Team23}')
            #         await ctx.send(f'Map: {random.choice(Maps)}')
            #         await ctx.send(f'Match ID : {GameID}')
            #         results = ctx.guild.get_channel(728759249064427580)
            #         botMSG4 = await results.send(f'Match : {GameID}')
            #         await botMSG4.add_reaction('🟧')
            #         await botMSG4.add_reaction('🟦')
            #         await botMSG4.add_reaction('✖')
            #         await ctx.send(f'uplay names: {uplay3}')
            #         uplay3 = []
            #         await ctx.send(f'{chosenP4.mention} you are the host')

                else:
                    embed = discord.Embed(
                        title='PA help', description=f'{ctx.author.mention}, You are not in the Queue Channel', colour=discord.Colour.red())
                    await ctx.send(embed=embed)


@client.event
async def on_reaction_add(react: discord.Reaction, person: discord.User):
    mwjod = 0
    Tmwjod = 0
    squadsN = 0
    squadN = 0

    if react.message.channel.id == 765969729910997023:
        if person.id == 725433666481946736:
            pass
        else:
            if str(react) == '🟧':
                FGID = react.message.content[8:]
                myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='game id')
                myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
                async with myDB.cursor() as cur:
                    await cur.execute(f"SELECT `Team 1` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                    await myDB.commit()
                    WonT = await cur.fetchall()
                    await cur.execute(f"SELECT `Team 2` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                    await myDB.commit()
                    LosT = await cur.fetchall()
                    await cur.execute(f"UPDATE `games` SET `Won`= 1,`sign`='{person}' WHERE Game_id = '{FGID}' AND Won = '0'")
                    await myDB.commit()
                async with myDB1.cursor() as cur1:
                    for i in WonT:
                        i = ''.join(i)
                        await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`+50,`Games_Played`=`Games_Played`+1,`Games_won`=`Games_won`+1 WHERE name = {i}")
                        await myDB1.commit()
                    for i in LosT:
                        i = ''.join(i)
                        await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`-50,`Games_Played`=`Games_Played`+1,`Games_Lost`=`Games_Lost`+1 WHERE name = {i}")
                        await myDB1.commit()
                await react.message.clear_reaction('🟧')
                await react.message.clear_reaction('🟦')
                await react.message.clear_reaction('✖')

            elif str(react) == '🟦':
                FGID = react.message.content[8:]
                myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='game id')
                myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
                async with myDB.cursor() as cur:
                    await cur.execute(f"SELECT `Team 2` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                    await myDB.commit()
                    WonT = await cur.fetchall()
                    await cur.execute(f"SELECT `Team 1` FROM `games` WHERE Game_id = '{FGID}' AND Won = '0'")
                    await myDB.commit()
                    LosT = await cur.fetchall()
                    await cur.execute(f"UPDATE `games` SET `Won`= 2,`sign`='{person}' WHERE Game_id = '{FGID}' AND Won = '0'")
                    await myDB.commit()
                async with myDB1.cursor() as cur1:
                    for i in WonT:
                        i = ''.join(i)
                        await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`+50,`Games_Played`=`Games_Played`+1,`Games_won`=`Games_won`+1 WHERE name = {i}")
                        await myDB1.commit()
                    for i in LosT:
                        i = ''.join(i)
                        await cur1.execute(f"UPDATE `whatever` SET `MMR`=`MMR`-50,`Games_Played`=`Games_Played`+1,`Games_Lost`=`Games_Lost`+1 WHERE name = {i}")
                        await myDB1.commit()
                await react.message.clear_reaction('🟧')
                await react.message.clear_reaction('🟦')
                await react.message.clear_reaction('✖')

            elif str(react) == '✖':
                FGID = react.message.content[8:]
                myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='game id')
                async with myDB.cursor() as cur:
                    await cur.execute(f"DELETE FROM `games` WHERE Game_id = '{FGID}'")
                    await myDB.commit()
                await react.message.clear_reaction('🟧')
                await react.message.clear_reaction('🟦')
                await react.message.clear_reaction('✖')

            elif str(react) == '🔶':
                war2 = []
                await react.message.clear_reaction('🔶')
                await react.message.clear_reaction('🔷')
                FGID = react.message.content[8:]
                FGID = FGID.split(" ")
                elefaz = FGID[0]
                elefaz = elefaz.replace("'", "")
                elefaz = elefaz.replace(" ", "")
                ele5sr = FGID[-1]
                ele5sr = ele5sr.replace("'", "")
                ele5sr = ele5sr.replace(" ", "")
                myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
                async with myDB.cursor() as cur:
                    await cur.execute(f"UPDATE `tournament` SET `stage`='2' WHERE Team = '{elefaz}'")
                    await myDB.commit()
                    await asyncio.sleep(3)
                    await cur.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '2'")
                    await myDB.commit()
                    jwab = await cur.fetchall()
                    for i in jwab:
                        i = ''.join(i)
                        war2.append(i)

                if len(war2) >= 2:
                    chosenT = random.choice(war2)
                    war2.remove(chosenT)
                    chosenT1 = random.choice(war2)
                    war2.remove(chosenT1)
                    embed = discord.Embed(
                        title="SEMI-FINALE", description=f'{chosenT} vs {chosenT1}', colour=discord.Colour.red())
                    clanwarch = react.message.guild
                    clanwarch = clanwarch.get_channel(765984718713782272)
                    await clanwarch.send(embed=embed)
                    async with myDB.cursor() as cur:
                        await cur.execute(f"UPDATE `tournament` SET `stage`='0' WHERE Team = '{chosenT}' OR Team = '{chosenT1}'")
                        await myDB.commit()

            elif str(react) == '🔷':
                war2 = []
                await react.message.clear_reaction('🔶')
                await react.message.clear_reaction('🔷')
                FGID = react.message.content[8:]
                FGID = FGID.split(" ")
                ele5sr = FGID[0]
                ele5sr = ele5sr.replace("'", "")
                ele5sr = ele5sr.replace(" ", "")
                elefaz = FGID[-1]
                elefaz = elefaz.replace("'", "")
                elefaz = elefaz.replace(" ", "")
                myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
                async with myDB.cursor() as cur:
                    await cur.execute(f"UPDATE `tournament` SET `stage`='2' WHERE Team = '{elefaz}'")
                    await myDB.commit()
                    await asyncio.sleep(3)
                    await cur.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '2'")
                    await myDB.commit()
                    jwab = await cur.fetchall()
                    for i in jwab:
                        i = ''.join(i)
                        war2.append(i)

                if len(war2) >= 2:
                    chosenT = random.choice(war2)
                    war2.remove(chosenT)
                    chosenT1 = random.choice(war2)
                    war2.remove(chosenT1)
                    embed = discord.Embed(
                        title="SEMI-FINALE", description=f'{chosenT} vs {chosenT1}', colour=discord.Colour.red())
                    clanwarch = react.message.guild
                    clanwarch = clanwarch.get_channel(765984718713782272)
                    await clanwarch.send(embed=embed)
                    async with myDB.cursor() as cur:
                        await cur.execute(f"UPDATE `tournament` SET `stage`='0' WHERE Team = '{chosenT}' OR Team = '{chosenT1}'")
                        await myDB.commit()

    else:

        if person.id == 725433666481946736:
            pass

        else:
            myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='game id')
            myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')

            if str(react) == '🔎':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Player` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                    else:
                        pass
                    if mwjod == 0:
                        await react.message.delete()
                        await cur1.execute(f"SELECT `Team` FROM `clan`")
                        await myDB1.commit()
                        teams = await cur1.fetchall()
                        alteam = []
                        for i in teams:
                            i = ''.join(i)
                            if i in alteam:
                                pass
                            else:
                                alteam.append(i)
                        Teams_string = ""
                        count = 1
                        TeamN = ''
                        for i in alteam:
                            Teams_string = f"{Teams_string}" + \
                                f"{count} - " + f"{i}" + "\n"
                            count = count + 1
                        Aembed = discord.Embed(
                            title=f'Teams Names:', description=None, colour=discord.Colour.blue())
                        Aembed.add_field(
                            name="please write the team's name you want to join", value=f"{Teams_string}", inline=True)
                        await person.send(embed=Aembed)

                        def check(m):
                            return m.content and m.author.id != 725433666481946736 and m.author == person
                        msg = await client.wait_for('message', check=check)
                        TeamN = str(msg.content.upper().replace(' ', ''))

                        if TeamN in alteam:
                            await cur1.execute(f"SELECT `Captin` FROM `clan` WHERE Team = '{TeamN}'")
                            await myDB1.commit()
                            capi = await cur1.fetchall()
                            for i in capi:
                                i = int(''.join(i))
                            capi = await client.fetch_user(i)
                            ASKembed = discord.Embed(
                                title=f'Joining Request', description=f"Do you want to accept?\n {person.mention}", colour=discord.Colour.blue())

                            pMSG = await discord.User.send(capi, embed=ASKembed)

                            await pMSG.add_reaction('🤝')
                            await pMSG.add_reaction('🚫')
                            embed = discord.Embed(
                                title=f'Joining Request Sent', description=f"Please wait for {capi.mention} Response")
                            await person.send(embed=embed)
                        else:
                            await person.send('Please try again and write the exact name')

            # elif str(react) == '⚔':
            #     await react.message.delete()
            #     async with myDB1.cursor() as cur1:
            #         await cur1.execute(f'SELECT  `Captin` FROM `clan`')
            #         await myDB1.commit()
            #         pLA = await cur1.fetchall()
            #         for i in pLA:
            #             if i== (f'{person.id}',):
            #                 mwjod = mwjod+1
            #             else:
            #                 pass

            #         await cur1.execute(f"SELECT `Captain` FROM `tournament`")
            #         await myDB1.commit()
            #         pLA = await cur1.fetchall()
            #         for i in pLA:
            #             i = ''.join(i)

            #         await cur1.execute(f"SELECT `Player` FROM `clan` WHERE '{person.id}' = Captin")
            #         await myDB1.commit()
            #         elcapi = await cur1.fetchall()
            #         for i in elcapi:
            #             i = ''.join(i)
            #             squadN = squadN + 1

            #         await cur1.execute(f"SELECT `Team` FROM `tournament`")
            #         await myDB1.commit()
            #         elcapi = await cur1.fetchall()
            #         for i in elcapi:
            #             i = ''.join(i)
            #             squadsN = squadsN + 1

            #         if i ==  (f'{person.id}',):
            #             await person.send('you are already in the tournament')

            #         else:
            #             if squadsN < 8:
            #                 if squadN > 4:
            #                     await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Captin = '{person.id}'")
            #                     await myDB1.commit()
            #                     pLA = await cur1.fetchall()
            #                     for i in pLA:
            #                         i = ''.join(i)
            #                     await cur1.execute(f"INSERT INTO `tournament`(`Team`, `Captain`, `stage`) VALUES ('{i}','{person.id}','1')")
            #                     await myDB1.commit()
            #                     await person.send('you have joined the tournament')
            #                 else:
            #                     await person.send("you need a full stack to join")
            #             else:
            #                 await person.send('Sorry, tournament is full')

            elif str(react) == '🤝':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Captin` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Captin = '{person.id}'")
                    await myDB1.commit()
                    Team = await cur1.fetchall()
                    for i in Team:
                        i = ''.join(i)
                    Team = i

                    if mwjod != 0:
                        player = react.message.embeds[0].description
                        player = player.split(" ")
                        Aplayer = player[-1].replace("<", "")
                        Aplayer = Aplayer.replace(">", "")
                        Aplayer = Aplayer.replace("@", "")
                        Aplayer = Aplayer.replace("!", "")
                        Aplayer = await client.fetch_user(Aplayer)
                        Aembed = discord.Embed(
                            title=f'Congratulations!!', description=f"Your now a member of {Team} clan")
                        await discord.User.send(Aplayer, embed=Aembed)
                        await cur1.execute(f"INSERT INTO `clan`(`Team`, `Player`, `Captin`) VALUES ('{Team}','{Aplayer.id}','{person.id}')")
                        await myDB1.commit()

            elif str(react) == '🚫':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Captin` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Captin = '{person.id}'")
                    await myDB1.commit()
                    Team = await cur1.fetchall()
                    for i in Team:
                        i = ''.join(i)
                    Team = i

                    if mwjod != 0:
                        player = react.message.embeds[0].description
                        player = player.split(" ")
                        Aplayer = player[-1].replace("<", "")
                        Aplayer = Aplayer.replace(">", "")
                        Aplayer = Aplayer.replace("@", "")
                        Aplayer = Aplayer.replace("!", "")
                        Aplayer = await client.fetch_user(Aplayer)
                        Aembed = discord.Embed(
                            title=f'Sorry!', description=f"You have been Rejected from {Team} clan")
                        await discord.User.send(Aplayer, embed=Aembed)

            elif str(react) == '🏛':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Player` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    if mwjod == 0:
                        await react.message.delete()
                        await person.send('Please type youre clan name')

                        def check(m):
                            return m.content and m.author.id != 725433666481946736 and m.author == person
                        msg = await client.wait_for('message', check=check)
                        TeamN = str(msg.content.upper().replace(' ', ''))
                        await cur1.execute(f'SELECT `Team` FROM `clan`')
                        await myDB1.commit()
                        Teamm = await cur1.fetchall()
                        for i in Teamm:
                            if i == (f'{TeamN}',):
                                Tmwjod = Tmwjod+1
                            else:
                                pass

                        if Tmwjod == 0:
                            await cur1.execute(f"INSERT INTO `clan`(`Team`, `Player`, `Captin`) VALUES ('{TeamN}','{person.id}','{person.id}')")
                            await myDB1.commit()
                            await person.send('You just created your team')
                        else:
                            await person.send(f'{TeamN} is taken, please try again')

            elif str(react) == '🚶‍♂️':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Player` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    if mwjod != 0:
                        await react.message.delete()
                        Pembed = discord.Embed(
                            title='Are you sure you want to leave the clan?', description=None, colour=discord.Colour.blue())
                        Pembed.add_field(name="✅", value=f"YES", inline=True)
                        Pembed.add_field(name="🛑", value=f"NO", inline=True)
                        PbotMSG = await person.send(embed=Pembed)
                        await PbotMSG.add_reaction('✅')
                        await PbotMSG.add_reaction('🛑')

            elif str(react) == '✅':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Player` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    if mwjod != 0:
                        await cur1.execute(f'DELETE FROM `clan` WHERE Player = {person.id}')
                        await myDB1.commit()
                        await react.message.delete()
                        await person.send('You just left your team')

            elif str(react) == '📄':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT `name` FROM `whatever` ')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    if mwjod != 0:
                        await person.send('please write your new Uplay name')

                        def check(m):
                            return m.content and m.author.id != 725433666481946736 and m.author == person
                        msg = await client.wait_for('message', check=check)
                        playerN = str(msg.content.upper().replace(' ', ''))
                        await cur1.execute(f"UPDATE `whatever` SET `uplay`='{playerN}' WHERE name = '{person.id}'")
                        await myDB1.commit()
                        Pembed = discord.Embed(title='Your Uplay name has been changed',
                                               description=f"New name: {playerN}", colour=discord.Colour.blue())
                        await person.send(embed=Pembed)

            elif str(react) == '🛑':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Player` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass
                    if mwjod != 0:
                        await react.message.delete()

            elif str(react) == '🏰':
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f'SELECT  `Player` FROM `clan`')
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    await cur1.execute(f"SELECT `Team` FROM `clan` WHERE Player = '{person.id}'")
                    await myDB1.commit()
                    Teamk = await cur1.fetchall()
                    for i in Teamk:
                        i = ''.join(i)

                    Teamk = ''.join(i)
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1
                        else:
                            pass

                    if mwjod != 0:
                        await react.message.delete()
                        await cur1.execute(f"SELECT `Player` FROM `clan` WHERE Team = '{Teamk}'")
                        await myDB1.commit()
                        Players = await cur1.fetchall()
                        alteam = []
                        for i in Players:
                            i = ''.join(i)
                            alteam.append(i)
                        count = 1
                        player_string = ""
                        for i in alteam:
                            player_string = f"{player_string}" + \
                                f"{count} - " + f"<@{i}>" + "\n"
                            count = count + 1
                        embed = discord.Embed(
                            title=f'Team Members', description=f"{player_string}", colour=discord.Colour.blue())
                        await person.send(embed=embed)

            elif str(react) == '🖊':
                await react.message.delete()
                async with myDB1.cursor() as cur1:
                    await cur1.execute(f"SELECT `name` FROM `whatever` WHERE name = '{person.id}'")
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1

                    if mwjod == 0:
                        embed = discord.Embed(
                            title=f'Register', description="Please type youre Uplay name:", colour=discord.Colour.blue())

                        def check(m):
                            return m.content and m.author.id != 725433666481946736 and m.author == person
                        await person.send(embed=embed)
                        msg = await client.wait_for('message', check=check)
                        playerN = str(msg.content.upper().replace(' ', ''))
                        await cur1.execute(f"SELECT `uplay` FROM `whatever`")
                        await myDB1.commit()
                        pLAs = await cur1.fetchall()
                        for i in pLAs:
                            if i == (f'{playerN}',):
                                mwjod = mwjod+1
                        if mwjod != 0:
                            await person.send('you already have been Registered')
                        else:
                            await cur1.execute(f"INSERT INTO `whatever`(`name`, `uplay`, `Platform`, `MMR`, `Games_Played`, `Games_won`, `Games_Lost`) VALUES ('{person.id}','{playerN}','pc',2500,0,0,0)")
                            await myDB1.commit()
                            embed = discord.Embed(
                                title=f'Congratulations!!', description=f"You have been Registered Successfully as {playerN}", colour=discord.Colour.red())
                            await person.send(embed=embed)

            elif str(react) == '🥾':
                async with myDB1.cursor() as cur1:
                    await react.message.delete()
                    await cur1.execute(f"SELECT `Captin` FROM `clan` WHERE Player = '{person.id}'")
                    await myDB1.commit()
                    pLA = await cur1.fetchall()
                    for i in pLA:
                        if i == (f'{person.id}',):
                            mwjod = mwjod+1

                    if mwjod != 0:
                        await cur1.execute(f"SELECT `Player` FROM `clan` WHERE Captin = '{person.id}'")
                        await myDB1.commit()
                        Players = await cur1.fetchall()
                        alteam = []
                        for i in Players:
                            i = ''.join(i)
                            if i == f'{person.id}':
                                pass
                            else:
                                alteam.append(i)
                        # count = 1
                        player_string = ""
                        for i in alteam:
                            player_string = f"{player_string}" + \
                                f"{i}  =>" + f"<@{i}>" + "\n"
                            # count  = count +1

                        embed = discord.Embed(
                            title=f'Which player?', description="Please write player's Number you want to kick \n" + f"{player_string}", colour=discord.Colour.red())
                        await person.send(embed=embed)

                        def check(m):
                            return m.content and m.author.id != 725433666481946736 and m.author == person
                        msg = await client.wait_for('message', check=check)
                        playerN = str(msg.content.upper().replace(' ', ''))
                        if playerN in alteam:
                            playerN = await client.fetch_user(playerN)
                            Aembed = discord.Embed(
                                title=f'Sorry!!', description=f"You have been kicked from {person.mention} team")
                            await discord.User.send(playerN, embed=Aembed)
                            await cur1.execute(f"DELETE FROM `clan` WHERE Player = '{playerN.id}'")
                            await myDB1.commit()
                            await person.send(f"{playerN.mention} got kicked")

                        else:
                            await person.send('Please try again and type the exact number')


@client.command(aliases=['INFO', 'Info'])
async def info(ctx):
    shbab = []
    mwjod = 0
    myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB.cursor() as cur:
        await cur.execute(f"SELECT `name` FROM `whatever`")
        await myDB.commit()
        up = await cur.fetchall()
        for i in up:
            i = ''.join(i)
            shbab.append(i)
        for i in shbab:
            if i == f'{ctx.author.id}':
                mwjod = 1

        if mwjod == 1:

            await cur.execute(f"SELECT uplay FROM `whatever` WHERE name = '{ctx.author.id}'")
            await myDB.commit()
            up = await cur.fetchall()
            for i in up:
                i = ''.join(i)
            await cur.execute(f"SELECT  `Platform` FROM `whatever` WHERE name = {ctx.author.id}")
            await myDB.commit()
            pl = await cur.fetchall()
            for a in pl:
                a = ''.join(a)
            await cur.execute(f"SELECT  `MMR` FROM `whatever` WHERE name = {ctx.author.id}")
            await myDB.commit()
            mmr = await cur.fetchall()
            for b in mmr:
                b = ''.join(b)
            await cur.execute(f"SELECT  `Games_Played` FROM `whatever` WHERE name = {ctx.author.id}")
            await myDB.commit()
            GP = await cur.fetchall()
            for c in GP:
                c = ''.join(c)
            await cur.execute(f"SELECT  `Games_won` FROM `whatever` WHERE name = {ctx.author.id}")
            await myDB.commit()
            GW = await cur.fetchall()
            for d in GW:
                d = ''.join(d)
            await cur.execute(f"SELECT  `Games_Lost` FROM `whatever` WHERE name = {ctx.author.id}")
            await myDB.commit()
            GL = await cur.fetchall()
            for e in GL:
                e = ''.join(e)

            istring = f'{i}' + "\n" + f'{a}\n' + \
                f'{b}\n' + f'{c}\n' + f'{d}\n' + f'{e}\n'
            string = "Uplay:\n Platform: \n MMR: \n Games Played: \n Games Won: \n Games Lost:"
            embed = discord.Embed(
                title=f"{i}'s Stats:", description=f"Known as:{ctx.author.mention}", colour=discord.Colour.red())
            embed.add_field(name=f"{string}", value='‎', inline=True)
            embed.add_field(name=f"{istring}", value='‎', inline=True)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="PA help", description=f"{ctx.author.mention} ,You need to register using .player ", colour=discord.Colour.red())
            await ctx.send(embed=embed)


@client.command(aliases=['Top', 'TOP'])
async def top(ctx):
    myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB.cursor() as cur:
        await cur.execute(f"SELECT `name` FROM `whatever` ORDER BY `whatever`.`MMR` DESC LIMIT 10")
        await myDB.commit()
        elshbab = []
        elshb = await cur.fetchall()
        for i in elshb:
            i = ''.join(i)
            elshbab.append(i)

        await cur.execute(f"SELECT `MMR` FROM `whatever` ORDER BY `whatever`.`MMR` DESC LIMIT 10")
        await myDB.commit()
        elmmrs = []
        elmmr = await cur.fetchall()
        for j in elmmr:
            j = ''.join(j)
            elmmrs.append(j)

        Tembed = discord.Embed(
            title='TOP 10', description=None, colour=discord.Colour.blue())
        Tcount = 1
        Tplayer = ""
        for i in elshbab:
            # elplayer = await client.fetch_user(i)
            Tplayer = f"{Tplayer}" + f"{Tcount} - " + f"<@{i}>" + "\n"
            Tcount = Tcount + 1

        Mplayer = ""
        for m in elmmrs:
            Mplayer = f"{Mplayer}" + f"{m}" + "\n"

        await verify(ctx)

        Tembed.add_field(name="PLAYERS ", value=f"{Tplayer}", inline=True)
        Tembed.add_field(name="MMR ", value=f"{Mplayer}", inline=True)
        await ctx.send(embed=Tembed)


@client.command()
@client.command(aliases=['CLAN', 'Clan', 'cLAN'])
async def clan(ctx):
    mwjod = 0
    # myDB = await aiomysql.connect(host='localhost',user='root',password='ayham123123',db='game id')
    myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB1.cursor() as cur1:
        await cur1.execute(f'SELECT  `Player` FROM `clan`')
        await myDB1.commit()
        pLA = await cur1.fetchall()
        for i in pLA:
            if i == (f'{ctx.author.id}',):
                mwjod = mwjod+1
            else:
                pass
        if mwjod == 0:
            Bembed = discord.Embed(
                title='CLAN WARS ⚔', description=None, colour=discord.Colour.blue())
            Bembed.add_field(name="🔎", value=f"Join A Team", inline=True)
            Bembed.add_field(name="l", value=f"l", inline=True)
            Bembed.add_field(name="🏛 ", value=f"Create A Team", inline=True)
            PbotMSG = await ctx.author.send(embed=Bembed)
            await PbotMSG.add_reaction('🔎')
            await PbotMSG.add_reaction('🏛')
        else:
            await cur1.execute(f'SELECT `Captin` FROM `clan`')
            await myDB1.commit()
            elcapi = await cur1.fetchall()
            elcaptins = []
            for i in elcapi:
                i = ''.join(i)
                elcaptins.append(i)

            if f'{ctx.author.id}' in elcaptins:
                Bembed = discord.Embed(
                    title='CLAN WARS ⚔', description=None, colour=discord.Colour.blue())
                Bembed.add_field(
                    name="🏰", value=f"Show Team Members", inline=True)
                Bembed.add_field(name="l", value=f"l", inline=True)
                Bembed.add_field(
                    name="🚶‍♂️ ", value=f"Leave Team", inline=True)
                Bembed.add_field(name="🥾", value=f"Kick Player", inline=True)
                Bembed.add_field(name="l", value=f"l", inline=True)
                Bembed.add_field(name="⚔", value=f"join the war", inline=True)
                PbotMSG = await ctx.author.send(embed=Bembed)
                await PbotMSG.add_reaction('🏰')
                await PbotMSG.add_reaction('�‍♂️')
                await PbotMSG.add_reaction('🥾')
                # await PbotMSG.add_reaction('⚔')

            else:
                Bembed = discord.Embed(
                    title='CLAN WARS ⚔', description=None, colour=discord.Colour.blue())
                Bembed.add_field(
                    name="🏰", value=f"Show Team Members", inline=True)
                Bembed.add_field(name="l", value=f"l", inline=True)
                Bembed.add_field(
                    name="🚶‍♂️ ", value=f"Leave Team", inline=True)
                PbotMSG = await ctx.author.send(embed=Bembed)
                await PbotMSG.add_reaction('🏰')
                await PbotMSG.add_reaction('🚶‍♂️')


@client.command(aliases=['POLL'])
async def poll(ctx):
    global war
    gamesstring = ''
    n = 0

    myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB1.cursor() as cur1:
        await cur1.execute(f"SELECT `Team` FROM `tournament`")
        await myDB1.commit()
        jwab = await cur1.fetchall()
        for i in jwab:
            i = ''.join(i)
            if i in war:
                pass
            else:
                war.append(i)

    while n < 4:
        n = n+1
        chosenT = random.choice(war)
        war1.append(chosenT)
        war.remove(chosenT)
        chosenT1 = random.choice(war)
        war1.append(chosenT1)
        war.remove(chosenT1)
        gamesstring = gamesstring + f"{chosenT} vs {chosenT1} \n"
        results = ctx.guild.get_channel(765984718713782272)
        botMSG4 = await results.send(f'Match : {chosenT} VS {chosenT1}')
        await botMSG4.add_reaction('🔶')
        await botMSG4.add_reaction('🔷')
        warch = ctx.guild.get_channel(765984718713782272)

    embed = discord.Embed(title="clan war started",
                          description='Quarter-finale', colour=discord.Colour.blue())
    embed.add_field(name=gamesstring, value='GOOD LUCK!', inline=True)
    await warch.send(embed=embed)


@client.command()
async def p(ctx):

    myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB1.cursor() as cur1:
        await cur1.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '2'")
        await myDB1.commit()
        jwab = await cur1.fetchall()
        for i in jwab:
            i = ''.join(i)
            war2.append(i)

    if len(war2) >= 2:
        chosenT = random.choice(war2)
        war2.remove(chosenT)
        chosenT1 = random.choice(war2)
        war2.remove(chosenT1)
        embed = discord.Embed(
            title="SEMI-FINALE", description=f'{chosenT} vs {chosenT1}', colour=discord.Colour.red())
        clanwarch = ctx.guild.get_channel(765984718713782272)
        await clanwarch.send(embed=embed)


@client.command()
async def show(ctx):

    global war
    war = []
    myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB1.cursor() as cur1:
        await cur1.execute(f"SELECT `Team` FROM `tournament` WHERE stage = '1'")
        await myDB1.commit()
        jwab = await cur1.fetchall()
        for i in jwab:
            i = ''.join(i)
            war.append(i)

    count = 1
    teamsstring = ''
    for i in war:
        teamsstring = teamsstring + f'{count}-' + f"{i}" + "\n"
        count = count + 1

    embed = discord.Embed(title="Clan WAR Teams:",
                          description=teamsstring, colour=discord.Colour.blue())
    await ctx.send(embed=embed)


@client.command()
async def teams(ctx):

    global war
    war = []
    myDB1 = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB1.cursor() as cur1:
        await cur1.execute(f"SELECT `Team` FROM `clan` ")
        await myDB1.commit()
        jwab = await cur1.fetchall()
        for i in jwab:
            i = ''.join(i)
            if i in war:
                pass
            else:
                war.append(i)

    count = 1
    teamsstring = ''
    for i in war:
        teamsstring = teamsstring + f'{count}-' + f"{i}" + "\n"
        count = count + 1

    embed = discord.Embed(
        title="Teams:", description=teamsstring, colour=discord.Colour.blue())
    await ctx.send(embed=embed)


async def verify(ctx):
    msg = ''
    myDB = await aiomysql.connect(host='localhost', user='root', password='ayham123123', db='test1')
    async with myDB.cursor() as cur:
        await cur.execute(f"SELECT `name` FROM `whatever` ORDER BY `whatever`.`MMR` DESC LIMIT 15")
        await myDB.commit()
        elshbab = []
        elshb = await cur.fetchall()
        for i in elshb:
            i = ''.join(i)
            elshbab.append(i)

    channel = ctx.guild.get_channel(836379205225938954)
    for i in elshbab:
        elplayer = await client.fetch_user(i)
        msg = msg + elplayer.mention + ' '
    await channel.send(msg)

token = 'NzI1NDMzNjY2NDgxOTQ2NzM2.XvOqvw.YoeFIQ-B2L8vz-iedcMkko5-baQ'
client.run(token)
