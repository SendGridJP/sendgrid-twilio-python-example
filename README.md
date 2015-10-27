# SendGrid :heart: Twilio Python Example

電話でメールを読みあげるPython 3のサンプルコードです。

[SendGrid](https://sendgrid.kke.co.jp/)からPOSTされた内容を、[Twilio](http://twilio.kddi-web.com/)の[音声通話API](https://jp.twilio.com/docs/api/rest/making-calls)に橋渡します。

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## 紹介記事

TODO: Blog URL

## SendGrid設定

「SETTINGS > [Inbound Parse](https://app.sendgrid.com/settings/parse)」にて、Parse Webhookを設定します。

HOSTには、宛先メールアドレスのドメインを指定します。
通常は宛先ドメインのDNSにMXレコードを登録する必要がありますが、SendGridが開発用に用意している「bymail.in」ドメインを利用するとこの手順を省くことができます。
この場合、「sgxxxxxx.bymail.in」のようにサブドメインを付加したものを入力します。
ここで付加するサブドメインは、一意なものであればなんでも構いませんが、ユーザ名の@より前の部分を利用することを推奨しています。

URLには、受信したメールの内容をPOSTするURL「（デプロイ先URL）/incoming」を指定します。

## 環境変数

| 環境変数名 | 説明 |
| --- | --- |
| TWILIO_ACCOUNT_SID | TwilioのACCOUNT SID |
| TWILIO_AUTH_TOKEN | TwilioのAUTH TOKEN |
| TWILIO_PHONE_NUMBER | Twilioの国際電話番号 |
| YOUR_PHONE_NUMBER | 手持ちの国際電話番号（日本の場合は81始まり） |

## 動作確認環境

| ファイル名 | 内容 |
| --- | --- |
| runtime.txt | Pythonのバージョン |
| requirements.txt | Pythonのライブラリとバージョン |
| Procfile | Webアプリケーションの起動コマンド |

## 参考元

- [Code Challenge: Listen to Incoming Emails with Twilio](https://sendgrid.com/blog/code-challenge-listen-incoming-emails-twilio/)
    - [GridTwil.py](https://gist.github.com/kunal732/1ce19f720a6ff0be2ea8)
