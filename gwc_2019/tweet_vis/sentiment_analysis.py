import json
from textblob import TextBlob
import matplotlib.pyplot as plt
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#Create a Sentiment List
polarityList = []
#[OPTIONAL] Subjectivity
subjectivityList = []

#Get Sentiment Data
for tweet in tweetData:
	tweetblob = TextBlob(tweet["text"])
	polarityList.append(tweetblob.polarity)
#[OPTIONAL] Subjectivitys
	subjectivityList.append(tweetblob.subjectivity)
#Create the Graph
plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()
#[OPTIONAL] Subjectivity
plt.plot(polarityList, subjectivityList, 'ro')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('Tweet Polarity vs Subjectivity')
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()
