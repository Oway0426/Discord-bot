import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import urllib
import random
import requests


class Wordle(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        self.Play = 0
        r = requests.get('https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt')
        y = str(r.content)
        x = []
        x = y.split('\\n')
        x [0] = x[0].replace('b\'','')
        x[-1] = x[-1].replace('\'','')
        self.word_list = x
        '''
        TODO 
        要在init function 中載入單字庫

        Hint:
        1. 好像有import urllib
        2. data.json中有貼上url了
        '''

    @commands.command()
    async def Play(self, ctx):
        self.playtime = 0
        word = random.randint(0,len(self.word_list)-1)
        self.ans = self.word_list[word]
        print(self.ans)
        await ctx.send("Start")
        self.Play=1
        '''
        TODO 
        要在爬好的單字庫中, 隨機挑選一個單字做為預設的答案
        '''
    

    
    @commands.command()
    async def Ask(self, ctx, ans):
        
        if self.Play == 0:
             await ctx.send("請先輸入 Play 指令")
        else:
            if self.playtime > 8:
                await ctx.send(f"真可惜,超過8次, 答案是{self.ans}")
                self.Play = 0
            else:
                self.playtime+=1
                if len(ans) != 5:
                    await ctx.send("請輸入5個字母的單字")
                else:
                    if ans not in self.word_list:
                        await ctx.send("這好像不是個單字")
                    else:
                        if ans == self.ans:
                            await ctx.send("恭喜答對!!!")
                            self.Play = 0
                        else:
                            flag = False
                            for i in range(5):
                                if ans[i] in self.ans:
                                    flag = True
                                    if ans[i] == self.ans[i]:
                                        await ctx.send(f"{ans[i]} 在正確位置上")
                                    else:
                                        await ctx.send(f"{ans[i]} 在這個單字裡")
                                else:
                                    continue
                            if flag == False:
                                await ctx.send("ㄏㄏ真了不起，一個都沒猜中")
                            else:
                                await ctx.send("差一點啦")

                    
        '''
        ans 是使用者傳入的猜測答案

        TODO
        1. 沒有play直接ask : 請先輸入 Play 指令
        2. 不是5個字的單字 : 請輸入5個字母的單字
        3. 不是單字的英文組合(不在單字庫中) : 這好像不是個單字
        4. 答對 : 恭喜答對!!!
        5. 猜太多次了 : 真可惜, 答案是{answer}
        '''
        


async def setup(bot):
    await bot.add_cog(Wordle(bot))