from keras.models import Sequential
from keras.layers import Dense 

def create_basic_autoencoder(hidden_layer_size):
    model = Sequential()
    model.add(Dense(units=hidden_layer_size, input_shape=(784,),
    activation='relu'))
    model.add(Dense(units=784, activation='sigmoid'))
    return model