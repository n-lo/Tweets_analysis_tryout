# Trying out various analytics on Tweets

This is a simple repository of my attempt at analysing Tweets. Data set used here is tweets relating to the Australia One Nation party over time.

### Files:  
db2df - script to retrieve data (tweets) from MongoDB into Python pandas dataframe  
onp_01_sentiment_afinn - sentiment measurement of tweets with weighted sentiment words from AFINN  
onp_02_wc - various word clouds of the tweets  
onp_03_topic_modelling - attempt at topic modelling, does not take into account of common phrases (this in next part)  
onp_04_topic_modelling_phrases - also topic modelling, but this time take into account of common phrases  

#### Note:
To view the interactive models in topic modelling, either  
1. use the html file version in Docs folder (if you know how to view html on GitHub rather than the source code), or  
2. simply goto https://n-lo.github.io/Tweets_analysis_tryout/ and follow the links there (recommeded).
