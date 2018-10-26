'''
TASK:
A list of Subreddits and search terms
A function to call Reddit's API (pass in subreddit)
A function to process reddit's results (search for search terms, returns positives)
A function that calls reddit's API for each subreddit in our list
A function that calls Twilios API to send a Text with matching results
'''

import praw
from twilio.rest import Client



# 1 ###########################################################################

subreddits_list = ['forehire','forehire2','freelance']



# 2 ###########################################################################

# A function to call Reddit's API 
# with passed in subreddit name as argument 
def call_reddit(subreddit_name):

	# Notice the imported PRAW at the biggining of this script,
	# in order to use PRAW, the following 5 pieces of information
	# are required.
	reddit = praw.Reddit(

		client_id		= '_VLlkPOoDXoaPQ',
	    client_secret	= 'c5jO1y_wSigePj1NE0aG-vjQcag',
	    password		= 'chrisPractice2018',
	    user_agent		= 'testscript by /u/chrisPractice2018',
	    username		= 'chrisPractice2018'

	    )


	subreddit = reddit.subreddit(subreddit_name)

	return subreddit




# 3 #############################################################################

# This function process search results according to the matching keyword 
# passed as an argument.
def process_results(func, number_of_results, term_to_look_for):


	new_post = func.new(limit = number_of_results)



	# this is where is the issue, this comprehension list is not working properly
	# it's not returning the number of posts requested
	posting_list = [

	submission.title for submission in new_post if not submission.stickied 

	] 



	filtered_by_terms = [ 

	each_title for each_title in posting_list if term_to_look_for in each_title

	]



	return filtered_by_terms



# TEST
# print(process_results(call_reddit('forehire'),50,'[Hiring]'))




# 4 ###############################################################################

# This function call each subreddit in the given list
def call_subreddits_list(names_list):

	called_subreddits = map(call_reddit, subreddits_list)

	return list(called_subreddits)




# 5 ###############################################################################

# This function call Twilio API
def call_twilio():
	
	account_sid = 'ACf7e44e9a6566ffc16a3b9dbb40b3ea08'
	auth_token = '425aa3e13fe91eb3cbcaf2602dd37f41'
	client = Client(account_sid, auth_token)

	return client

