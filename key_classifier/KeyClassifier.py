from fourparts import KeyClassifier
import pandas as pd


def initialise_key_classifier():

    data = pd.read_csv('key_classifier/train.csv')
    classifier = KeyClassifier(hidden_layer_sizes=(100,), max_iter=1000)
    classifier.train(data)

    return classifier
