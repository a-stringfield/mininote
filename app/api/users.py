from flask import request, jsonify
from datetime import datetime
from hashlib import md5
from app.api import api_requests
from app import model

@api_requests.route('/user', methods=['POST'])
def add_user():
    model.User(username=request.json['username'],
        password_hash=str(md5((request.json['password']).encode()).hexdigest()),
        register_date=datetime.now()).save()

    return jsonify({
        'success': True,
        'message': 'User was added.',
        'data': None
        })
