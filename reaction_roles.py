import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

role_add_message_id = 775828238097317908
role_remove_message_id = 775837036317900821
emoji_to_role = {
    "👍": 753706042809909328,
    "test": 775836134655000586
}

@bot.event
async def on_ready():
    print("CONNECTED!")

@bot.event
async def on_raw_reaction_add(payload):
    #Message may not be in a guild!
    if payload.emoji.name in emoji_to_role.keys():
        guild = bot.get_guild(payload.guild_id)
        role = guild.get_role(emoji_to_role[payload.emoji.name])
        if payload.message_id == role_add_message_id:
            await payload.member.add_roles(role)
        elif payload.message_id == role_remove_message_id:
            await payload.member.remove_roles(role)

token = ""
with open('../token.txt') as f:
    token = f.readline().strip()

bot.run(token)
