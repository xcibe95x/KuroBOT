# Kuro Bot used on Discord: https://discord.gg/pzRDBKXMZu
# Author: Mauro 'xcibe95x' Leoci
# License: Open Source
# Language: Python


# Train Bot if it doesn't have any data trained
import os.path
from os import path

from KuroBOT.Neural.kuro_train import train_data

if path.exists("chat_model") != True:
  train_data()

# Load Kuro.py

import KuroBOT.kuro
KuroBOT.kuro()