import tweepy # for tweeting
import secrets # shhhh
import requests
import json
import urllib
import xml.etree.ElementTree
from book_manager import BookManager # for getting sentences out of our book file

def get_next_chunk():
  # open text file
  book = BookManager()
  first_sentence = book.first_sentence()
  # tweet the whole sentence if it's short enough
  if len(first_sentence) <= 140:
    chunk = first_sentence
  # otherwise just print the first 140 characters
  else:
    chunk = first_sentence[0:140]

  # delete what we just tweeted from the text file
  book.delete_message(chunk)
  return chunk

def match_lyrics():
  data = requests.get('http://api.lololyrics.com/0.5/getLyric?artist=kanyewest&track=graduation')
  e = xml.etree.ElementTree.parse(data).getroot()
  print(e)

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message {}".format(message))
  api.update_status(status=message)

if __name__ == '__main__':
  tweet(match_lyrics())
