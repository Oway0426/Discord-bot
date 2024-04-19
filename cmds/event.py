import discord
from discord.ext import commands
import os
from core import Cog_Extension

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        g_channel = self.bot.get_channel(1114861226065920112)
        await g_channel.send(f"歡迎{member}加入!")

    '''
    TODO (optional)
    Add other events such as on_message, on_command_error
    '''
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        await ctx.send(f"指令錯誤: {error}")

    @commands.Cog.listener()
    async def on_message(self,message):
        g_channel = self.bot.get_channel(1114861226065920112)
        if message.author == self.bot.user:  
            return
        else:
            if message.content == 'Hi':
                await g_channel.send("Hello")
            if message.content == "Nice to meet you":
                await g_channel.send("Nice to meet you ,too")
            
      
async def setup(bot):
    await bot.add_cog(Event(bot))