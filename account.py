class Account(object):

    def __init__(self, name, number,  fb):
        self.name = name
        self.numer = number
        self.fb = fb

    def addTwitter(self, twitter):
        self.twitter = twitter

    def addInsta(self, insta):
        self.insta = insta
