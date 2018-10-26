'''
TASK:
A list of Subreddits and search terms
A function to call Reddit's API (pass in subreddit)
A function to process reddit's results (search for search terms, returns positives)
A function that calls reddit's API for each subreddit in our list
A function that calls Twilios API to send a Text with matching results
'''

import praw




def call_reddit(subreddit_name):

	subreddit_name = str(subreddit_name)

	reddit = praw.Reddit(

		client_id		= '_VLlkPOoDXoaPQ',
	    client_secret	= 'c5jO1y_wSigePj1NE0aG-vjQcag',
	    password		= 'chrisPractice2018',
	    user_agent		= 'testscript by /u/chrisPractice2018',
	    username		= 'chrisPractice2018'

	    )


	subreddit = reddit.subreddit(subreddit_name)

	return subreddit






hot_post = call_reddit('forhire').hot(limit = 5)


for submition in hot_post:
	print (submition)