from app.api import api_requests
from flask import jsonify, abort


@api_requests.route('/about', methods=['GET'])
def get_info():
    info_about = {
    "name": "Mininote",
    "description": "RESTful web app for working with notes.",
    "version": "0.2 pre-alfa",
    "license": "MIT License (MIT)",
    "author": "A. Stringfield",
    "api_reference": "https://github.com/a-stringfield/mininote",
    }

    return jsonify({
        'success': True,
        'message': 'Mininote info.',
        'data': info_about
        })


@api_requests.route('/coffee', methods=['GET'])
def get_coffee():
    abort(418)