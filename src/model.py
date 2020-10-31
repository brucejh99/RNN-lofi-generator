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


model = keras.Sequential()

# Add LSTM layer with 128 internal units. We can define stuff like activation function here too
model.add(layers.LSTM(128, input_shape=(10, 2)))

# Add a dense layer with 10 units.
model.add(layers.Dense(1))

# Prints overview of model
model.summary()

# model.compile()
# model.fit()
