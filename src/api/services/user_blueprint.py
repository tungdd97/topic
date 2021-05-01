from src.api.uri import URI
from src.api import build_response_susccess, try_catch_error
from flask import Blueprint
from src.controllers.user_controller import UserController

user_mod = Blueprint(__name__, __name__)


@user_mod.route(URI.LOGIN, methods=["POST"])
def login():
    return UserController.login()


@user_mod.route(URI.REGISTER, methods=["POST"])
def register():
    return UserController.register()


@user_mod.route(URI.CHANGE_PASSWORD, methods=["POST"])
def change_password():
    return UserController.login()
