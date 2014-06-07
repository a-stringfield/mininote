from flask import Blueprint

api_requests = Blueprint('api_requests', __name__)

import app.api.routes