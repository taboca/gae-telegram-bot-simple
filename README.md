# GAE Technote - Telegram Bot and GAE

This technote shows a basic Telegram Bot implementation - the echo test. This sample uses the approach referred from Telegram API as *webhooks*. In the *webhooks* setup, first, your code will need to establish a config step with the API, to setup the web hook: The public end-point that is available on your end so Telegram bot can send an HTTP POST message to you for any new incoming messages from an user chat session.

With that initial setup, you are good to go, and any new messages from the chat should call your hook end point of choice.

## Local install to the lib - optimizing for GAE

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

## Mac OSX pip -t troubleshooting

With MAC OSX, vi ~/.pydistutils.cfg with the following contents uncommented.  This is based in https://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both which is solution based on this

```
#[install]
#prefix=
```

## References

* [setWebhook method](https://core.telegram.org/bots/api#setwebhook)
