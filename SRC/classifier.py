import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

class Classifier:
  def __init__(self, input_data_frame):
    data = input_data_frame.text.to_numpy()
    target = input_data_frame.pc_nonpc_flag.to_numpy()

    self.spliting_train_test_data(data, target)
    self.vectorizing()
    self.applying_multiNB()
    self.predicting()

  def spliting_train_test_data(self, data, target):
    self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(data, target, test_size=.15)

  def vectorizing(self):
    self.vectorizer = TfidfVectorizer(max_features=25, decode_error='ignore')
    self.vectorizer.fit(self.x_train)

  def applying_multiNB(self):
    self.clf = MultinomialNB()
    self.clf.fit(self.vectorizer.transform(self.x_train), self.y_train)

  def predicting(self):
    self.y_pred = self.clf.predict(self.vectorizer.transform(self.x_test))
    print(accuracy_score(self.y_test, self.y_pred))
    print(classification_report(self.y_test, self.y_pred))
    return self.y_pred