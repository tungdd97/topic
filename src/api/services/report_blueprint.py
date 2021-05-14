from src.api.uri import URI
from flask import Blueprint
from src.controllers.report_controller import ReportController

report_mod = Blueprint(__name__, __name__)


@report_mod.route(URI.REPORT, methods=["GET"])
def report():
    return ReportController.report()
