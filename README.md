# GAE Technote - Telegram Bot and GAE

This technote shows a basic Telegram Bot implementation - yet another echo test bot app. The included sample uses the approach referred from Telegram API as *webhooks*.

With this approach, first, your code will need to establish a configuration step with the Telegram API in order to setup the web hook. Once the referred web hook is setup, your remote Telegram Bot handler, on the Telegram server end, will always send an HTTP POST message on your end, therefore enabling you to receive all incoming messages from an user chat session.

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
