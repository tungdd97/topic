from flask import request, jsonify
from src.common import SoLuongSV
from src.models.teacher_model import TeacherModel
from src.models.project_model import ProjectModel


class TeacherController:

    @staticmethod
    def get_all_teacher_not_enough_student():
        soluong = request.args.get("soluong", SoLuongSV.GVTiepNhan)

        teachers = TeacherModel.get_teacher_by_soluong(
            soluong=soluong
        )
        result = list()
        for teacher in teachers:
            data_teacher = {
                "ten": teacher.Ten,
                "soluong": teacher.SoLuong,
                "magv": teacher.MaGV,
                "email": teacher.Email
            }
            result.append(data_teacher)
        return jsonify({"messgae": "Lấy thông tin thành công!", "code": 200, "data": result}), 200

    @staticmethod
    def get_project_by_teacher():
        ma_gvhd = request.args.get("ma_gvhd")
        if not ma_gvhd:
            return jsonify({"messgae": "Không tìm thấy mã giáo viên!", "code": 413}), 413
        project_data_teachers = ProjectModel.get_project_by_one_teacher(ma_gvhd=ma_gvhd)
        result = dict()
        for project_data_teacher in project_data_teachers:
            result = {
                "ten": project_data_teacher.Ten,
                "mota": project_data_teacher.MoTa,
                "trang_thai": project_data_teacher.Ten,
                "Ten": project_data_teacher.Ten,
            }
