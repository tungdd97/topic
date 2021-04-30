from src.api.uri import URI
from flask import Blueprint
from src.controllers.report_controller import ReportWeeklyController

report_mod = Blueprint(__name__, __name__)


@report_mod.route(URI.REPORT_POINT, methods=["POST"])
def update_report_point(week):
    return ReportWeeklyController.get_report_by_week(week=week)

