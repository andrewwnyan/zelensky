import discord
from discord.ext import commands
import requests
import random
import re
# libs

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='%', intents=intents)
token = 'Put there your token!'

# for reactions command(it's pretty broken tho)
reactions1 = '1️⃣'
reactions2 = '2️⃣'
reactions3 = '3️⃣'
reactions4 = '4️⃣'
reactionsY = '✅'
reactionsN = '❌'

badwords = ["блять", "бля", "хуй", "пизда", "пиздец" , "хуесос" , "пидор" , "сука"]
breakevery = ["l.daily", "l.d", "l.work", "l.w", "l.s", "l.sell" , "cc.ban" , ".tr" , ".avatar"]
votkomy = ["linux" , "линукс" , "Linux" , "Линукс" , "линь" , "убунту" , "минт" , "арч" , "федора" , "линус" , "gnome" , "кде" ,]
chipichipi = ["чипи " , "чапа " , "chipi " , "chapa "]
# word trigger , maybe i will improve this(NO LOL)

@bot.event # for cooldowns
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"`Повтори команду через {round(error.retry_after, 2)} секунд!`" , delete_after=5)

@bot.command() # AI based using llama ai
@commands.cooldown(1, 45, commands.BucketType.user)
async def ai(ctx, *, prompt):
	async with ctx.typing(): 
		await ctx.reply("**Ответ генерируется.. Подождите пожалуйста. Если ответа не было то бот сдох xdd**", delete_after=10)
		URL = "https://www.llama2.ai/api"
		resp = requests.post(URL, json={"prompt":f"<s>[INST]{prompt}[/INST]</s>", "model":"meta/llama-2-7b-chat", "temperature":0.75, "topP":0.9, "maxTokens":1650, "image":None, "audio":None})
		if(len(resp.text) > 2000):
			for i in range(0, len(resp.text), 2000):
				await ctx.reply(f"Сгенерированный текст:```\n {resp.text}``` \n **Ответы могут быть неправильными или иметь ошибки.**")	
		else:
			await ctx.reply(f"Сгенерированный текст: ```\n {resp.text}``` \n **Ответы могут быть неправильными или иметь ошибки.**")

@bot.event
async def on_ready():
	guild_count = 0
	guild_c = 0


	for guild in bot.guilds:
		print(f"- {guild.id} (ПИДОРАШСКИЕ СЕРВЕРА: {guild.name})")

		guild_count = guild_count + 1

	print("ПИЗДОБЛЯДСКИЙ БОТ ОККУПИРОВАН ЭТИ СЕРВЕРА " + str(guild_count) + " guilds.") # server counter
	await bot.change_presence(activity=discord.Streaming(name="топ 5 грустных гвоздей", url="https://www.youtube.com/watch?v=xuicAMyeP3k"))

@bot.command(name="say")
async def say(ctx, *, text):
    await ctx.send(f"{text}")

@bot.command(name="emoji")
async def emoji(ctx, emoji: discord.Emoji):
    embed=discord.Embed(title=f"**Эмодзи : {emoji.name}**")
    embed.set_thumbnail(url=f"{emoji.url}")
    embed.add_field(name="URL", value=f"{emoji.url}", inline=False)
    await ctx.send(embed=embed)
    
@bot.command(name="хелп")
async def хелп(ctx):
    embed=discord.Embed(title="Доступные команды", description="`%say` - **Бот пишет фразу** \n `%ai` - **И.И запросы(или как назвать хз). Работает хуёво , не используйте** \n `%межсервер` - **Бот передаёт сообщение между серверами** \n 📰 - **Создаётся ветка для обсуждения**(только для доверенных людей , и добавлять вначале сообщения) \n 2️⃣3️⃣4️⃣ - **Ставит реакцию** (только для доверенных людей ) \n ❓ - **Создаёт голосование**(✅ ❌ , ставить вначале сообщения и только для доверенных людей) \n \n БОТ ПЕРЕСТАНЕТ РАБОТАТЬ <t:1710665700:R> `Бот создан @phibiiscool__.`", color=0xe8ccff)
    embed.set_author(name="Зеленский", icon_url="https://cdn.discordapp.com/attachments/905721004704296970/1207260782815875092/fd7a723bdeba999ba0f0a05277ee9422.png?ex=65df0038&is=65cc8b38&hm=93042d8bb33836fa9876ee78508d2cd3c90cca2093b50c4abb2fd79a34014dad&")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/905721004704296970/1207260782815875092/fd7a723bdeba999ba0f0a05277ee9422.png?ex=65df0038&is=65cc8b38&hm=93042d8bb33836fa9876ee78508d2cd3c90cca2093b50c4abb2fd79a34014dad&")
    await ctx.send(embed=embed) # help command

