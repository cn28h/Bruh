"""
  Retreives requested users latest tweet.
"""
from plugins.commands import command
from json import loads
from TwitterAPI import TwitterAPI


@command
def twitter(irc, nick, chan, msg, args):
    '''Retrieves requested users latest tweet'''
    
    if 'twitter' in irc.config['plugins']:
        consumer_key,consumer_secret,access_token_key,access_token_secret = irc.config['plugins']['twitter']['keys']
    else:
        return "Something went wrong"
	
    if not msg:
        return "Need a user to search for"
    
    try:
        request = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        request = request.request('statuses/user_timeline',{'screen_name':msg,'count':'1'})

        if request.status_code != 200:
            raise Exception("bad status code")

        # removing the first and last characters because they are [' ']'
        request = loads(request.text[1:-1])
        return "{}  -  https://twitter.com/{}/status/{}".format(request['text'],request['user']['name'],request['id'])
		
    except:
        return "Something went wrong"