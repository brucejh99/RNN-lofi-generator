import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# This creates a LSTM RNN according to the parameters we give it.
# It expects a 3D array with features and I think a loss function.
# Maybe more, still working on it
model = keras.Sequential()

# Add LSTM layer with 128 internal units. We can define stuff like activation function here too
model.add(layers.LSTM(128, input_shape=(10, 2)))

# Add a dense layer with 10 units.
model.add(layers.Dense(1))

# Prints overview of model
model.summary()

# model.compile()
# model.fit()
