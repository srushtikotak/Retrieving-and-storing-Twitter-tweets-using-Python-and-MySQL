from __future__ import print_function
import tweepy
import json
import MySQLdb
import re
from dateutil import parser
 
WORDS = ['#Shahrukh','Hrithik'] #Any words you wish to tags(It can be a hashtag, username or any word)
 
CONSUMER_KEY = "Your Consumer Key"
CONSUMER_SECRET = "Your Consumer Secret"
ACCESS_TOKEN = "Your Access Token"
ACCESS_TOKEN_SECRET = "Your Access Token Secret"
 
HOST = "localhost"
USER = "root"
PASSWD = "********"
DATABASE = "Your Database name"
 
# This function takes the tweet_id, screen_name, created_at, text , filtered_text ,url , emoji ,token_text and stores it into a MySQL database

def store_data(tweet_id, screen_name, created_at, text , filtered_text ,url , emoji ,token_text):
    db=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8mb4")
    cursor = db.cursor()
    insert_query = "INSERT INTO twitter (tweet_id, screen_name, created_at, text , filtered_text ,url , emoji , token_text) VALUES (%s, %s, %s, %s, %s, %s, %s , %s )"
    cursor.execute(insert_query, (tweet_id, screen_name, created_at, text , filtered_text , url , emoji ,token_text))
    db.commit()
    cursor.close()
    db.close()
    return
 
class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API. 
 
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        try:
           # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #grab the wanted data from the Tweet
            text = datajson['text']
            screen_name = datajson['user']['screen_name']
            tweet_id = datajson['id']
            created_at = parser.parse(datajson['created_at']) 

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            token_text = text.split()
            text_without_url = re.sub(r"http\S+", "", text)
            url = re.findall(r'(https?://[^\s]+)', text)
            emoji =  re.findall(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])', text)
            #insert the data into the MySQL database
            store_data(tweet_id, screen_name, created_at, text , text_without_url , str(url) , str(emoji), str(token_text))

        except Exception as e:
           print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
