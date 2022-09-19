import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
import os
from loguru import logger
from nltk.stem.lancaster import LancasterStemmer


# ---------------------
## This class handles all chatbot Ai model functionality
# Main Program Entry
class ChatbotModel:
    def __init__(self):
        self._solutions_path = os.path.dirname(__file__) + '/Solutions'
        self._model_path = os.path.dirname(__file__) + '/Model'
        self.stemmer = LancasterStemmer()

    # ---------------------
    ## Load all chatbot solution files
    def LoadSolutions(self):
        logger.debug(self._solutions_path)

    # ---------------------
    ## Load Model File
    def LoadModel(self):
        with open("Model/data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)

    # ---------------------
    ## Create Model File
    def CreateModel(self):
        words = []
        labels = []
        docs_x = []
        docs_y = []

        # loops thorugh intents and tokenize
        for intent in data['intents']:
            for pattern in intent['patterns']:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent['tag'])

            if intent['tag'] not in labels:
                labels.append(intent['tag'])

        # stem the patterns to the root of the word
        words = [self.stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [self.stemmer.stem(w.lower()) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)

        training = np.array(training)
        output = np.array(output)

        with open("Model/data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)

    # ---------------------
    ## Start Model
    def InitModel(self):
        # resets previous info
        tf.compat.v1.reset_default_graph()
        # define input shape for the model
        net = tflearn.input_data(shape=[None, len(training[0])])
        # add fully connected layer with 8 neurons
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        # output layer
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)


if __name__ == '__main__':
    CeciliaModelv = ChatbotModel()
    CeciliaModelv.LoadSolutions()
