# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"
    if request.method == 'GET':
        return "service up!"

if __name__ == '__main__':
    app.run(ssl_context='adhoc')