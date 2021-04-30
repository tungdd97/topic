from src.api.uri import URI
from flask import Blueprint
from src.controllers.teacher_controller import TeacherController

teacher_mod = Blueprint(__name__, __name__)


@teacher_mod.route(URI.TEACHER, methods=["GET"])
def get_all_teacher():
    return TeacherController.get_all_teacher_not_enough_student()


@teacher_mod.route(URI.TEACHER, methods=["POST"])
def add_teacher():
    return TeacherController.add_teacher()


@teacher_mod.route(URI.TEACHER_DETAIL, methods=["GET"])
def get_teacher_detail(teacher_id):
    return TeacherController.get_list_student_by_teacher(teacher_id)
