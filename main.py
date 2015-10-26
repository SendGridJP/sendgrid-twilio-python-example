import os
import urllib.parse
from flask import Flask, request
from twilio.rest import TwilioRestClient

app = Flask(__name__)

def voice_address(text_address):
  return text_address. \
    replace('<',' '). \
    replace('>',' ')

@app.route ('/')
def index():
  return 'Hello!'

@app.route ('/incoming', methods =['POST'])
def forward_to_twilio():
  sender  = voice_address(request.form['from'])
  subject = request.form['subject']
  body    = request.form['text']

  twiml = \
    '<Response><Say voice="alice" language="ja-jp">' + \
    'メールを受信しました。送信者は、' + sender + \
    '、です。件名は、' + subject + \
    '、です。本文は、' + body + \
    '、です。</Say></Response>'
  echo_url = "http://twimlets.com/echo?Twiml=" + urllib.parse.quote(twiml)
  print(echo_url)

  try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token  = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ['TWILIO_PHONE_NUMBER']
    to_number   = os.environ['YOUR_PHONE_NUMBER']

    client = TwilioRestClient(account_sid, auth_token)
    call = client.calls.create(
      from_ = from_number,
      to = to_number,
      url = echo_url)
    print(call.sid)
    return 'OK'
  except Exception as e:
    print(e)
    return 'NG'

if __name__=='__main__':
  app.run()
