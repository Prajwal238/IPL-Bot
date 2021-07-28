import discord
import random
from discord.ext import commands
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print("IPL Bot is online")


@client.command()
async def fixture(ctx):
    
    await ctx.send('https://cricketaddictor.com/wp-content/uploads/2021/09/IPL-2021-schedule-1-scaled.jpg')


@client.command()
async def srh(ctx):
    taglines = ['Go Go Go Orange Army!', 'Rise up to every challenge']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def csk(ctx):
    taglines = ['Chennai Super Kingsku Whistle Podu', 'Raise Your Hands', 'Yellove Again', 'AnbuDen']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def rr(ctx):
    taglines = ['HAALLAAAA BOOOLLLL']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def rcb(ctx):
    taglines =  ['Just Play Bold Royal Challengers!', 'Jeetenge hum shaan se', 'We are the best forget the rest', 'Game for More']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def mi(ctx):
    taglines = ['Amachi Mumbai', 'Cricket meri jaan', 'Duniya hila denge']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def kxip(ctx):
    taglines = ['Live Punjabi Play Punjabi', 'Sadda Punjab', 'Sadda squad']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def kkr(ctx):
    taglines = ['KKR hai Tayarr', 'Korbo,Lorbo,Jeetbo Re', 'Ami KKR']
    await ctx.send(taglines[random.randrange(len(taglines))])
@client.command()
async def dd(ctx):
    taglines = ['Khelo front foot pe', 'Munday Dilli Ke', 'Dhuandaar Dilli', 'This is New Delhi']
    await ctx.send(taglines[random.randrange(len(taglines))])

@client.command()
async def score(ctx):
    url5 = 'https://www.espncricinfo.com/scores'
    page = requests.get(url5)
    soup = BeautifulSoup(page.text, 'html.parser')

    bat_team = soup.find_all(class_='name')
    runs = soup.find_all(class_ = 'score')
    overs = soup.find(class_ = 'extra-score').getText()
    
    bat_team_list = [item.text for item in bat_team]
    bat_team_2_final = bat_team_list[1]
    bat_team_1_final = bat_team_list[0]


    runs_list = [item.text for item in runs]
    runs_2_final = runs_list[1]
    runs_1_final = runs_list[0]

    scorecard = bat_team_1_final + ": " + "\n" + runs_1_final + " \n \n" + overs +"\n \n" + bat_team_2_final +":"+ "\n" + runs_2_final
    await ctx.send(scorecard)


@client.command()
async def pos(ctx):

    url = 'https://www.espncricinfo.com/table/series/8048/season/2021/indian-premier-league'


    page=requests.get(url)  
    soup = BeautifulSoup(page.text, 'html.parser')

    names = soup.find_all('h5')
    points = soup.find_all(class_='border-right label')

    teams = [item.text for item in names]
    del teams[0]
    del teams[-1]

    stands = [item for item in range(1,9)]
    spaces = '      '

    pts = [p.text for p in points]

    table = {'S.NO':stands,' ':spaces,
            'TEAM': teams,'  ':spaces,
            'PTS': pts  }
    df = pd.DataFrame(table, columns = ['S.NO',' ',' ','TEAM',' ',' ', 'PTS'], index = ['Q','Q','Q','Q',' ',' ',' ',' '])
    await ctx.send(df)

@client.command()
async def orgcap(ctx):

    url2 = 'https://www.iplt20.com/stats/2021/most-runs'

    page_2 = requests.get(url2)
    soup2 = BeautifulSoup(page_2.text,'html.parser')

    stands2 = [item for item in range(1,6)]
    spaces = '      '

    most_runs = soup2.find_all(class_= 'top-players__last-name')


    orange_cap_final = []
    orange_cap =[player.text for player in most_runs]

    for i in range(5):
        orange_cap_final.append(orange_cap[i])

    orangecap = {'POS':stands2,' ':spaces, 'PLAYER': orange_cap_final}
    df2 = pd.DataFrame(orangecap, columns = ['POS', ' ','PLAYER'], index = ['','','','',''] )

    await ctx.send(df2)

@client.command()
async def prpcap(ctx):

    url3 = 'https://www.iplt20.com/stats/2021/most-wickets'

    page_3 = requests.get(url3)
    soup3 = BeautifulSoup(page_3.text,'html.parser')

    stands2 = [item for item in range(1,6)]
    spaces = '      '

    most_wickets = soup3.find_all(class_= 'top-players__last-name')

    purple_cap_final = []
    purple_cap =[player.text for player in most_wickets]

    for i in range(5):
        purple_cap_final.append(purple_cap[i])

    purplecap = {'POS':stands2,' ':spaces, 'PLAYER': purple_cap_final}
    df3 = pd.DataFrame(purplecap, columns = ['POS', ' ','PLAYER'], index = ['','','','',''] )

    await ctx.send(df3)

@client.command()
async def most6(ctx):

    url4 = 'https://www.iplt20.com/stats/2021/most-sixes'

    page_4 = requests.get(url4)
    soup4 = BeautifulSoup(page_4.text, 'html.parser')
    sixes = soup4.find_all(class_='top-players__last-name')
    most_sixes_final = []
    spaces = '      '

    stands2 = [item for item in range(1,6)]
    most_sixes =[player.text for player in sixes]
        
    for i in range(5):
        most_sixes_final.append(most_sixes[i])

    noofsixes = {'POS':stands2,' ':spaces,'PLAYER': most_sixes_final}
    df4 = pd.DataFrame(noofsixes, columns = ['POS', ' ', 'PLAYER'], index = ['','','','',''] )

    await ctx.send(df4)

@client.event
async def on_message(message):
    if message.content.startswith('help'):
        embedVar = discord.Embed(title="IPLBot", description="Commands: \n 1. -fixture: To see the schedule of IPL2021 \n 2. -pos: To see the points table \n 3. -orgcap: To know leading run scorer \n 4. -prpcap: To know leading wicket taker \n 5. -{team name}: To get a tagline of the team \n 6. -score: To get the scorecard\n Hope you enjoy this IPL2021 \n 7. -most6: To know who hit more 6's", color=0x00CED1)
        await message.channel.send(embed=embedVar)
    await client.process_commands(message)
      

#Uncomment the below command:
#client.run('Put your bot ID here')