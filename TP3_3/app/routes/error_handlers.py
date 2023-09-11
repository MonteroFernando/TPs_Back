from flask import Blueprint
from ..models.exceptions import FilmNotFound,InvalidDataError

errors=Blueprint('error',__name__)

@errors.app_errorhandler(FilmNotFound)
def handle_file_not_request(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data_error(error):
    return error.get_response(), error.status_code


