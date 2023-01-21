import discord
import time
from youtube_dl import YoutubeDL
import youtube_dl
from discord import FFmpegPCMAudio
from discord.utils import get

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.bot:
            return None
        
        if message.content == ("!시작"):
            await message.author.voice.channel.connect()
            
        if message.content.startswith ("!음악추가"):
            channel = message.channel
            with open("file.txt", "a", encoding='utf-8') as f: #txt추가
                data= message.content.split(" ")[1]
                f.write(data)
                
                embed = discord.Embed(title = '음악 추가', description = title + '이름을 추가하였습니다' , color = discord.Color.blue())
                await channel.send(embed=embed)
                
        if message.content == ("!음악목록"):
            channel = message.channel
            with open('file.txt', "r", encoding='utf-8') as f: #txt읽기
                main = f.read()
                f.close()
            embed = discord.Embed(title = '목록', description = main + '\n\n**목록의 이름을 입력해주세요!**' , color = discord.Color.yellow())
            await channel.send(embed=embed)
        
        if message.content.startswith ("!음악다운"): # x
            for vc in client.voice_clients:
                if vc.guild ==message.guild:
                    channel = message.author.voice.channel
                    voice=vc
                    url=message.content.split(" ")[1]
                    options = {
                        'outtmpl' :"file/"+url.split('=')[1] + ".mp3"
                    }
                    
                    embed = discord.Embed(title = '음악 다운로드', description = title + '다운을 시작할게요!' , color = discord.Color.blue())
                    await channel.send(embed=embed)
                    
                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([url])
                        info=ydl.extract_info(url, download=False)
                        title=info["title"]
                        
                    embed = discord.Embed(title = '음악 다운로드', description = '다운을 시작할게요!' , color = discord.Color.blue())
                    await channel.send(embed=embed)
                    
        if message.content.startswith ("!재생url"):
            for vc in client.voice_clients:
                if vc.guild ==message.guild:
                    voice=vc
                    url=message.content.split(" ")[1]
                    voice.play(discord.FFmpegPCMAudio(source="file/"+url.split('=')[1] + ".mp3"))
                    
        if message.content.startswith ("!재생"):
            for vc in client.voice_clients:
                if vc.guild ==message.guild:
                    voice=vc
                    name=message.content.split(" ")[1]
                    voice.play(discord.FFmpegPCMAudio(source="file/"+ name + ".mp3"))
                    embed = discord.Embed(title = '음악 재생', description = '재생을 시작힐게요!' , color = discord.Color.blue())
                    await channel.send(embed=embed)

        if message.content == ("!나가"): # x
            channel=voice.channel
            await message.channel.disconnect()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA1NDY5Njk5MjA4Njk1NDA3NA.GSI69K.hkB7jSsfZiITqEHZYgnnbPeBmzbWMyTLUZ7kxQ')