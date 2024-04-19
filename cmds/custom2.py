'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''
import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import urllib
import random
import requests
from bs4 import BeautifulSoup


class Custom2(Cog_Extension):
    def __init__(self, bot):
        f = open('成語.txt', 'r',encoding="utf-8")
        wordd = f.read()
        self.history = []
        f.close()
        wordd = wordd.split('、')
        self.tword = []
        for i in  wordd:
            if len(i) == 0:
                continue
            else:
                if '\n' in i:
                    i = i.replace('\n','')
                    self.tword.append(i)
                else:
                    self.tword.append(i)
        
        '''
        TODO 
        要在init function 中載入單字庫

        Hint:
        1. 好像有import urllib
        2. data.json中有貼上url了
        '''

    @commands.command()
    async def Play2(self, ctx):
        self.playtime2 = 0
        startwordn = random.randint(0,len(self.tword)-1)
        startword = self.tword[startwordn]
        await ctx.send(f"第一個成語是:{startword}")
        self.history = [startword]
        self.Playny=1
    

    
    @commands.command()
    async def Ask2(self, ctx, ans):
        if self.Playny == 0:
            await ctx.send("請先使用\"Play2\"指令")
        else:
            if len(ans) != 4:
                await ctx.send("只能用四字成語喔!")
            else:
                if ans not in self.tword:
                    await ctx.send("這個成語不能用喔")
                else:
                    if ans[0] !=  self.history[self.playtime2][-1]:
                        await ctx.send("要接到前面的最後一個字喔")
                    else:
                        self.history.append(ans)
                        self.playtime2+=1
                        flag = 0
                        for i in self.tword:
                            if i in self.history:
                                continue
                            else:
                                
                                if i[0] == ans[-1]:
                                    await ctx.send(f"{i}")
                                    self.history.append(i)
                                    flag = 1
                                    break
                        if flag == 0:
                            await ctx.send("我詞窮了......你真厲害")
                            await ctx.send(f"你總共得了{self.playtime2}分")
                        else:
                            self.playtime2+=1
                            
    @commands.command()
    async def Stop2(self, ctx):
        await ctx.send("認輸了嗎????")
        await ctx.send(f"你總共得了{self.playtime2}分")
        self.playtime2 = 0
        self.history.clear()
        self.Playny=0
        

async def setup(bot):
    await bot.add_cog(Custom2(bot))