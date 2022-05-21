import discord.client
from discord.ext import commands
from discord.utils import get
from discord import role
from discord import utils
from discord import Member
from discord import guild

client = commands.Bot(command_prefix='%')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(name='test', aliases=['test-command'], pass_context=True)
async def test(ctx):
    channel = client.get_channel(id=967173975799128085)
    await channel.send('Hello World!')


@client.command(name='security', aliases=['add-security'], pass_context=True)
async def security(ctx, user: discord.Member):
    secrole = discord.utils.get(ctx.message.guild.roles, name='𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲-𝐆𝐮𝐚𝐫𝐝')
    jobrole = discord.utils.get(ctx.message.guild.roles, name='Jobs')
    verrole = discord.utils.get(ctx.message.guild.roles, name='Verified')
    await user.add_roles(secrole)
    await user.add_roles(jobrole)
    await user.add_roles(verrole)
    await ctx.send(f"{user.mention} has been added to the security team!")
    return

@client.command(name='rsecurity', aliases=['remove-security'], pass_context=True)
async def rsecurity(ctx, user: discord.Member):
    secrole = discord.utils.get(ctx.message.guild.roles, name='𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲-𝐆𝐮𝐚𝐫𝐝')
    jobrole = discord.utils.get(ctx.message.guild.roles, name='Jobs')
    verrole = discord.utils.get(ctx.message.guild.roles, name='Verified')
    await user.remove_roles(secrole)
    await user.remove_roles(jobrole)
    await user.remove_roles(verrole)
    await ctx.send(f"{user.mention} has been removed from the security team!")
    return
    
@client.command(name='bar', aliases=['add-bar'], pass_context=True)
async def bar(ctx, user: discord.Member):
    barrole = discord.utils.get(ctx.message.guild.roles, name='𝐁𝐚𝐫𝐭𝐞𝐧𝐝𝐞𝐫')
    jobrole = discord.utils.get(ctx.message.guild.roles, name='Jobs')
    verrole = discord.utils.get(ctx.message.guild.roles, name='Verified')
    await user.add_roles(barrole)
    await user.add_roles(jobrole)
    await user.add_roles(verrole)
    await ctx.send(f"{user.mention} has been added to the bartender team!")
    return

@client.command(name='rbar', aliases=['remove-bar'], pass_context=True)
async def rbar(ctx, user: discord.Member):
    barrole = discord.utils.get(ctx.message.guild.roles, name='𝐁𝐚𝐫𝐭𝐞𝐧𝐝𝐞𝐫')
    jobrole = discord.utils.get(ctx.message.guild.roles, name='Jobs')
    verrole = discord.utils.get(ctx.message.guild.roles, name='Verified')
    await user.remove_roles(barrole)
    await user.remove_roles(jobrole)
    await user.remove_roles(verrole)
    await ctx.send(f"{user.mention} has been removed from the bartender team!")
    return

@client.command(pass_context=True)
async def nvip(ctx, member: discord.Member, first, last, vipnum, discordname, discordlastname = ''):
    await member.edit(nick=first + ' ' + last + ' ' + '|'  + ' ' + '#' +vipnum + ' ' + '|' + ' ' + discordname + ' ' + discordlastname)
    await ctx.send(f'Nickname was changed for {member.mention} ')
    
@client.command(pass_context=True)
async def nemp(ctx, member: discord.Member, first, last, job):
    await member.edit(nick=first + ' ' + last + ' ' + '|'  + ' ' + job)
    await ctx.send(f'Nickname was changed for {member.mention} ')

client.run("OTc2NjE0NDk5MjUzNjMzMDU0.GfJvXN.rTrBHJZOygAWrBzvY4CMFZN-fMih1zOXkl2se8")
