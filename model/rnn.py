import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


model = keras.Sequential()

# Add an embedding layer expecting input size of 1000 and output size of 64
model.add(layers.Embedding(input_dim=1000, output_dim=64))

# Add LSTM layer with 128 internal units
model.add(layers.LSTM(128))

# Add a dense layer with 10 units
model.add(layers.Dense(10))

# Prints overview of model
model.summary()
