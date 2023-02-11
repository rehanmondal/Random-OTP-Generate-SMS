import random
from twilio.rest import Client

SID = " ## YOUR API KEY ##"
AUTH_TOKEN = '##    YOUR AUTHENTICATION TOKEN    ##'

# OTP Generation
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spec = '!@#$%^&*()_/|'
number = '0123456789'
pass_char = lower + upper + number + spec
pass_len = 8

OTP = "".join(random.sample(pass_char,pass_len))
print("\nOTP for login to your account : ",OTP)

# SMS sending using twilio  API

var = Client(SID,AUTH_TOKEN)
var.messages.create(body=(f'One time PASSWORD for login to your account is {OTP},valid for 45 secs'),from_='## YOUR TWILIO ACCOUNT DUMMY NUMBER ##',to='+91 ##NUMBER OF PERSON TO WHOM YOU WANT TO SENDMESSAGE##')
