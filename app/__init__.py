from flask import Flask
from mongoengine import *

from app.api import api_requests
from app.web import web_interface

connect("mininote_test")


mininote = Flask(__name__)


mininote.register_blueprint(api_requests, url_prefix='/api')
mininote.register_blueprint(web_interface)



if __name__ == '__main__':
	mininote.run(host='127.0.0.1', port=5000, debug=True)