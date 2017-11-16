# GAE Technote - Telegram Bot and GAE

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
