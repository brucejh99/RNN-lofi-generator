import numpy as np
import tensorflow as tf
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

process_data('datasets/shampoo_sales.csv')


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

model.compile()
model.fit()
