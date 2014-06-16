from flask import jsonify
from app.api import api_requests


@api_requests.errorhandler(400)
def bad_request(e):
    return jsonify({
        'success': False,
        'message': 'Error 400: Bad request.',
        'data': None
        }), 400


@api_requests.errorhandler(401)
def not_authorized(e):
    return jsonify({
        'success': False,
        'message': 'Error 401: You must be authorized.',
        'data': None
        }), 401


@api_requests.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'success': False,
        'message': 'Error 404: Not found.',
        'data': None
        }), 404


@api_requests.errorhandler(413)
def too_long(e):
    return jsonify({
        'success': False,
        'message': 'Error 413: One of request fields is too long.',
        'data': None
        }), 413


@api_requests.errorhandler(418)
def teapot(e):
    return jsonify({
        'success': False,
        'message': 'Error 418: I am a teapot.',
        'data': None
        }), 418