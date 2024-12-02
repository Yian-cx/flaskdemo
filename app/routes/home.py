from flask import Blueprint

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
def index():
    return "Welcome to the Home Page"
