from flask import Blueprint

web_interface = Blueprint('web_interface', __name__, template_folder='templates', static_folder='static')

import app.web.routes