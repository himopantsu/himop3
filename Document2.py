import discord
import glob
from discord.ext import commands,tasks
import gspread
import random 
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
import datetime
import os
import urllib.request, urllib.error
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from datetime import timedelta
import cv2
import io
from PIL import Image

bot_token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
	"""起動時に通知してくれる処理"""
	print('ログインしました')
	print(client.user.name)  # ボットの名前
	print(client.user.id)  # ボットのID
	print(discord.__version__)  # discord.pyのバージョン
	print('------')

@client.event
async def on_member_join(member):
	dm = await member.create_dm()
	await dm.send(f"{member.mention}さんゲーム参加ありがとう！ゲームの説明をするね\nどうやらこの地図に描いてある島のどこかに宝が隠されているようなんだ。\n")
	await dm.send(file=discord.File("map1.png"))
	await dm.send(f"これがその地図。\n今いる場所がちょうど赤い点のあるD-8だよ。\nこの町の長老にこの地図について知っているか聞いたんだ\nそうしたら「まずはこの謎を解いてみろ」って言われたんだけど・・・・")
	await dm.send(f"正直全然わからなくて････。")
	await dm.send(file=discord.File("nazo1.png"))
	await dm.send(f"もしも解けたら答えを教えてほしい！。あ、解答するときはカタカナにして解答の前に[!]を付けてね")
	await dm.send(f"(例:解答が「メイプルキノコ」の場合「!メイプルキノコ」と発言してください。")
	await dm.send(f"!は半角ね")

@client.event
async def on_message(message):
	"""メッセージを処理"""
	if message.author.bot:  # ボットのメッセージをハネる
		return
	
	elif message.attachments:
		headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}
		request = urllib.request.Request(url=str(message.attachments[0].url),headers=headers)
		f = io.BytesIO(urllib.request.urlopen(request).read())
		validation_img = Image.open("horntale_necklace.png")
		validation_grayimg = validation_img.convert('L')
		validation_array = np.asarray(validation_grayimg)
		img = Image.open(f)
		grayimg = img.convert('L')
		input_array = np.asarray(grayimg)
		custom_cascade = cv2.CascadeClassifier('cascade.xml')
		custom_rect = custom_cascade.detectMultiScale(grayimg, scaleFactor=1.07, minNeighbors=2, minSize=(1, 1))
		if len(custom_rect) == 0:
			return
		else: await message.channel.send(f"あるよ")
	
	elif message.content == "!やるじゃん":
		await message.channel.send(f"ありがとう")

	elif message.content == "!やってないじゃん":
		await message.channel.send(f"ごめんなさい")
		
	elif message.content == "!ゆきやこんこ":
		await message.channel.send(f"⛄雪や⛄\n\n❄❅❆❄❅❆❄❅❆❄\n▉▉▉ ◥◣　　 ▉▉▉ \n　　▉ 　　◢◤ 　　▉ \n▉▉▉ ◢▉◤　 ▉▉▉ \n❄❅❆❄❅❆❄❅❆❄\n\n🚽ケツから🚽\n\n💩💩💩💩💩💩💩💩\n　▉\n▉▉▉▉◥◣　　▉▉▉\n▉　◢◤　　◢◤　　▉\n　◢◤　◢▉◤　▉▉▉\n💩💩💩💩💩💩💩💩")
		
	elif message.content == "!ホーンテイル":
		dm = await message.author.create_dm()
		await dm.send(f"そうか！ホーンテイルか！\n長老、答えはホーンテイルだ！")
		await dm.send(f"長老「答えは合っている。だが、この町では大人しくしといたほうが身のためだぞ！")
		await dm.send(f"長老「次の街の手がかりを教える。この町へ向かい、情報屋を訪ねるんだ」")
		await dm.send(file=discord.File("map2.png"))
		await dm.send(f"どうやら次はD-11の町へ向かえば良いんだね")
		await dm.send(f"=====D-11移動中=====")
		await dm.send(f"というわけで町について情報屋を見つけたよ！")
		await dm.send(f"どうやら情報屋も手掛かりを教えてくれるらしい\nただし、この謎を解けたらだけど・・・・")
		await dm.send(file=discord.File("nazo2.png"))
	
	elif message.content == "!サメ":
		dm = await message.author.create_dm()
		await dm.send(f"答えはサメだ！\nまったく、癪に障る問題だね")
		await dm.send(f"情報屋「よく解けましたね、次はこの街へ向かい、アイテム制作屋を訪ねなさい」")
		await dm.send(file=discord.File("map3.png"))
		await dm.send(f"よし！この調子で進もう！")
		await dm.send(f"=====F-11移動中=====")
		await dm.send(f"制作屋「
		
		

client.run(bot_token)
