from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        #return "Webhook received!"
        return request.json
    if request.method == 'GET':
        return "service up test!"