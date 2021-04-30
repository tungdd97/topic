from src.api.uri import URI
from flask import Blueprint
from src.controllers.project_controller import ProjectController

project_mod = Blueprint(__name__, __name__)


@project_mod.route(URI.PROJECT, methods=["GET"])
def get_project():
    return ProjectController.get_all_project()


@project_mod.route(URI.PROJECT, methods=["POST"])
def add_project():
    return ProjectController.add_project()