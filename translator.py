import discord
from google_trans_new import google_translator  

translator = google_translator()  

token = "BOT_TOKEN_HERE"
client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')
    activity=discord.Activity(type=discord.ActivityType.listening, name="Translation")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if reaction.emoji == '🇪🇸':
        translaty = translator.translate(str(reaction.message.content), lang_tgt='es')
        await channel.send("Translating {}'s message: {}".format(str(reaction.message.author)[:-5], reaction.message.content))
        await channel.send("`" + str(translaty) + "`")

    elif reaction.emoji == '🇫🇷':
        translaty = translator.translate(str(reaction.message.content), lang_tgt='fr')
        await channel.send("Translating {}'s message: {}".format(str(reaction.message.author)[:-5], reaction.message.content))
        await channel.send("`" + str(translaty) + "`")

    elif reaction.emoji == '🇺🇸':
        translaty = translator.translate(str(reaction.message.content), lang_tgt='en')
        await channel.send("Translating {}'s message: {}".format(str(reaction.message.author)[:-5], reaction.message.content))
        await channel.send("`" + str(translaty) + "`")

client.run(token)