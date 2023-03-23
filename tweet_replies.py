pip3 install snscrape

import snscrape.modules.twitter as sntwitter
import pandas as pd

# Define the tweet ID
tweet_id = '1634591545826344961'

# Define the query string to search for tweets in the conversation thread
query_string = f'conversation_id:{tweet_id} filter:replies'

# Scrape the tweets
tweets = []
for tweet in sntwitter.TwitterSearchScraper(query_string).get_items():
    tweets.append(tweet)

# Convert the results to a pandas DataFrame
df = pd.DataFrame(tweets)

# Export the results to a csv file
df.to_csv(f'{tweet_id}.csv', index=False, encoding='utf-8')
