import os
import sys
from twilio.rest import Client

account_sid = "ACf91e60bf6394982df564444b5db4c508"
auth_token  = "59bb2da30e29d7414d9d629f3d73f3ee"

client = Client(account_sid, auth_token)

if(len(sys.argv) != 3):
	print "Error"
	sys.exit()

data = sys.argv[1]
userPhone = sys.argv[2]
message = client.messages.create(
	to="+1" + userPhone,
	from_="+18622197472",
	body=data)

print "SMS sent to " + userPhone;
