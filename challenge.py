import os
import discord
import random
from dotenv import load_dotenv

# create discord connection
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print("{} has connected to Discord Guild {} (id = {})!".format(client.user, guild.name, guild.id))

    members = "\n".join([member.name for member in guild.members])
    print("Server Members:\n{}".format(members))


@client.event
async def on_message(message):
    if message.content == '-break':
        raise discord.DiscordException
    # if bot sent message, do nothing
    if message.author == client.user:
        return

    brooklyn_99_quote = "I\'m the human form of the 💯 emoji."
    if message.content == "-99!":
        await message.channel.send(brooklyn_99_quote)
    elif message.content == "-get":
        await message.channel.send("NOT YET IMPLEMENTED")


@client.event
async def on_error(event, *args, **kwargs):
    with open('challenge_error.log', 'a') as f:
        if event == 'on_message':
            f.write('Unhandled message: {}\n'.format(args[0]))
        else:
            raise


client.run(TOKEN)
