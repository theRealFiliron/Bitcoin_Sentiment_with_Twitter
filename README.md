Twitter Sentiment

The goal of my project was to use the Unix Tools and a couple of Python scripts to create a pipeline of commands that automatically retrieves tweets relating to a specific search term from Twitter’s API and then analyzes the sentiment of those tweets. Ultimately, this allows us to track the Twitter sentiment related to a specific search term over time. If we track the Twitter sentiment relating to traded assets like currencies or stocks, we can then attempt to determine whether there is a correlation between the Twitter sentiment and the specific asset.
Unfortunately, this paper will be limited to a rather general “proof of concept,” since we do not have enough time to test our program and get enough data to draw accurate and interesting conclusions. Hopefully, I will be able to replace this paragraph in the Fall semester, when we will have a few months’ worth of data!

Step 1: Retrieving the tweets and measuring sentiment with Python’s vader library
	In this step, we focus on retrieving and cleaning the tweets, the sentiment analysis is entirely performed by vader.
We want to keep track of the current date, which we will use to track the sentiment. We use the Unix tools “date” and “sed” to get the date is a nice format. We then pass the text stream as an argument to our Python script, which measures sentiment and adds a line to our “sentimentTracker.txt” file with the current date and the current sentiment. This is all done by “date.sh” (1), which modifies the run.sh (2) script with the current time and date.
The Python script (3), when executed, uses the tweepy library to authenticate to Twitter’s API and retrieve 3,500 tweets. We store these tweets in a text file and then “clean” them. Before feeding the tweets to vader, we want to remove links, special characters (‘RT’ or ‘\n’ for example), tags… To do this, we use the python module re, which allows us to make the desired modifications using Unix commands. Finally, we feed the cleaned string containing all the tweets into vader, which measures the sentiment.
Finally, we use the Unix watch command to perform this task every X minutes (4).






Step 2: Let’s try our own sentiment analysis!
	Although using modules like vader is nice and simple, it’s also interesting to build a model from scratch. In order to build our own model for sentiment analysis, we first need to find a dataset with labeled tweets. The dataset that I chose is called Sentiment140 (5) and can be found here: http://help.sentiment140.com/. The dataset essentially consists of 1,600,000 entries with the cleaned text of the tweet and the sentiment score (0 for negative and 4 for positive).
After splitting our dataset into a training set and a test set, the idea is to create a bag of n unique words (or tokens) and then represent each tweet as a vector of length n of 0s and 1s. For this, we use sklearn’s built-in tools. We also choose to fit a logistic regression model, since the target variables are either 0 or 4 (binary classification problem).
However, we run into some issues when we attempt to use sklearn’s functions. This is because the UTF-8 encoding is inconsistent in the dataset. In fact, if we attempt to use the Unix tool “sed,” we also encounter some issues. But we can still use the Unix tools to fix this problem! First, we notice that attempting to capture the second character in each line with sed will show us which lines are not troublesome. Then, we use cat -n, sort, and join in a makefile to solve the problem by deleting the troublesome lines (6).
Finally, we can now fit our own model using sklearn’s logistic regression (7).



Step 3: Track Bitcoin Price (for example)
	While we can always go back and download past prices, we can also track asset prices in real time with wget, as in bitcoin.sh (8).


We leave the statistical part of this project to the Fall semester, when we will have more data.


