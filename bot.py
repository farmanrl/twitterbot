import tweepy # for tweeting
import secrets # shhhh
from book_manager import BookManager # for getting sentences out of our book file
from nltk.sentiment import SentimentAnalyzer

def get_next_chunk():
  # open text file
  book = BookManager()
  first_sentence = book.first_sentence()
  # tweet the whole sentence if it's short enough
  if len(first_sentence) <= 137:
    chunk = first_sentence
  # otherwise just print the first 140 characters
  else:
    chunk = first_sentence[0:137]
  # delete what we just tweeted from the text file
  book.delete_message(chunk)
  chunk = chunk.strip() + get_sentiment(chunk)
  print(chunk)
  return chunk

def get_sentiment(string):
  pos = 1
  neg = 0
  if pos > neg:
    response = ' :)'
  else:
    response = ' :('
  return response

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message {}".format(message))
  api.update_status(status=message)

if __name__ == '__main__':
  tweet(get_next_chunk())
