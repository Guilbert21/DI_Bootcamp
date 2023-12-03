from django.shortcuts import render
import tweepy

# API credidentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# authenticate API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def feedback(request):
    tweets = api.search(q='stock feedback.html', count = 10)
    context = {'tweets': tweets}
    return render(request, 'twitterapp/feedback.html', context)
