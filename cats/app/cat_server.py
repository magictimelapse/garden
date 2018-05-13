from flask import Flask
from flask import request,jsonify
import numpy as np
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
        #pred = np.array([[0.55,0.22]],np.float64)
        #pred = np.array([[1.63431e-07, 0.99999988]],np.float64)
        #pred = np.array([[1.63431e-07, 0.99999988]],np.float64)
        print("prediction (0: cats, 1: noCat: ")
        print(pred)
        probabilities = {'cats': float(pred[0][0]),'noCat': float(pred[0][1])}
        #probabilities = {'cats':1.63431e-07,'noCat':  0.99999988}
        print('probs:')
        print(probabilities)
        print("______")
        return jsonify(probabilities)
