# GAE Technote - Telegram Bot and GAE

This technote shows a basic Telegram Bot implementation - yet another echo test bot app. The included sample uses the approach referred from Telegram API as *webhooks*. This project depends on the Python third-party library named 'python-telegram-bot'.

With this approach (*webhooks*), your code will need to establish a configuration step with the Telegram API in order to setup the web hook. Once the referred web hook is setup, your remote Telegram Bot handler, on the Telegram server end, will always send an HTTP POST message on your end, therefore enabling you to receive all incoming messages from an user chat session.

## Local install to the lib - optimizing for GAE

In orther to use the Telegram
https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27

```
# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
```

## Install local lib

```
pip install -t lib/ python-telegram-bot
```

## Mac OSX troubleshooting for pip local lib install (pip -t)

With MAC OS X you may stumble in a problem when installing local pip libraries. If so, check this [thread about a known issue with pip and a work around](https://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both). This was my case so I had to "vi ~/.pydistutils.cfg" with the following config values:

```
#[install]
#prefix=
```

## Code

See whole sample [here](https://github.com/taboca/gae-telegram-bot-simple/blob/master/telegram-python.py). First, we need to start via making the necessary authentication with Telegram API:

```
import config
bot = telegram.Bot(config.token)
```

Your config file will need to have the token from Telegram's Bot Father which is their human interface for initial bot setup — you can get the token from [Bot Father](https://telegram.me/BotFather).

Enable an end-point handler in your webapp, so you can call it from your own browser and establish the initial config for web hook method to work:

```
app = webapp2.WSGIApplication([
    ('/config_setWebhook' , set_webhook ),
], debug=True)
```

The end-point implementation establishes a connection with the bot handler on Telegram's end using "bot.setWebhook" API. Notices that you will need to pass your public end-point web hook address:

```
class set_webhook(webapp2.RequestHandler):
  def get(self):

    strResult = 'Configuration failed..'

    ok = bot.setWebhook('https://MYAPPDOMAIN/telegram_post_hook')
    if ok:
        strResult = "Configuration for webhook 'telegram_post_hook' ok"

    self.response.out.write(strResult)
```

Now, you should add the referred (telegram_post_hook) end-point so Telegram's remote server can call you for all incoming messages:

```
app = webapp2.WSGIApplication([
    ('/config_setWebhook' , set_webhook ),
    ('/telegram_post_hook', webhook_handler) # Actually should be called from Telegram
], debug=True)
```

The implementation of it, in our limited sample, will just send back the same text:

```

class webhook_handler(webapp2.RequestHandler):
  def post(self):

    if self.request.method == "POST":

        body = json.loads(self.request.body)

        update  = telegram.Update.de_json(body, bot)
        chat_id = update.message.chat.id
        text    = update.message.text.encode('utf-8')
        bot.sendMessage(chat_id=chat_id, text=text)

    self.response.out.write('ok')
```


## References

* [setWebhook method](https://core.telegram.org/bots/api#setwebhook)
* [Python Telegram Bot Library (python-telegram-bot)](https://github.com/python-telegram-bot/python-telegram-bot)
