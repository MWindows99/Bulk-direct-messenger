import tweepy

def main():
    # API Key
    consumer_key = "xxxx"
    consumer_secret = "xxxx"
    access_token = "xxxx"
    access_token_secret = "xxxx"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # LIST ID
    list_id = 1234567890
    # Direct Message
    message = "Hello, World!"
    
    for member in tweepy.Cursor(api.get_list_members, list_id=list_id).items()
        try:
            api.send_direct_message(member.id, message)
        except:
            pass
    
if __name__ == "__main__":
    main()
