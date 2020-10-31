import numpy as np
import tensorflow as tf
import magenta
from numpy import array
from tensorflow import keras
from tensorflow.keras import layers



# Reading data. LSTM expects 3D array as input
def process_data(file_path):
    # raw_data = list(map(lambda x: x.split(','), open(file_path).read().split('\n')))
    data = array([
        [0.1, 1.0],
        [0.2, 0.9],
        [0.3, 0.8],
        [0.4, 0.7],
        [0.5, 0.6],
        [0.6, 0.5],
        [0.7, 0.4],
        [0.8, 0.3],
        [0.9, 0.2],
        [1.0, 0.1]])
    # reshapes sequence into 3D 
    data.reshape((1, 10, 2))
    print(data.shape)

process_data('dataset/shampoo_sales.csv')


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
