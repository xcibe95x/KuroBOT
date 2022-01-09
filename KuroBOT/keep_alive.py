# Web Server Keep Alive Script
# Create a WebServer to Keep the Bot Alive on Replit.com, so we don't need an hosting # or to host the bot on our server at all.
# Uses https://uptimerobot.com to ping the https url every 5 minutes 
# Ignore the Development Server stuff is not important

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask
from threading import Thread
from flask import render_template

# Remove Annoying Red Loggings
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('Kuro')

# Create an HTML default home in the root of the webserver
@app.route('/')
def home():
      #return "<b>Hello, i'm Kuro, i'm currently running!</b>"
      return render_template("index.html")
      
# Run the webserver on replit localhost
def run():
  app.run(host='0.0.0.0',port=8080)

# Funtion run the webserver and keep the bot alive
def keep_alive():
    t = Thread(target=run)
    t.start()