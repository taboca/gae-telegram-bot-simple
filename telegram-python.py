#!/usr/bin/env python

import sys
import os
import telegram
import webapp2 

global bot

import config 

bot = telegram.Bot(config.token)

class webhook_handler(webapp2.RequestHandler):
  def post(self):

    if self.request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        text = update.message.text.encode('utf-8')
        bot.sendMessage(chat_id=chat_id, text=text)

    self.response.out.write(strResult)

class set_webhook(webapp2.RequestHandler):
  def get(self):
 
    strResult = 'Configuration failed..'

    ok = bot.setWebhook('https://bot-telegram-gae-test.appspot.com/telegram_post_hook')
    if ok:
        strResult = "Configuration for webhook 'telegram_post_hook' ok"
    
    self.response.out.write(strResult)


app = webapp2.WSGIApplication([
    ('/config_setWebhook' , set_webhook ),
    ('/telegram_post_hook', webhook_handler)
], debug=True)
