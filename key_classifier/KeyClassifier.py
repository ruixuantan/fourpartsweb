from fourparts import KeyClassifier
import pandas as pd
from sklearn import svm


def initialise_key_classifier():

    data = pd.read_csv('key_classifier/train.csv')
    model = svm.SVC(gamma=1e-3, kernel='rbf')
    classifier = KeyClassifier(model)
    classifier.train(data)

    return classifier
