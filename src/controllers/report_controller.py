import json

from flask import jsonify, request

from src.common.utils import get_current_time
from src.common import SoLuongSV
from src.models.student_model import StudentModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.models.report_model import ReportModel
from src.models.teacher_model import TeacherModel
from configs import Topic


class ReportController:

    @staticmethod
    def report():
        students = StudentModel.count_student()
        student_not_do_project = StudentModel.count_student_not_do_project()
        teachers = TeacherModel.count_teacher_by_where(TeacherModel.ChucVu == "GiaoVien")
        all_teachers = list()
        teachers_count_by_sl = TeacherModel.get_teacher_by_soluong(SoLuongSV.GVTiepNhan)
        for teacher in teachers_count_by_sl:
            all_teachers.append({
                "ten": teacher.Ten,
                "soluong": teacher.SoLuong,
                "magv": teacher.MaGV,
                "email": teacher.Email
            })
        result = {
            "count_student_do_project": students,
            "count_student_not_do_project": student_not_do_project,
            "count_teacher": teachers,
            "teacher_not_enough_student": all_teachers,
        }
        return jsonify({"message": "Lấy dữ liệu thành công!", "data": result, "code": 200}), 200
