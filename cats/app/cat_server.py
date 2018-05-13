from flask import Flask
from flask import request,jsonify

app = Flask(__name__)
import apply_model
@app.route('/')
def hello_world():
        return 'Hello, World!'

@app.route('/cat_detected',methods=['POST'])
def cat_detected():
        content = request.get_json()
        print (content)
        filename = content['filename']
        print("predict...")
        pred = apply_model.predict(filename)
        print("prediction (0: cats, 1: noCat: ")
        print(pred)
        return jsonify(pred)
