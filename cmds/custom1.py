'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''

import discord
from discord.ext import commands
from core import Cog_Extension
import time

class Custom1(Cog_Extension):
    def __init__(self, bot):
        pass
        
    # Add todolist 
    # item 是要增加的待辨事項
    @commands.command()
    async def localtime(self, ctx):
        second = time.time()
        lt = time.ctime(second)
        await ctx.send(f"{lt}")

    # Remove todolist
    # item 是要移除的待辨事項
    @commands.command()
    async def timecounter(self, ctx):
        await ctx.send("https://tw.piliapp.com/timer/stopwatch/")
        await ctx.send("Google 是個好工具")

    # Sort todolist
    @commands.command()
    async def computer(self, ctx, ask1):
        ans = eval(ask1)
        print(ans)
        await ctx.send(f"{ans}")
        


async def setup(bot):
    await bot.add_cog(Custom1(bot))