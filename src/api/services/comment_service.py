from src.api.uri import URI
from src.api import try_catch_error
from flask import Blueprint
from src.controllers.report_weekly_controller import ReportWeeklyController

comment_service_mod = Blueprint(__name__, __name__)


@comment_service_mod.route(URI.ALL_COMMENT, methods=["GET"])
# @try_catch_error
def get_all_comment(student_id):
    return ReportWeeklyController.get_all_comment_by_student_id(student_id=student_id)
