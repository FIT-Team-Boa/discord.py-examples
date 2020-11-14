import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

@bot.event
async def on_ready():
    print("CONNECTED!")

@bot.command()
async def copy(ctx, count : int, *, msg):
    for _ in range(count):
        await ctx.send(msg)

@bot.command()
async def give(ctx, role : discord.Role, member : discord.Member):
    await member.add_roles(role)

class RoleMembersConverter(commands.RoleConverter):
    async def convert(self, ctx, arguement):
        role = await super().convert(ctx, arguement)
        return role.members
@bot.command()
async def list(ctx, members : RoleMembersConverter):
    member_list = ", ".join(m.name for m in members)
    await ctx.send(member_list)

@bot.command()
async def kill(ctx, members : commands.Greedy[discord.Member], days : int):
    member_list = ", ".join(m.name for m in members)
    await ctx.send("Oh no! {} died {} days ago! RIP".format(member_list, days))

token = ""
with open('../token.txt') as f:
    token = f.readline().strip()

bot.run(token)
