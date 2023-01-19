import os 
from dotenv import load_dotenv
import discord
import csv
import random
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)


@bot.command()
async def wen(ctx):

    with open('kaine.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        random_row = random.choice(list(data))
        print(random_row[0])

        await ctx.send(random_row[0] + " - Mr. Kaine")

bot.run(TOKEN)