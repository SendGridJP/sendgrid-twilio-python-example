# SendGrid :heart: Twilio Python Example

電話でメールを読みあげるPython 3のサンプルコードです。

[SendGrid](https://sendgrid.kke.co.jp/)の[Parse Webhook](https://sendgrid.kke.co.jp/docs/API_Reference/Webhooks/parse.html)からPOSTされた内容を、[Twilio](http://twilio.kddi-web.com/)の[音声通話API](https://jp.twilio.com/docs/api/rest/making-calls)に橋渡しします。

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## 紹介記事

TODO: Blog URL

## SendGridの設定

「SETTINGS > [Inbound Parse](https://app.sendgrid.com/settings/parse)」にて、Parse Webhookを設定します。
Parse Webhookは、指定HOSTのメールアドレスへ送信されたメールをパースして、その内容を指定URLにPOSTする機能です。

HOSTには、SendGridが開発用に用意している「bymail.in」ドメインにサブドメインを付加したものを入力します。  
ここで付加するサブドメインは、一意なものであればなんでも構いませんが、ユーザ名の@より前の部分を利用して「sgxxxxxx.bymail.in」のようにすることを推奨しています。
実際に使う宛先メールアドレスのローカルパートは何でも構いません。

URLには、受信したメールの内容をPOSTするURL「（デプロイ先URL）/incoming」を指定します。

## 環境変数

| 環境変数名 | 説明 |
| --- | --- |
| TWILIO_ACCOUNT_SID | TwilioのACCOUNT SID |
| TWILIO_AUTH_TOKEN | TwilioのAUTH TOKEN |
| TWILIO_PHONE_NUMBER | Twilioの国際電話番号 |
| YOUR_PHONE_NUMBER | お手持ちの電話の国際電話番号（日本の場合は81始まり） |

## 動作確認環境

| ファイル名 | 内容 |
| --- | --- |
| runtime.txt | Pythonのバージョン |
| requirements.txt | Pythonのライブラリとバージョン |
| Procfile | Webアプリケーションの起動コマンド |

## 参考元

- [Code Challenge: Listen to Incoming Emails with Twilio](https://sendgrid.com/blog/code-challenge-listen-incoming-emails-twilio/)
    - [GridTwil.py](https://gist.github.com/kunal732/1ce19f720a6ff0be2ea8)
