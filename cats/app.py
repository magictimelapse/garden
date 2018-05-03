from flask import Flask
app = Flask(__name__)
import prediction

@app.route('/cat'):
def cat():



@app.route('/')
def hello_world():
        return 'Hello, World!'
