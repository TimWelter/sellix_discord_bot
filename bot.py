import os
from discord import Intents, Embed, utils
from discord.ext import commands
import sellix_requests

TOKEN = os.getenv('DISCORD_TOKEN')

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

intents = Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', help_command=help_command, intents=intents)

@bot.command(name='stock', help='Shows the stock')
async def stock(ctx):
    ticket_channel = bot.get_channel(1198590206685749248)
    products = sellix_requests.get_products()
    chunks = list(utils.as_chunks(products, 25))
    embeds = []
    amountChunks = len(chunks)
    for i in range(0, amountChunks):
        chunk = chunks[i]
        if i == 0:
            embed = Embed(title='Stock:')
        else:
            embed = Embed()
        for product in chunk:
            embed.add_field(name=f"**{product['title']}**", value=f"${product['price']} - ({product['stock']} in stock)", inline=False)
        embeds.append(embed)
    embeds.append(Embed().add_field(name='', value=f"All account builds last logged in minimum of 7-14 days ago\nTo purchase please open a ticket in {ticket_channel.mention} (Automatic payments via Crypto are handled on the website)\nhttps://bread-services.mysellix.io/"))
    await ctx.send(embeds=embeds)

@bot.command(name='instock', help='Shows the currently available stock')
async def instock(ctx):
    ticket_channel = bot.get_channel(1198590206685749248)
    products = sellix_requests.get_products()
    products = filter(lambda p: p['stock'] > 0, products)
    chunks = list(utils.as_chunks(products, 25))
    embeds = []
    amountChunks = len(chunks)
    for i in range(0, amountChunks):
        chunk = chunks[i]
        if i == 0:
            embed = Embed(title='Stock:')
        else:
            embed = Embed()
        for product in chunk:
            embed.add_field(name=f"**{product['title']}**", value=f"${product['price']} - ({product['stock']} in stock)", inline=False)
        embeds.append(embed)
    embeds.append(Embed().add_field(name='', value=f"All account builds last logged in minimum of 7-14 days ago\nTo purchase please open a ticket in {ticket_channel.mention} (Automatic payments via Crypto are handled on the website)\nhttps://bread-services.mysellix.io/"))
    await ctx.send(embeds=embeds)


print('Bot starting!')
bot.run(TOKEN)
