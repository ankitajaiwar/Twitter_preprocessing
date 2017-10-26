import pandas as pd
import sys
import csv

url = 'https://raw.githubusercontent.com/hkundnani/TSA/master/data/twitter_feeds_apple_processed.csv'
    
chipo = pd.read_csv(url, sep = "[,]", header = 0, engine = 'python')



x = chipo.head(10)

print x

y = chipo.info

print y

z = chipo.columns

print z

tweets = chipo.iloc[:,3]

print tweets
tweets.to_csv("tweetsonly.csv")