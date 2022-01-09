# Kuro Discord BOT
# By Mauro 'xcibe95x' Leoci

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import json
import discord

from KuroBOT.Neural.kuro_train import train_data
from KuroBOT.Neural.kuro_chat import chat
from discord.ext import commands
from KuroBOT.keep_alive import keep_alive

# Teach stuff the bot could say in a category

def update_kurodb(tag, pattern, response, filename='KuroBOT/Neural/intents.json'):
    with open(filename, 'r+') as file:
        # python object to be appended

      y = {
            "tag":
            tag,
            "patterns": [
                pattern,
            ],
            "responses":
            [response]
        }

      # First we load existing data into a dict.
      file_data = json.load(file)

      labels = []

      for intent in file_data['intents']:
          if intent['tag'] not in labels:  labels.append(intent['tag'])
          #print(labels)

      if tag not in labels:
          # Join new_data with file_data inside emp_details
          file_data["intents"].append(y)
          # Sets file's current position at offset.
          file.seek(0)
          # convert back to json.
          json.dump(file_data, file, indent=4)
      elif tag in labels:
          if pattern != "" not in file_data['intents'][labels.index(tag)]['patterns']:
            file_data['intents'][labels.index(tag)]['patterns'].append(pattern)
          if response != "" not in file_data['intents'][labels.index(tag)]['responses']: 
            file_data['intents'][labels.index(tag)]['responses'].append(response)
          file.seek(0)
          json.dump(file_data, file, indent=4)

intents = discord.Intents.all()
intents.members = True

# Change default commands category
help_command = commands.DefaultHelpCommand(no_category='Other')

curry = commands.Bot(command_prefix="!",
                     intents=intents,
                     help_command=help_command)

curry.load_extension('KuroBOT.commands')



# Change Bot Play Activity Command


@curry.command(brief='[Owner Only] Change Bot Activity')
@commands.is_owner()
async def activity(activity, activity_name):
    pass
    await curry.change_presence(activity=discord.Game(name=activity_name))


@activity.error
async def secretguilddata_error(activity, error):
    if isinstance(error, commands.CheckFailure):
        await activity.send(
            "Only the owner of the server can change my activity!")


# KNOWLEDGE COMMANDS


@curry.command(brief='[Owner Only] Update bot knowledge')
@commands.is_owner()
async def train(message, tag, pattern, response):
    update_kurodb(tag, pattern, response)
    train_data()
    pass
    await message.channel.send("Train Successfully Exectued.")


@activity.error
async def botknowledge_error(train, error):
    if isinstance(error, commands.CheckFailure):
        await train.send(
            "Only the owner of the server can use this command!")


@curry.event
async def on_ready():
    print('Logged in as {0.user}'.format(curry))
    print('Account ID: ' + str(curry.user.id))
    # Setting `Playing ` status
    await curry.change_presence(activity=discord.Game(name="Constraints"))


@curry.event
async def on_member_join(member):
    await member.send(
        f"Welcome to the Above Constraints community! I'm Kuro, nice to meet you, if you need my help, use the !help command in DM or in a channel to know where i can help you, i'm still in development and in future i will be more helpful replying in a channel to all your questions."
    )


@curry.event
async def on_message(message):
    if message.author == curry.user:
        return

    await curry.process_commands(message)  # Fix command line

    if message.content.startswith("!") != True:
        await message.channel.send(chat(message.content))


keep_alive()

# Get the Environment Variable "TOKEN" which is our secret Discord Token.
# Run our Bot
curry.run(os.getenv('TOKEN'))
