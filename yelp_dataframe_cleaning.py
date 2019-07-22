import re, string
import numpy as np
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import sys
import time
import collections
import matplotlib
import matplotlib.pyplot as plt
import CleanerHelpers as C

rest_reviews_csvs = ['Donburiya.csv', 
					'nonono.csv', 
					'Ootoya_Chelsea.csv', 
					'Sakagura.csv', 
					'Soba_Totto.csv', 
					'Torishin.csv',
					'Yakitori_Taisho.csv',
					'Yakitori_TORA.csv',
					'Yakitori_Totto.csv',
					'Yopparai.csv']


dataframes_list = [pd.read_csv(x,index_col=0)for x in rest_reviews_csvs]

for item in dataframes_list:
	C.handleDateString(item)
	C.strNumToInt(item)
	C.statusToInt(item)
	C.word_len(item)

cleaned_csvs = list(map(lambda x:"cleaned_csvs\\cleaned_"+x, rest_reviews_csvs))

for i in range(len(cleaned_csvs)):
	dataframes_list[i].to_csv(cleaned_csvs[i])

