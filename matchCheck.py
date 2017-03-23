#!/usr/bin/env python

from fuzzywuzzy import fuzz 
from twilio.rest import TwilioRestClient
import config

account_sid = config.account_sid # Your Account SID from www.twilio.com/console
auth_token  = config.auth_token  # Your Auth Token from www.twilio.com/console

data = open("out.txt").readline().rstrip()

result = fuzz.ratio(data, config.postcode)

if result > 80:
	print("match, sending text")
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(to=config.to, from_=config.from_,
                                     body="You may have won the Free Postcode Lottery: " + config.fpc_url)
else:
	print("no match")
