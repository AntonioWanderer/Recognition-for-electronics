import numpy
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, Dropout

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train_noise = numpy.random.random(size=x_train.shape)
    y_train_noise = numpy.ones(shape=y_train.shape)*10
    x_train = numpy.concatenate([x_train, x_train_noise], axis=0)
    y_train = numpy.concatenate([y_train, y_train_noise], axis=0)

