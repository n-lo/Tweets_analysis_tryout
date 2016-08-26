"""
Read in Tweets from json file, and store into MongoDB
(https://n-lo.github.io/Tweets_analysis_tryout/)
"""

from __future__ import print_function
import json
from pymongo import MongoClient

# stored Tweets data
json_filename = "tweets.json"

try:
    json_file = open(json_filename, "r")
except ValueError:
    print("Cannot open file!")

client = MongoClient('localhost', 27017)
db = client.collections

for line in json_file:
    try:
        data = json.loads(line)
        db.tweets.insert_one(data)
    except BaseException, e:
        print("Error!", str(e))
        client.close()

client.close()
