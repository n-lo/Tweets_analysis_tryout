Recently I have started to look into the collection and analysis of Tweets, and getting familiar with a couple of the popular natural language processing libraries in Python (and R later on), here is a repository of the scripts.  
There are two main data sets I have collected so far, one is Tweets relating to the Australian One Nation party over two weeks time in August, about six weeks after the Federal Election 2016; second data set contains Tweets regarding to the space exploration computer/video game - No Man's Sky, shortly before and after the release.  

**With One Nation party data set**  
**Part 1:** [sentiment measurement](http://htmlpreview.github.io/?https://github.com/n-lo/Tweets_analysis_tryout/blob/master/docs/onp_01_sentiment_afinn.html)  
**Part 2:** [word clouds](http://htmlpreview.github.io/?https://github.com/n-lo/Tweets_analysis_tryout/blob/master/docs/onp_02_wc.html)  
**Part 3:** [topic modelling](http://htmlpreview.github.io/?https://github.com/n-lo/Tweets_analysis_tryout/blob/master/docs/onp_03_topic_modelling.html)  
**Part 4:** [topic modelling with phrases](http://htmlpreview.github.io/?https://github.com/n-lo/Tweets_analysis_tryout/blob/master/docs/onp_04_topic_modelling_phrases.html)  

**With No Man's Sky data set**  
[Sentiment measurement](http://htmlpreview.github.io/?https://github.com/n-lo/Tweets_analysis_tryout/blob/master/docs/nms_sentiment_afinn_mongo.html) shortly before and after release day.  

***
#### Extras:
[Search Twitter](https://github.com/n-lo/Tweets_analysis_tryout/blob/master/twitter_search_json_file.py) - search historical Tweets with keywords.  
[Timeline](https://github.com/n-lo/Tweets_analysis_tryout/blob/master/scripts/twitter_timeline_json_file.py) - download user's timeline.  
[Store data](https://github.com/n-lo/Tweets_analysis_tryout/blob/master/scripts/json_to_mongo.py) to MongoDB.  
[Database to data frame](https://github.com/n-lo/Tweets_analysis_tryout/blob/master/db2df.ipynb) - script to retrieve data (tweets) from MongoDB into Python pandas data frame.  

#### Next:  
Who's tweeting who (user group/cluster)?  
