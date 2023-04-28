"""
About:    Twitter is a platform where people share their thoughts and opinions           about various financial topics, and evidence has shown that                    impactful outcomes to company stock have shifted simply due to an              influential tweet. We were inspired to create a sentiment analysis             flask app that can provide a more objective view of the conversation           by analyzing the sentiment of tweets that relate to these financial            topics and providing users with an overall "public opinion" of a               company ranging from positive, negative, or neutral. This can be               useful for individuals who want to understand the public's                     perception of a potential investment.

Devlopers: Bhuvan Biju, Chirag Singh, Long Do, Michael Clark
"""

import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
from textblob import TextBlob
from langdetect import detect
"""All neccessary variables"""

limit = 100
"""--------------------"""


def get_sentiment(text):
  blob = TextBlob(text)
  return blob.sentiment.polarity


def clean_tweet(tweet):
  # Remove URLs
  tweet = re.sub(r'http\S+', '', tweet)
  tweet = re.sub(r'www\S+', '', tweet)

  # Remove user mentions
  tweet = re.sub(r'@\w+', '', tweet)

  # Remove hashtags
  tweet = re.sub(r'#\w+', '', tweet)

  # Remove special characters and digits
  tweet = re.sub(r'[^\w\s]', '', tweet)
  tweet = re.sub(r'\d+', '', tweet)

  # Remove extra white spaces
  tweet = ' '.join(tweet.split())
  return tweet


def filter_english(tweet):
  lang = detect(tweet)
  if lang == 'en':
    return True
  else:
    return False


def sentiment_to_label(sentiment_score):
  if sentiment_score > 0:
    return 1
  elif sentiment_score == 0:
    return 0
  else:
    return -1


def main_func(query):
  tweets = []
  for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
      break
    else:
      tweets.append([tweet.date, tweet.username, tweet.content])
  df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
  
  df['Sentiment'] = df['Tweet'].apply(get_sentiment)
  df['Clean_Tweet'] = df['Tweet'].apply(clean_tweet)

  lol = df[['User', 'Clean_Tweet', 'Sentiment']].values[:10].tolist()

  avg_sentiment = df['Sentiment'].mean()
  df['Sentiment'] = df['Sentiment'].apply(sentiment_to_label)

  positive = (df['Sentiment'] == 1).sum()
  negative = (df['Sentiment'] == -1).sum()
  neutral = (df['Sentiment'] == 0).sum()

  lol.append(avg_sentiment)
  lol.append(positive)
  lol.append(negative)
  lol.append(neutral)
  return lol
    
