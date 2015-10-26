# SendGrid :heart: Twilio Python Example

電話でメールを読みあげるPython 3のサンプルコードです。

[SendGrid](https://sendgrid.kke.co.jp/)の[Parse Webhook](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/parse.html)で受信したメールを、[Twilio](http://twilio.kddi-web.com/)で[音声通話](https://jp.twilio.com/docs/api/rest/making-calls)してもらいます。

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## 解説

TODO: Blog URL

## 環境変数

| 環境変数名 | 説明 |
| --- | --- |
| TWILIO_ACCOUNT_SID | TwilioのACCOUNT SID |
| TWILIO_AUTH_TOKEN | TwilioのAUTH TOKEN |
| TWILIO_PHONE_NUMBER | Twilioの国際電話番号 |
| YOUR_PHONE_NUMBER | 手持ちの国際電話番号（日本の場合は81始まり） |

## 動作確認環境

次のファイルを参照してください。

- runtime.txt
- requirements.txt
- Procfile

## 参考元

- [Code Challenge: Listen to Incoming Emails with Twilio](https://sendgrid.com/blog/code-challenge-listen-incoming-emails-twilio/)
    - [GridTwil.py](https://gist.github.com/kunal732/1ce19f720a6ff0be2ea8)
