import sys, os
import pandas as pd
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

class ETL:
  def __init__(self):
    self.filename = 'ASSETS/New_Query_2021_09_27.csv'
    self.__load_df()
    self.__drop_unecessary_cols()
    self.__cleaning()
    self.__extracting_labesl_of_results_orig()
  
  def __load_df(self):
    self.data_frame = pd.read_csv(self.filename, dtype=str, engine='python', encoding='utf-8').fillna(0)
  
  def __drop_unecessary_cols(self):
    self.data_frame.drop(columns=['doc_id', 'doc_status', 'scrapetime',
            'update_time', 'scrape_count', 'title', 'cleaned_title',
            'url', 'text_hash', 'comment_count', 'share_count',
            'fb_graph_api_call_time', 'reaction_count', 'results_json',
            'agegroup', 'outlet', 'owntime', 'author', 'top1', 'top2',
            'top4','top8', 'top12', 'top24', 'top48', 'results_alt',
            'text_tf'], inplace=True)
  
  def __cleaning(self):
    for column in self.data_frame.columns:
      self.data_frame['results_orig'] = self.data_frame['results_orig'].str.replace("u'", '')
      self.data_frame['text'] = self.data_frame['text'].values.astype('U')
      self.data_frame[column] = self.data_frame[column].str.replace("[^ ,:a-zA-Z0-9-áéíóúöőüű]+", '').str.lower()
    
  def __extracting_labesl_of_results_orig(self):
    self.politician_names = []
    politicians_names_not_clean = np.array(self.data_frame['results_orig'].loc[2][7:].split(','))
    
    #Transforming the column results_orig (originally a dict) in an array of Strings (Politician names)
    [self.politician_names.append(item.split(':')[:1][0].strip()) for item in politicians_names_not_clean]
    
