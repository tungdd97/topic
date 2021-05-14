from src.api.uri import URI
from src.api import build_response_susccess, try_catch_error
from flask import Blueprint
from src.controllers.student_controller import StudentController

student_mod = Blueprint(__name__, __name__)


@student_mod.route(URI.CONTACT, methods=["POST"])
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


@student_mod.route(URI.STUDENT_TEACHER, methods=["PUT"])
def update_teacher(student_id):
    return StudentController.join_teacher(student_id)


@student_mod.route(URI.STUDENT_PROJECT, methods=["PUT"])
def update_project(student_id):
    return StudentController.update_request_select_project(student_id)


@student_mod.route(URI.STUDENTS, methods=["POST"])
def get_all_students():
    return StudentController.get_list_student()
