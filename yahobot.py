from msilib.schema import MsiAssembly
import discord
import asyncio
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #봇이 실행되면 콘솔창에 표시

@client.event
async def on_message(message):
    message_content = message.content
    qad = message_content.find("여캠")
    if qad >=0:
        await message.channel.send('별풍선 충전하러 가야겠다')
    message_content = message.content
    wad = message_content.find("혜린")
    if wad >=0:
        await message.channel.send('꾸에엑')
    message_content = message.content
    ead = message_content.find("민서")
    if ead >=0:
        await message.channel.send('어떤 민서??')
    message_content = message.content
    rad = message_content.find("시현")
    if rad >=0:
        await message.channel.send('무슨 시현??')
    message_content = message.content
    tad = message_content.find("재호")
    if tad >=0:
        await message.channel.send('야호')
    message_content = message.content
    yad = message_content.find("현기")
    if yad >=0:
        await message.channel.send('응애')
    message_content = message.content
    uad = message_content.find("용준")
    if uad >=0:
        await message.channel.send('썅')
    message_content = message.content
    iad = message_content.find("정호")
    if iad >=0:
        await message.channel.send('꺼져')
    message_content = message.content
    iad = message_content.find("민영")
    if iad >=0:
        await message.channel.send('지혜와 함께')
    message_content = message.content
    oad = message_content.find("성진")
    if oad >=0:
        await message.channel.send('그냥 불러봤어')
    message_content = message.content
    pad = message_content.find("민규")
    if pad >=0:
        await message.channel.send('저런')
    message_content = message.content
    aad = message_content.find("가은")
    if aad >=0:
        await message.channel.send('피자먹으러 와')
    message_content = message.content
    sad = message_content.find("주영")
    if sad >=0:
        await message.channel.send('(짝꿍)')
    dad = message_content.find("지혜")
    if dad >=0:
        await message.channel.send('끼룩끼룩')
    message_content = message.content
    fad = message_content.find("끄투")
    if fad >=0:
        await message.channel.send('https://kkutu.co.kr/')
    message_content = message.content
    gad = message_content.find("갈틱폰")
    if gad >=0:
        await message.channel.send('https://garticphone.com/ko')
    message_content = message.content
    kad = message_content.find("애들아")
    if kad >=0:
        await message.channel.send('@everyone ')
    message_content = message.content
    bad = message_content.find("씨발")
    if bad >= 0:
        await message.delete()
    if message.content.startswith("!먹어치워 "):
        purge_number = message.content.replace("!먹어치워 ", "")
        check_purge_number = purge_number.isdigit()
        if check_purge_number == True:
            await message.channel.purge(limit=int(purge_number) + 1)
            msg = await message.channel.send(f"옴냠냠")
            await asyncio.sleep(5)
            await msg.delete()
        else:
            await message.channel.send("올바른 값을 입력해주세요.")
client.run(os.environ['token'])