import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
import asyncio
import aiomysql


class Example(commands.Cog):
   
    def __init__(self,client):
       
        self.client = client

    @commands.command()
    async def ping(self , ctx):
        await ctx.send('pong!')

class Moderation(commands.Cog):
    def __init__(self,client):
       
        self.client = client
    

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=10):
        await ctx.channel.purge(limit=amount)  
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        botMSG9 = await ctx.send('RIP the homie')
        await asyncio.sleep(2)
        await botMSG9.delete()


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *,member):
        banned_users = await ctx.guild.bans()
        memberN,memberD=member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator)==(memberN,memberD):
                await ctx.guild.unban(user)
                await ctx.send (f'unbanned {user.mention}')
                return    




def setup(client):
    
    client.add_cog(Example(client))
    
    client.add_cog(Moderation(client))
