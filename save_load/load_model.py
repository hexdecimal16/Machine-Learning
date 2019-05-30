import pickle
from keras.datasets import mnist
from keras.utils import np_utils

# model filename
filename = 'finalized_model.sav'

# load model
loaded_model = pickle.load(open(filename, 'rb'))

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28).astype('float32')
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


# Final evaluation of the model
scores = loaded_model.evaluate(X_test, y_test, verbose=0)
print("Large CNN Error: %.2f%%" % (100-scores[1]*100))

