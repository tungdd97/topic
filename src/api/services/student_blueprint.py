from src.api.uri import URI
from src.api import build_response_susccess, try_catch_error
from flask import Blueprint
from src.controllers.student_controller import StudentController

student_mod = Blueprint(__name__, __name__)


@student_mod.route(URI.CONTACT, methods=["POST"])
@try_catch_error
def student_contact():
    return StudentController.send_contact_bean()


@student_mod.route(URI.STUDENT_REPORT, methods=["POST"])
def student_report(student_id):
    return StudentController.report_student(student_id)


@student_mod.route(URI.STUDENT, methods=["POST"])
def add_student():
    return StudentController.add_student()


@student_mod.route(URI.STUDENT, methods=["GET"])
def get_students():
    return StudentController.get_list_student()