from src.api.uri import URI
from flask import Blueprint
from src.controllers.report_weekly_controller import ReportWeeklyController

report_weekly_mod = Blueprint(__name__, __name__)


@report_weekly_mod.route(URI.REPORT_WEEKLY, methods=["GET"])
def get_report_weekly(week):
    return ReportWeeklyController.get_report_by_week(week=week)


@report_weekly_mod.route(URI.REPORT_WEEKLY_DETAIL, methods=["PUT"])
def update_report_weekly(week_id, week):
    return ReportWeeklyController.update_information_report(week_id=week_id, week=week)
