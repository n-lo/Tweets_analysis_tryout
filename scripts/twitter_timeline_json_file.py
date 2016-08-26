"""
Download Twitter user timeline, then store in json file
(https://n-lo.github.io/Tweets_analysis_tryout/)
"""

# import use python 3 print() syntax
from __future__ import print_function
from builtins import *

import tweepy
import json

# query user id
uid = ''
# or query user screen name
uscn = 'user screen name'


# output filename
filename = 'user_timeline_' + uscn + '.json'


# Load in Twitter API credentials from a filed
# Each line is a key-value pair of the form: KEY_NAME:KEY
CREDENTIALS_PATH = '../keys.txt'

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

with open(CREDENTIALS_PATH) as f:
    for line in f:
        line = line.rstrip('\r\n').split(":")
        if line[0] == "CONSUMER_KEY":
            CONSUMER_KEY = line[1]
        elif line[0] == "CONSUMER_SECRET":
            CONSUMER_SECRET = line[1]
        elif line[0] == "ACCESS_TOKEN":
            ACCESS_TOKEN = line[1]
        elif line[0] == "ACCESS_TOKEN_SECRET":
            ACCESS_TOKEN_SECRET = line[1]

# Authenticating
auth1 = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth1, wait_on_rate_limit = True, wait_on_rate_limit_notify = True, retry_count=3, retry_delay=5,
                 retry_errors=set([401, 404, 500, 503]))

results = []
page_cnt = 0

# query by page, better than by items (tweets) due to 
# API calls limit is 180, also note that Tweets limit on timeline is 3200
for page in tweepy.Cursor(api.user_timeline, screen_name = uscn, count = 100, include_rts = 1).pages(179):
    page_cnt += 1
    print("Query page %d" % page_cnt)
    for tweet in page:
        results.append(tweet._json)


print("%d Tweets retrieved." % len(results))
print("Page count: %d" % page_cnt)


# Create a file to append data
print("Writing data to file...")
with open(filename, 'w', encoding="utf-8") as fout:
    for i in results:
        fout.write(unicode(json.dumps(i, ensure_ascii = False)))
        fout.write(unicode("\n"))

fout.close()

print("Data written to file %s" % filename)