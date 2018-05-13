#!/home/pi/miniconda3/envs/ml/bin/python

from gevent.pywsgi import WSGIServer
from cat_server import app

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
