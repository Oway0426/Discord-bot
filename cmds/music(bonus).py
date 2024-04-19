import discord
from discord.ext import commands
import os
from core import Cog_Extension
class Music(Cog_Extension):
    def __init__(self,bot):
        self.play_list = []
        self.bot = bot
    @commands.command()
    async def play(self, ctx, url):
        self.play_list.append(url)
        
        os.chdir('./cmds/')
        song_exist = os.path.isfile("song.mp3")
            
        try:
            if song_exist:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("adding to the play list(fake)")
            print(self.play_list)
            #await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            os.chdir('../')
            return
                
            '''
            TODO (optional)
            Allow users to seach for song by name
            (Try adding a web crwaler or exploring the options of yt-dlp)
            Reference : https://www.mankier.com/1/yt-dlp
            '''
        os.system(f"yt-dlp_x86.exe --extract-audio --audio-format mp3 --audio-quality 0 {url}")
        await ctx.send("installing")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice is None:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='一般')
            await voiceChannel.connect(timeout = 600.0)
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
                self.play_list.pop(0)
        os.chdir('../')
        voice.play(discord.FFmpegPCMAudio(executable = './cmds/ffmpeg.exe', source = "./cmds/song.mp3"))
        
    '''
        TODO (optional)
        Add other features such as queue, vote, etc.https://www.youtube.com/watch?v=JCs7s5BnwAA
    '''
    async def PLay(self, ctx, url):
        os.chdir('./cmds/')
        song_exist = os.path.isfile("song.mp3")
            
        os.system(f"yt-dlp_x86.exe --extract-audio --audio-format mp3 --audio-quality 0 {url}")
        await ctx.send("installing")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice is None:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='一般')
            await voiceChannel.connect(timeout = 600.0)
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        for file in os.listdir("./"):
            print(file)
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
                self.play_list.pop(0)
        os.chdir('../')
        voice.play(discord.FFmpegPCMAudio(executable = './cmds/ffmpeg.exe', source = "./cmds/song.mp3"))
        if len(self.play_list)!=0:
            print("continue")
            url = self.play_list[0]
            Music.PLay(self,ctx,url)
        else:
            return
    @commands.command()
    async def leave(self,ctx):
        self.play_list.clear()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
                await voice.disconnect()
        except:
            await ctx.send("The bot is not connected to a voice channel.")
    @commands.command()
    async def pause(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try: 
            if voice.is_playing():
                voice.pause()
            else:
                await ctx.send("Currently no audio is playing.")
        except:
            await ctx.send("Bot is not connected to a voice channel.")


    @commands.command()
    async def resume(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            if voice.is_paused():
                voice.resume()
            else:
                await ctx.send("The audio is not paused.")
        except:
            await ctx.send("Bot is not connected to a voice channel.")

    @commands.command()
    async def stop(self,ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            voice.stop()
        except:
            await ctx.send("Bot is not connected to a voice channel.")
    
async def setup(bot):
    await bot.add_cog(Music(bot))