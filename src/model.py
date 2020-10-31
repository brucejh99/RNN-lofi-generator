import numpy as np
import tensorflow as tf
import magenta
from numpy import array
from tensorflow import keras
from tensorflow.keras import layers


# Things we need to figure out. Lot of these are probably hyperparameters:
# 1. number of internal units for layers.
# 2. what is dense and what to do with it
# 3. input/output dimensions
# 4. for each layer and tool we use, look into the possible arguments and figure out what we need to do with each


model = keras.Sequential()

# Add LSTM layer with 128 internal units. We can define stuff like activation function here too.
# Comes built in with the information gating system we talk about in our report according to:
# https://towardsdatascience.com/implementation-of-rnn-lstm-and-gru-a4250bf6c090
model.add(layers.LSTM(128))

# Add a dense layer with 10 units. A dense layer just means it gets output from all neurons in the previous layer.
model.add(layers.Dense(1))

# Prints overview of model.
model.summary()

# In compiling, we need to pass in things like loss
# model.compile()
# model.fit()
