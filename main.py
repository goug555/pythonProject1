import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("YMvDElA0XtM1Pb4Ip0ea1xBFR",
    "0XhPUQipkcwvJnStn6KxKhEiunGTP9KI4Ou7JzZ8BCOX33jVW5")
auth.set_access_token("1237052598286528513-tnD0D0WlM6o1F8YgK2qJ5ktzbIdrbG",
    "OXu388xkmTljxjGrsyDHJoBL2nopAgb")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")