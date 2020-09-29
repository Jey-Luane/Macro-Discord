# <---------> - = - = - <--------->
import discord
import asyncio
# <---------> - = - = - <--------->
client = discord.Client()
# <---------> - = - = - <--------->
email = "Email"
pw = "PW"
id = "Id User"
# <---------> - = - = - <--------->
@client.event
async def on_ready():
    print("Embed Macro ON")
    print("Servers: {}".format(str(len(client.servers))))
    print("Ok! Successfully logged.")

@client.event
async def on_message(message):
    if message.content.startswith('.') and message.author.id == id:
        await client.send_message (message.channel, "Message\n{}\n\nMessage\n\nMessage\n\nMessage\n\nMessage")


client.run(email, pw)
