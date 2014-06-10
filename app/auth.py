from flask import abort
from flask.ext.httpauth import HTTPBasicAuth
from hashlib import md5
from app import model


login = HTTPBasicAuth()


@login.get_password
def get_pw(username):
    if model.User.objects(username=username):
        return model.User.objects(username=username)[0].password_hash
    return None

@login.hash_password
def hash_pw(password):
    return str(md5(password.encode()).hexdigest())


@login.error_handler
def auth_error():
    return abort(401)