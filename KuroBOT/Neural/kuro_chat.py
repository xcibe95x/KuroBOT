import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import json 
import numpy as np
from tensorflow import keras
#from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
#from colorama import Fore, Style, Back

#import random
import pickle

with open("KuroBOT/Neural/intents.json") as file:
    data = json.load(file)

def chat(message):

    # Load trained model
    model = keras.models.load_model('chat_model')

    # Load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # Load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # Parameters
    max_len = 20

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([message]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
            if i['tag'] == tag:
                KuroResponse = np.random.choice(i['responses'])
                return KuroResponse