import discord
from discord.ext import commands
import datetime
import os
import asyncio
from itertools import cycle

client = discord.Client()

#client config

status = ["WolHa_Radio | WolHa", "By ArdanKR_#3402"]
radio = ['584372821195620354', '543428999418871828']
mention = ["message.author.name + '#' + message.author.discriminator"]

    # 543428999418871828 = ArdanKR_#3402 , 584372821195620354 = 시나KR#9741

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status, type=1, url='https://www.twitch.com/ardankjr'))
        await asyncio.sleep(5)

# client commands

@client.event
async def on_message(message):
    if message.content.startswith('+start_radio'):
        if message.author.id in radio:
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0x6184ff)

            embed.set_author(name=message.author.name + '#' + message.author.discriminator)
            embed.add_field(name=':red_circle: Live **월하_라디오 시작 알림**', value='라디오가 시작됩니다. 청취자 여러분들은 채널을 <#623174984474558464>로 맞춰주시기 바랍니다.', inline=False)
            embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, "<@&623505873519509504>", embed=embed)

    if message.content.startswith('+stop_radio'):
        if message.author.id in radio:
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0x6184ff)

            embed.set_author(name=message.author.name + '#' + message.author.discriminator)
            embed.add_field(name=':red_circle: Live **월하_라디오 방송 종료 알림**', value='라디오 방송이 종료됩니다. 청취해주셔서 감사합니다.', inline=False)
            embed.set_footer(text='Requested by • ' + message.author.name + '#' + message.author.discriminator, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, "<@&623518005648949257>", embed=embed)


client.loop.create_task(change_status())
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
