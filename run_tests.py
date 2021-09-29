from SRC.etl import ETL
from SRC.classifier import Classifier
import pandas as pd
from SRC.task1 import verify_political_or_non_political
from unittest import mock, TestCase, main

class TestClassifier(TestCase):

  @classmethod
  def setUpClass(cls):
    cls.etl = ETL()
    cls.response_y_predcition = Classifier(TestClassifier.etl.data_frame)

  def test_task1(self):
    response_array = verify_political_or_non_political(['orosz anna', 'random name'], self.etl.politician_names)
    
    self.assertEqual(response_array, [1, 0])

if __name__ == '__main__':
  main()