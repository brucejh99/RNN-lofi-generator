from numpy import array


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
