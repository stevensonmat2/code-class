import os
from twilio.rest import Client

account_sid = 'AC86189c370a1fcca6c3dd11c2fa15ee04'
auth_token = '1769e4656916ec050cdbe4e58d17e6c1'
client = Client(account_sid, auth_token)
number = []

day_numbers = ['+18067860264','+19713209937', '+15039808649', '+15038884575', '+19724153532', '+19724156381']

for number in day_numbers:
    message = client.messages.create(to=number, from_="+14243512633", body="Look Up!")
    print("Sent to {}".format(number))
#
# client = Client(account_sid, auth_token)
#
# client.messages.create(
#     to=os.environ['+2524322144'],
#     from_="+2524322144",
#     body='hotdog'
# )




