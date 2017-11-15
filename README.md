## Local install to the lib - optimizing for GAE 

With MAC OSX, vi ~/.pydistutils.cfg with the following contents uncommented.  This is based in https://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both which is solution based on this https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27 

```
#[install]
#prefix=
```

## Install local lib 

```
pip install -t lib/ python-telegram-bot
```
