# Tweet collector via tweepy and user-supplied search terms,
# to be used with CloudFormation template
# based on http://badhessian.org/2012/10/collecting-real-time-twitter-data-with-the-streaming-api/
# with modifications by http://github.com/marciw

from twaiter import TWaiter
import tweepy, sys, twitterparams
from cities import *

# authentication params (supplied via cfn)
consumer_key = twitterparams.OAuthConsKey
consumer_secret = twitterparams.OAuthConsSecret
access_token = twitterparams.OAuthToken
access_token_secret = twitterparams.OAuthTokenSecret

# OAuth via tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():

    collection = 'tweets'
    waiter = TWaiter(api, collection)

    print "Collecting tweets. Please wait."

    try:
        stream = tweepy.Stream(auth, waiter)
	stream.filter(track = cities_filter)
    except Exception, e:
        print "An error occurred. No tweets collected.", e
        stream.disconnect()


if __name__ == '__main__':
    main()
