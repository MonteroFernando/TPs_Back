from flask import Blueprint
from ..models.exceptions import FilmNotFound

errors=Blueprint('error',__name__)
@errors.app_errorhandler(FilmNotFound)
def handle_file_not_request(error):
    return error.get_response(), error.status_code

