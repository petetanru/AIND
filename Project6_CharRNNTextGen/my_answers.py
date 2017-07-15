import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []

    # generate i/o pairs
    # X - iterates over the text (minus window size) to capture a window of text.
    # y - iterates over the text to captures the next letter, following the window.

    X = [series[i:window_size + i] for i in range(len(series) - window_size)]
    y = [serie for serie in series[window_size:]]

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):

    # LSTM, a type of recrruent layer, allows certain node to skip forward
    # Dense layer multiplies the output of LSTM back to match the number of categories
    # No softmax activation is needed to translate the output (in other cases of different classes) into probabilities. For a regression, the raw continous value works.

    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    model.summary()
    
    # build model using keras documentation recommended optimizer initialization
    optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # compile the model
    model.compile(loss='mean_squared_error', optimizer=optimizer)


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    # remove as many non-english characters and character sequences as you can
    text = text.replace('\n',' ')    
    text = text.replace('\r',' ')
    text = text.replace('\\',' ')
    text = text.replace('@',' ')
    text = text.replace('/',' ')
    text = text.replace('*',' ')
    text = text.replace('%',' ')
    text = text.replace('#',' ')
    text = text.replace('à','a')
    text = text.replace('â','a')
    text = text.replace('è','e')
    text = text.replace('é','e')
    text = text.replace('[',' ')
    text = text.replace(']',' ')
    text = text.replace('(',' ')
    text = text.replace(')',' ')
    text = text.replace('\ufeff',' ')
    text = text.replace('$',' ')
    text = text.replace('1',' ')
    text = text.replace('2',' ')
    text = text.replace('3',' ')
    text = text.replace('4',' ')
    text = text.replace('5',' ')
    text = text.replace('6',' ')
    text = text.replace('7',' ')
    text = text.replace('8',' ')
    text = text.replace('9',' ')
    text = text.replace('0',' ')
    text = text.replace('&',' ')
    text = text.replace('-',' ')

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    # inputs - iterates over text, each step being step_size, to create a list of window of text
    for i in range(0, len(text) - window_size, step_size):
        window = text[i:window_size + i]
        inputs.append(window)

    # output - iterates over text, each step being step_size, to create a list of the character following the window of text
    outputs = [i for i in text[window_size::step_size]]
    
    return inputs,outputs
