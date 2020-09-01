import os
from discord.ext import commands
from dotenv import load_dotenv

# create discord connection
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("{} has connected to Discord Guild!".format(bot.user.name))


@bot.command(name='hello', help='Says Hello!')
async def say_hello(ctx):
    response = "Hello!"
    await ctx.send(response)

# @client.event
# async def on_message(message):
#     if message.content == '-break':
#         raise discord.DiscordException
#     # if bot sent message, do nothing
#     if message.author == client.user:
#         return
#
#     if message.content == "-get":
#         await message.channel.send("NOT YET IMPLEMENTED")
#
#
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('challenge_error.log', 'a') as f:
#         if event == 'on_message':
#             f.write('Unhandled message: {}\n'.format(args[0]))
#         else:
#             raise


bot.run(TOKEN)
