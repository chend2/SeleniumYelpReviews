import numpy as np
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import seaborn as sns
import collections
import matplotlib.pyplot as plt
import re, string

## I want to get a data frame and do some visualizations on it 


cleaned_csvs = ['cleaned_csvs\\cleaned_Sakagura.csv']
cleanedframes = [pd.read_csv(x, index_col=0) for x in cleaned_csvs]

df = cleanedframes[0]

new_df = df.copy()
new_df.date = pd.to_datetime(new_df['date'])
## this changes the all the column values of date to a timestamp


## add new columns of periods in month and year
new_df['month_year'] = new_df.date.dt.to_period('M')
new_df['year'] = new_df.date.dt.to_period('Y')

## create dataframe using monthyear and graph # reviews per month year
# gb_df = new_df.groupby('month_year').agg(
#     {'title':['count'],
#      'Status':['sum']})
# gb_df['total'] =gb_df['title']['count']

# gb_df['elites']=gb_df['Status']['sum']
# gb_df['regs']=gb_df['total']-gb_df['elites']


# gb_df.plot(y=['regs','elites'], kind='bar', use_index=True, stacked=True, figsize=(16,4), title="Reviews per Month")



## create dataframe using year and graph # reviews per year

# gb_y =new_df.groupby('year').agg(
#     {'title':['count'],
#      'Status':['sum']})


# gb_y['total'] =gb_y['title']['count']
# gb_y['elites']=gb_y['Status']['sum']
# gb_y['regs']=gb_y['total']-gb_y['elites']


# gb_y.plot(y=['regs','elites'], kind='bar', use_index=True, stacked=True, figsize=(16,4), title="Reviews per Year")


## create new dataframe grouped by rating and month_year
# rating separated subplots rating vs time

# gb_rd=new_df.groupby(['rating','month_year']).agg({'title':['count'],'Status':['sum']})
# gb_rd['elite']=gb_rd['Status']['sum']
# gb_rd['total']=gb_rd['title']['count']
# gb_rd['regs'] = gb_rd['total']-gb_rd['elite']
# gb_rd =gb_rd.reset_index()

# g = sns.catplot(x="month_year", y="total", col="rating", data=gb_rd, kind="bar", palette="Reds")

## create new dataframe grouped by rating and year
# rating separated subplots rating vs time

# gb_ry=new_df.groupby(['rating','year']).agg({'title':['count'],'Status':['sum']})
# gb_ry['elite']=gb_ry['Status']['sum']
# gb_ry['total']=gb_ry['title']['count']
# gb_ry['regs'] = gb_ry['total']-gb_ry['elite']
# gb_ry =gb_ry.reset_index()

# g = sns.catplot(x="year", y="total", col="rating", data=gb_ry, kind="bar", palette="Reds")

## creates two dataframes one by year and the other by monthyear 
## plots sublots reviews vs year/month_year per rating

# gb__ = new_df.copy()
# gb__['count']  = gb__.apply(lambda x: 1, axis = 1) 

# gb__rd_= gb__.groupby(['rating' ,'month_year']).agg({'count': ['count']})
# gb__rd_=gb__rd_.reset_index()
# gb__rd_['new_count'] =gb__rd_['count']['count']
# g = sns.catplot(x="month_year", y="new_count", col="rating", data=gb__rd_, kind="bar", palette="Reds")


# gb__ry= gb__.groupby(['rating' ,'year']).agg({'count': ['count']})
# gb__ry= gb__ry.reset_index()
# gb__ry['new_count'] =gb__ry['count']['count']
# g = sns.catplot(x="year", y="new_count", col="rating", data=gb__ry, kind="bar", palette="Reds")

## daaframe for plotting avg vs year/month_year

# new_df_2 = new_df.copy()
# new_df_2y = new_df_2.groupby(['year']).mean()
# new_df_2y.plot(y='rating', use_index=True, kind='line', figsize=(16,4), ylim =(2,5.5), title="Total rating in Years")

