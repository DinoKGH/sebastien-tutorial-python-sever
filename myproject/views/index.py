# -*- coding: utf-8 -*-

from flask import Flask, make_response
from flask import request, redirect, url_for, render_template, flash
from myproject import app
import json
from myproject.views import code

@app.route('/test', methods=['GET', 'POST'])
def test():
  if request.method == 'POST' and 'application/json' in request.headers.get('Content-Type', ""):
    event = request.json
    response = make_response()
    response.status_code = 200

    texts = text_handler(event, "")
    response.data = json.dumps(texts, sort_keys=True, indent=4)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response
  else:
    return "test"

def text_handler(event, context):

  print(event["args"], type(event["args"]))

  utterance = event["args"]["utterance"]
  intent = event["args"]["intent"]
  slot = {}
  for key, value in event["args"].items():
      print(key, value)
      if key == u'intent':
          pass
      elif key == u'utterance':
          pass
      else: slot[key]=value

  sentence = code.text(utterance, intent, slot)

  return {
      "error_code": "success",
      "status": "true",
      "user_id": event["user_id"],
      "bot_id": event["bot_id"],
      "params": {"status": "true",
                 "message": sentence
                 }
      }
