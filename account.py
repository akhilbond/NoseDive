class Account(object):

    def __init__(self, name, number,  fb):
        self.name = name
        self.number = number
        self.fb = fb
        self.twitter = ''
        self.insta = ''

    def addTwitter(self, twitter):
        self.twitter = twitter

    def addInsta(self, insta):
        self.insta = insta
