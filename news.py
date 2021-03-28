import requests
from bs4 import BeautifulSoup as bs
import os
import glob
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import pandas as pd
import urllib, csv, os, datetime, urllib.request, re ,sys

newsapi=NewsApiClient(api_key='50c140da3c164aec9cec08cea8211189')
data=newsapi.get_everything(q='India', language='en', page_size=100)

articles=data['articles']

#for x, y in enumerate(articles):
    #print(f'{x} {y["title"]}')

#for key,value in articles[0].items():
    #print(f"\n{key.ljust(15)} (value)")
column_names=['source', 'author', 'title', 'description', 'urlToImage', 'publishedAt', 'content']
df=pd.DataFrame(articles, columns=column_names)

df.to_csv('data1.csv')

newsapi=NewsApiClient(api_key='50c140da3c164aec9cec08cea8211189')
data=newsapi.get_everything(q='US', language='en', page_size=100)

articles=data['articles']

#for x, y in enumerate(articles):
    #print(f'{x} {y["title"]}')

#for key,value in articles[0].items():
    #print(f"\n{key.ljust(15)} (value)")
column_names=['source', 'author', 'title', 'description', 'urlToImage', 'publishedAt', 'content']
df=pd.DataFrame(articles, columns=column_names)

df.to_csv('data2.csv')

newsapi=NewsApiClient(api_key='50c140da3c164aec9cec08cea8211189')
data=newsapi.get_everything(q='China', language='en', page_size=100)

articles=data['articles']

#for x, y in enumerate(articles):
    #print(f'{x} {y["title"]}')

#for key,value in articles[0].items():
    #print(f"\n{key.ljust(15)} (value)")
column_names=['source', 'author', 'title', 'description', 'urlToImage', 'publishedAt', 'content']
df=pd.DataFrame(articles, columns=column_names)

df.to_csv('data3.csv')

newsapi=NewsApiClient(api_key='50c140da3c164aec9cec08cea8211189')
data=newsapi.get_everything(q='France', language='en', page_size=100)

articles=data['articles']

#for x, y in enumerate(articles):
    #print(f'{x} {y["title"]}')

#for key,value in articles[0].items():
    #print(f"\n{key.ljust(15)} (value)")
column_names=['source', 'author', 'title', 'description', 'urlToImage', 'publishedAt', 'content']
df=pd.DataFrame(articles, columns=column_names)

df.to_csv('data4.csv')

newsapi=NewsApiClient(api_key='50c140da3c164aec9cec08cea8211189')
data=newsapi.get_everything(q='Germany', language='en', page_size=100)

articles=data['articles']

#for x, y in enumerate(articles):
    #print(f'{x} {y["title"]}')

#for key,value in articles[0].items():
    #print(f"\n{key.ljust(15)} (value)")
column_names=['source', 'author', 'title', 'description', 'urlToImage', 'publishedAt', 'content']
df=pd.DataFrame(articles, columns=column_names)

df.to_csv('data5.csv')

newsapi=NewsApiClient(api_key='50c140da3c164aec9cec08cea8211189')
data=newsapi.get_everything(q='Russia', language='en', page_size=100)

articles=data['articles']

#for x, y in enumerate(articles):
    #print(f'{x} {y["title"]}')

#for key,value in articles[0].items():
    #print(f"\n{key.ljust(15)} (value)")
column_names=['source', 'author', 'title', 'description', 'urlToImage', 'publishedAt', 'content']
df=pd.DataFrame(articles, columns=column_names)

df.to_csv('data6.csv')


#data1 = pd.read_csv('India.csv')
#data2 = pd.read_csv('US.csv')
#data3 = pd.read_csv('China.csv')
#data4 = pd.read_csv('France.csv')
#data5 = pd.read_csv('Germany.csv')
#data6 = pd.read_csv('Russia.csv')

#df_outer=pd.merge(data1, data2, data3, data4, data5, data6, on='sno', how='outer')

#print(df_outer.tail())


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8')