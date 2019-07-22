import re, string
import numpy as np
import pandas as pd
import datetime

def handleDateString(dataframe):
    def findAndSlice(str_):
            val = str_.find('\n')
            if val != -1:
                val = val -1
                str_ = str_[:val]
            return str_
    
    dataframe.date = dataframe.date.apply(lambda x: findAndSlice(x))
    dataframe.date = dataframe.date.apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'))
    
def strNumToInt(dataframe):    
    dataframe.rating = (dataframe.rating.str.replace(r'\D.','')).astype(int)
    dataframe.friends = (dataframe.friends.str.replace(r'\D','')).astype(int)
    dataframe.photos = (dataframe.photos.str.replace(r'\D','')).astype(int)
    dataframe.review_num = (dataframe.review_num.str.replace(r'\D','')).astype(int)
    
def statusToInt(dataframe):
    dataframe.Status = dataframe.Status.apply(lambda x: x.replace("Not Elite", "0"))
    dataframe.Status = dataframe.Status.apply(lambda x: x.replace("Elite ’19","1"))
    dataframe.Status = dataframe.Status.astype(int)
    
def word_len(dataframe):
    def cleanedTextLen(string):
        word_list = re.findall(r'\w+', string.lower())
        return len(word_list)
    dataframe['word_len'] = dataframe.text.apply(lambda x:cleanedTextLen(x))