# new_df_2my = new_df_2.groupby(['month_year']).mean()
# new_df_2my.plot(y='rating', use_index=True, kind='line', figsize=(16,4), ylim =(2,5.5), title="Total rating in Years")


## dataframes and plotting for avg elite and regular rating over time (year)

# new_df_ds = new_df_2.groupby(['Status','year']).agg({'rating':['mean']})
# new_df_ds =new_df_ds.reset_index()
# new_df_reg = new_df_ds.loc[new_df_ds['Status']==0]
# new_df_elite = new_df_ds.loc[new_df_ds['Status']==1]
# new_df_reg = new_df_reg.set_index('year')
# new_df_elite = new_df_elite.set_index('year')
# new_df_reg['reg_rating'] = new_df_reg['rating']['mean']
# new_df_elite['el_rating'] = new_df_elite['rating']['mean']
# new_df_reg['el_rating'] = new_df_elite['el_rating']
# new_df_reg = new_df_reg.reset_index()

# new_df_reg.plot(x='year', y=['reg_rating','el_rating'], kind='line', figsize=(16,4), ylim =(2,5.5), title="Regular vs Elite rating in Years")


### Seaborn Pearson Corr Heatmap ###
# pearson_df = new_df
# pearson_df = pearson_df.drop(columns=["title","date","text","month_year","year"])
# plt.figure(figsize=(12,10))
# cor = pearson_df.corr()
# sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
# plt.show()





#### handle n-grams here ####

def tokenize(s):
    # """Convert string to lowercase and split into words (ignoring
    # punctuation), returning list of words.
    # """
    word_list = re.findall(r'\w+', s.lower())
    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    return filtered_words

def count_ngrams(lines, min_length=2, max_length=4):
#     """Iterate through given lines iterator (file object or list of
#     lines) and return n-gram frequencies. The return value is a dict
#     mapping the length of the n-gram to a collections.Counter
#     object of n-gram tuple and number of times that n-gram occurred.
#     Returned dict includes n-grams of length min_length to max_length.
#     """
    lengths = range(min_length, max_length + 1)
    ngrams = {length: collections.Counter() for length in lengths}
    queue = collections.deque(maxlen=max_length)
# Helper function to add n-grams at start of current queue to dict
    def add_queue():
        current = tuple(queue)
        for length in lengths:
            if len(current) >= length:
                ngrams[length][current[:length]] += 1
# Loop through all lines and words and add n-grams to dict
    for line in lines:
        for word in tokenize(line):
            queue.append(word)
            if len(queue) >= max_length:
                add_queue()
# Make sure we get the n-grams at the tail end of the queue
    while len(queue) > min_length:
        queue.popleft()
        add_queue()
    return ngrams

def print_most_frequent(ngrams, num=10):
    """Print num most common n-grams of each length in n-grams dict."""
    for n in sorted(ngrams):
        print('----- {} most common {}-word phrase -----'.format(num, n))
        for gram, count in ngrams[n].most_common(num):
            print('{0}: {1}'.format(' '.join(gram), count))
        print('')

def print_word_cloud(ngrams, num=5):
    """Print word cloud image plot """
    words = []
    for n in sorted(ngrams):
        for gram, count in ngrams[n].most_common(num):
            s = ' '.join(gram)
            words.append(s)
            
    cloud = WordCloud(width=1440, height= 1080,max_words= 200).generate(' '.join(words))
    plt.figure(figsize=(20, 15))
    plt.imshow(cloud)
    plt.axis('off');
    plt.show()
    print('')


great_reviews = new_df.loc[new_df['rating']>3].text
most_frequent_greatreviews = count_ngrams(great_reviews,max_length=3)
print_most_frequent(most_frequent_greatreviews, 10)

bad_reviews = new_df.loc[new_df['rating']<3].text
most_frequent_badreviews = count_ngrams(bad_reviews,max_length=3)
print_most_frequent(most_frequent_badreviews, 10)

