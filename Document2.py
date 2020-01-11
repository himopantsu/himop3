import discord
import glob
from discord.ext import commands,tasks
import gspread
import random  # おみくじで使用
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
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんゲーム参加ありがとう！ゲームの説明をするね\nどうやらこの島のどこかに宝が隠されているようなんだ。\n")
	
@client.event
async def on_message(message):
	"""メッセージを処理"""
	if message.author.bot:  # ボットのメッセージをハネる
		return
	
	elif message.content == "!参加":
	# チャンネルへメッセージを送信
		cell_1,cell_2,count = set_cell(message.author.id)
		if cell_2 == 0:
			await message.channel.send(f"{message.author.mention}さん シートにIDがありません")  # f文字列（フォーマット済み文字列リテラル）
			
		else:
			worksheet.update_cell(cell_2,cell_1,"〇")
			await message.channel.send(f"{message.author.mention}さん 参加確認しました\n今シーズンの参加回数は累計{count}回です")  # f文字列（フォーマット済み文字列リテラル）

	elif message.content == "!星空":
		if message.author.id == 573911598008107009:
			cell_1,cell_2,count = set_cell(506660639964659768)
			if cell_2 == 0:
				await message.channel.send(f"星空さん シートにIDがありません")  # f文字列（フォーマット済み文字列リテラル）
			else:
				worksheet.update_cell(cell_2,cell_1,"〇")
				await message.channel.send(f"星空さん 参加確認しました\n今シーズンの参加回数は累計{count}回です")  # f文字列（フォーマット済み文字列リテラル）
		else:await message.channel.send(f"それはニートちゃんしか使えないよ")
	
	elif message.content == "!きゃすん":
		embed = discord.Embed(title="個通相手募集～", description=f"{message.author.mention}さんが個通相手を募集しています！",color=0xFF6EC7)
		embed.set_thumbnail(url=message.author.avatar_url)
		await message.channel.send(embed=embed)
	
	elif message.content == "!ビビデバビデブー":
		if message.author.id == 303215008802930699:
			day = datetime.date.today() + timedelta(days=(7-datetime.date.today().weekday()))
			youbi = np.array(["月","火","水","木","金","土","日","月","火","水","木","金","土","日"])
			await message.channel.send(f"@everyone 来シーズンの出欠席\nチェックお願いします")
			await message.channel.send(f"日付の下の:relaxed::o::x::question:を押して貰えれば\nチェック完了です:ok_hand::skin-tone-1::sparkles:")
			await message.channel.send(f":relaxed: ▷優先的に参加にします\n:o:▷参加可能の日\n:x:▷参加不可の日\n:question:▷どちらか未定の日")
			await message.channel.send(f":o:の人が20人いない場合は:question:の人も呼び出す事があるので出られない場合は無理せず")
			await message.channel.send(f"#要塞戦出席表 に出れないと書いて貰えれば待機してくれる人がいるので、お願いします🤲")
			await message.channel.send(f"ちなみに、このシステムはほぼ手動なので後から:x:に変更しても気付かない場合があるのでその場合も\n #要塞戦出席表 に書いてもらえると助かります:strawberry:")
			await message.channel.send(f"全部❌でも怒られないので")
			await message.channel.send(f"リアクションおしてくれると助かります:macs: ")
			await message.channel.send(f"残りの今シーズンも頑張りましょう:daynogal:")
			for i in range(14):
				q = await message.channel.send(f"{(day+timedelta(days=i)).month}/{(day+timedelta(days=i)).day}({youbi[i]})")
				[await q.add_reaction(i) for i in ('😊','⭕','❌','❓')]

		else:await message.channel.send(f"それはまあこしか使えないよ")
		
	elif message.content == "!やるじゃん":
		await message.channel.send(f"ありがとう")
		
	elif message.content == "!Esprit":
		await message.channel.send(f"抜けたほうがいいですよ")
		
	elif message.content == "!えっち":
		await message.channel.send(f'きゃー！{message.author.mention}さんのえっち！！', file=discord.File("4ba65a1c.jpg"))
		
	elif message.content == "!くるみ":
		await message.channel.send(f'zeulon、私たちはもう終わりよ', file=discord.File("kurumi.png"))
		
	elif message.content == "!ドッグラン":
		await message.channel.send(file=discord.File("dogrun.jpg"))
		
	elif message.content == "!ヘリコプター":
		await message.channel.send(file=discord.File("herineet.png"))

	elif message.content == "!まあこ":
		await message.channel.send(f"寝てるよ")
		
	elif message.content == "!ハンバーグ":
		await message.channel.send(f"ハンバアアアアアアアアアアアアアアアアアアアアアアアアアアアグ！！！！！！")
	
	elif message.content == "!やってないじゃん":
		await message.channel.send(f"ごめんなさい")
		
	elif message.content == "!ゆきやこんこ":
		await message.channel.send(f"⛄雪や⛄\n\n❄❅❆❄❅❆❄❅❆❄\n▉▉▉ ◥◣　　 ▉▉▉ \n　　▉ 　　◢◤ 　　▉ \n▉▉▉ ◢▉◤　 ▉▉▉ \n❄❅❆❄❅❆❄❅❆❄\n\n🚽ケツから🚽\n\n💩💩💩💩💩💩💩💩\n　▉\n▉▉▉▉◥◣　　▉▉▉\n▉　◢◤　　◢◤　　▉\n　◢◤　◢▉◤　▉▉▉\n💩💩💩💩💩💩💩💩")
	elif message.content == "juruli":
		await message.channel.send(f"そのキャラはキャラデリしました")
		
	elif message.content == "!ままん":
		await message.channel.send(f"ままぁ\nあああん\nあああああん\nままああああ\nああん\nあああああああああああああああああああああああああああああああああああああああああああ\nあああああああああああああああああああああああああああｂｂ")
		
	elif message.content == "!にーと":
		await message.channel.send(f"にーとくさい")	
		
	elif message.content == "!マルガリタ":
		await message.channel.send(f"抜けませんでした")
	
	elif message.content == "!かてぽん":
		await message.channel.send(f"ブルブルブルブルアイ！:v:(՞ਊ՞:v:三:v:՞ਊ՞):v:アイ！:v:(՞ਊ՞:v:三:v:՞ਊ՞):v:ブ・ル・ベ・リ・アイ！！:v:(՞ਊ՞:v:三:v:՞ਊ՞):v:ブルブルブルブルアイ！:v:(՞ਊ՞:v:三:v:՞ਊ՞):v:アイ！:v:(՞ਊ՞:v:三:v:՞ਊ՞):v:ブ・ル・ベ・リ・アイ！！:v:(՞ਊ՞:v:三:v:՞ਊ՞):v:")
	
	
	elif message.content == "!投票":
	# リアクションアイコンを付けたい
		msg = await message.channel.send("あなたは右利きですか？")
		[await msg.add_reaction(i) for i in ('⭕')]  # for文の内包表記

	elif message.content == "!おみくじ":
		# Embedを使ったメッセージ送信 と ランダムで要素を選択
		embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",color=0x2ECC69)
		embed.set_thumbnail(url=message.author.avatar_url)
		embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
		await message.channel.send(embed=embed)
client.run(bot_token)
