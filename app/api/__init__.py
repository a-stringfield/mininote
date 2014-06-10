from flask import Blueprint

api_requests = Blueprint('api_requests', __name__)

import app.api.general
import app.api.notes
import app.api.users
import app.api.errors