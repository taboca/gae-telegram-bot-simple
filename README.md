# GAE Technote - Telegram Bot and GAE

This technote shows a basic Telegram Bot implementation - yet another echo test bot app. The included sample uses the approach referred from Telegram API as *webhooks*. This project depends on the Python third-party library named 'python-telegram-bot'.

With this approach, first, your code will need to establish a configuration step with the Telegram API in order to setup the web hook. Once the referred web hook is setup, your remote Telegram Bot handler, on the Telegram server end, will always send an HTTP POST message on your end, therefore enabling you to receive all incoming messages from an user chat session.

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



## References

* [setWebhook method](https://core.telegram.org/bots/api#setwebhook)
* [Python Telegram Bot Library (python-telegram-bot)](https://github.com/python-telegram-bot/python-telegram-bot)
