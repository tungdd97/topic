from src.api.uri import URI
from src.api import build_response_susccess, try_catch_error
from flask import Blueprint
from src.controllers.contact_controller import ContactController

contact_mod = Blueprint(__name__, __name__)


@contact_mod.route(URI.CONTACT, methods=["POST"])
@try_catch_error
def contact():
    return ContactController.send_contact_bean()
