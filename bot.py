import os
from discord import Intents
from discord.ext import commands
import sellix_requests

TOKEN = os.getenv('DISCORD_TOKEN')

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

intents = Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', help_command=help_command, intents=intents)

@bot.command(name='stock', help='Shows the current stock')
async def stock(ctx):
    products = sellix_requests.get_products()
    msg = 'Current stock:\n'
    for product in products:
        msg += f"**{product['title']}** - ${product['price']} ({product['stock']} in stock)\n"
    msg += '\nAll account builds last logged in minimum of 7-14 days ago\n\nTo purchase please open a ticket in <#1198590206685749248> (Automatic payments via Crypto are handled on the website)\nhttps://bread-services.mysellix.io/'
    await ctx.send(msg)

print('Bot starting!')
bot.run(TOKEN)
