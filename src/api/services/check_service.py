from src.api.uri import URI
from src.api import build_response_susccess, try_catch_error
from flask import Blueprint

check_service_mod = Blueprint(__name__, __name__)


@check_service_mod.route(URI.PING, methods=["GET"])
@try_catch_error
def check_service():
    return build_response_susccess("request successful!!!")
