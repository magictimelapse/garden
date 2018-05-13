#!/home/pi/miniconda3/envs/ml/bin/python
import requests
import sys
if __name__=='__main__':
    filename = sys.argv[1]
    r =requests.post('http://localhost:8000/cat_detected',json={'filename':filename})
    print(r.json())