@bot.command(name="anonsay")
async def anonsay(ctx, *, text):
	author = ctx.author
	if author == "518376913568268": # oh , this is my discord id =D
		channel = bot.get_channel(channelidx1)
		await channel.send(f"{text}")
	else:
		await ctx.send("ты че ебнутый у тебя прав нету лалка")

@bot.event
async def on_message(message):
	author = message.author
	randmnumber = random.randint(0, 5)
	randmeme = "https://tenor.com/view/%D0%B0-4-gif-14211769093273171637" , "https://media.discordapp.net/attachments/749768163968811081/1171875655651184701/speed.gif" , "https://tenor.com/view/sad-cat-gif-26067066" , "https://tenor.com/view/cat-berg-cat-orange-cat-swimming-gif-25177582" , "https://tenor.com/view/cat-kitty-pussycat-feline-gif-26001328" , "https://tenor.com/view/oneshot-spin-gif-8295119798900423556"
	if message.content.startswith("б "):
		await message.channel.send("__**БУБУН ЁБАНЫЙ ЧО НАДО? САМЫЙ УМНЫЙ ТУТ??? РЕАКЦИИ МОИ ЧЕКАТЬ РЕШИЛ!**__")	
	elif re.findall("зеленый", message.content):
		await message.channel.send("**СЛЫШЬ?? КОГО ТЫ ЗЕЛЕНЫМ НАЗВАЛ?**")	
	elif re.findall("зелёный", message.content):
		await message.channel.send("**СЛЫШЬ?? КОГО ТЫ ЗЕЛЁНЫМ НАЗВАЛ?**")	
	elif re.findall("лох", message.content):
		await message.channel.send("**ТЫ ЛOХ, ЯСНО???**")
	elif re.findall("ЛОХ", message.content):
		await message.channel.send("**ТЫ ЛOХ, ЯСНО???**")
	elif re.findall("чо", message.content):
		await message.channel.send("**НИЧО!**")
	elif message.content == "да":
		await message.channel.send("**Нет**")
	elif message.content == "ДА":
		await message.channel.send("**Нет**")
	elif any(word in message.content for word in votkomy):
		await message.channel.send("https://cdn.discordapp.com/attachments/1199215458973401111/1204717909906165770/animation.gif.gif?ex=65d5bffc&is=65c34afc&hm=03020ea8998dc24db9f0f32fd9dc9e7d6e1eee3635135bee59276204dbe03d66&")
	elif any(word in message.content for word in chipichipi):
		await message.channel.send("https://cdn.discordapp.com/attachments/1199215458973401111/1204717862002888754/chipi-chapa.gif?ex=65d5bff0&is=65c34af0&hm=b9a2d7cd568142284409b94c42773ca05f83e48ae3da8cb84c86a9960b696387&")
	elif message.content == "просто":
		await message.channel.send("**СЛОЖНА БЛЯТЬ СЛОЖНА!!! КАКОЙ НАХУ ПРОСТА?!??!?!?!**")
	elif message.content == "Z":
		await message.channel.send("https://tenor.com/view/letter-z-gif-14286599")
	elif any(word in message.content for word in badwords):
		await message.channel.send("**ТЫ ЧO МАТЕРИШЬСЯ?! СОВСЕМ СТРАХ ПОТЕРЯЛ?**")
	elif any(word in message.content for word in breakevery):
		await message.channel.send(tisho1)
	elif message.content == "🥚":
		await message.channel.send(f"__**ААА ПАМАГИТЕ!!!! ТУПОЙ {author.mention} СОВСЕМ СТРАХ ПОТЕРЯЛ!!!!!! ПАМАГИИИИТЕЕЕЕЕЕ**__")
	elif message.content == "скажи число ёпта":
		sexynumber = random.randint(100, 1200000000)
		await message.channel.send(f"**ДЕРЖИ СВОЁ ЧИСЛО ЁПТА {sexynumber} , А ТЕПЕРЬ** <:idinaxui:1192194365519581334>")
	elif re.findall("бан", message.content):	
		await message.channel.send("**СЛЫШ! ЩАС ТИБЯ ЗАБАНИМ ТУТ ПОНЕЛ?!**")
	elif re.findall("ban", message.content):	
		await message.channel.send("**СЛЫШ! ЩАС ТИБЯ ЗАБАНИМ ТУТ ПОНЕЛ?!**")		
	elif re.findall("класс", message.content):	
		await message.channel.send("**ТЫ В 1 КЛАССЕ ЯСНА**")
	elif re.findall("пон ", message.content):	
		await message.channel.send("https://cdn.discordapp.com/attachments/1199215458973401111/1204714098332540938/IMG_2484.MP4?ex=65d5bc6f&is=65c3476f&hm=cf8be1706b6e1ab70a3d1d9311d4f8303a5ef05b069b3ee9fdecb37bf89ff137&")
	elif re.findall("___", message.content):	
		await message.channel.send("**ЧО ЛЯКАЕШЬ?! ПОЕХАВШЫЙ ШТОЛИ?!??!?!?! ИДИОТ МОЛЧИ**")
	elif re.findall("хохол", message.content):	
		await message.channel.send(f"**ЧО , {author.mention} , ВАЩЕ ПАЕХАВШЫЙ ШТОЛЕ?!?!?! ПАШОЛ АТСЮДА! ТЕБЕ ТУД НИ РАДЫ!!!**")		
	elif re.findall("666", message.content):	
		await message.channel.send(f"**ААААА БЛЕАТЬ!!!! СУПИРПРИЗ ВЫБИЛ ДА , СКОТИНА??? {author.mention} **")
	elif message.content == "<@1192171792048070678>":
		if message.author != "1192171792048070678":			
			await message.channel.send(f"**__Э ТЫ ЧО , {author.mention} АФИГЕЛ??? ЩА САЛОМ КИДАЦА БУДУ!!!__**")
	elif message.content == "г":
		await message.channel.send("**__ГОВНО СТАРОЕ! МОЛЧИ В УГОЛОЧКЕ ЕБЛАН ТЫ ТУПОЙ! РЕАКЦИИ ПРОДОЛЖАЕШЬ МОИ ИСКАТЬ???!__**")
	elif re.findall("ыыы", message.content):	
		await message.channel.send("**ЫЫЫЫЫ**")		
	elif message.content == ".кица":
		await message.channel.send(randmeme[randmnumber])
	elif message.content == "бля скажи какая ава у этого чела":
		user = message.author
		avatar_url = user.avatar_url
		await message.channel.send(avatar_url)
	elif message.content == "бля скажи какие авы у этого чела":
		user = client.get_user(user_id)
		user_id = 104841305872218 # Изначально я хотел сделать Зеленского чтобы пиздить аватарки но... да. 
		avatar_url = user.avatar_url
		await message.channel.send(avatar_url)
	elif message.content == "магик":
		await message.channel.send("сперма" , reference=message)
	elif re.findall("📰", message.content):
		if author.id in [518376913568268288 , 1133688785847205970 , 1087336787317370931]:
			await message.create_thread(name="📰 Обсуждение", auto_archive_duration=60)
		else:
			print("some dumbass trying make a thread bruh")

### VOTE MESSAGE (MESSY ASF)
	elif message.content.startswith("2️⃣"):
		if author.id in [518376913568268288 , 1133688785847205970 , 1087336787317370931]:
					await message.add_reaction(reactions1)
					await message.add_reaction(reactions2)
	elif message.content.startswith("3️⃣"):
		if author.id in [518376913568268288 , 1133688785847205970 , 1087336787317370931]:
					await message.add_reaction(reactions1)
					await message.add_reaction(reactions2)
					await message.add_reaction(reactions3)
	elif message.content.startswith("4️⃣"):
		if author.id in [518376913568268288 , 1133688785847205970 , 1087336787317370931]:
			await message.add_reaction(reactions1)
			await message.add_reaction(reactions2)
			await message.add_reaction(reactions3)
			await message.add_reaction(reactions4)
	elif message.content.startswith("❓"):
		if author.id in [518376913568268288 , 1133688785847205970 , 1087336787317370931]:
			await message.add_reaction(reactionsY)
			await message.add_reaction(reactionsN)
	await bot.process_commands(message)


bot.run(token) 
