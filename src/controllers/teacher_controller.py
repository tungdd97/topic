import json

from flask import request, jsonify
from src.common import SoLuongSV
from src.common.utils import get_current_time
from src.models.teacher_model import TeacherModel
from src.models.project_model import ProjectModel
from src.models.student_model import StudentModel


class TeacherController:

    @staticmethod
    def get_all_teacher_not_enough_student():
        soluong = request.args.get("soluong", SoLuongSV.GVTiepNhan)

        try:
            teachers = TeacherModel.get_teacher_by_soluong(
                soluong=soluong
            )
        except Exception as e:
            return jsonify({"messgae": str(e), "code": 500}), 500
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
    def add_teacher():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        all_teacher_inserts = list()
        if isinstance(request_data, dict):
            request_data = [request_data]
        for data in request_data:
            all_teacher_inserts.append({
                "Ten": data.get("ten"),
                "SoLuong": 0,
                "MaGV": data.get("magv"),
                "SDT": data.get("sdt"),
                "Email": data.get("email"),
                "ChucVu": data.get("chucvu") if data.get("chucvu") else "GiaoVien",
                "TrangThai": "",
                "ThoiGianTao": get_current_time(),
                "ThoiGianCapNhat": get_current_time()
            })
        if all_teacher_inserts:
            try:
                TeacherModel.insert_many_teacher(all_teacher_inserts)
            except Exception as e:
                return jsonify({"message": str(e), "code": 500}), 500
        return jsonify({"message": "Thêm giáo viên thành công!", "code": 200}), 200

    @staticmethod
    def get_project_by_teacher():
        ma_gvhd = request.args.get("ma_gvhd")
        if not ma_gvhd:
            return jsonify({"messgae": "Không tìm thấy mã giáo viên!", "code": 413}), 413
        project_data_teachers = ProjectModel.get_project_by_one_teacher(ma_gvhd=ma_gvhd)
        result = list()
        for project_data_teacher in project_data_teachers:
            data = {
                "ten": project_data_teacher.Ten,
                "mota": project_data_teacher.MoTa,
                "trang_thai": project_data_teacher.Ten,
                "Ten": project_data_teacher.Ten,
            }
            result.append(data)
        if not result:
            return jsonify({"message": "Không tìm thấy đề tài của giáo viên", "code": 201}), 201
        return jsonify({"message": "Không tìm thấy đề tài của giáo viên", "data": result, "code": 200}), 200

    @staticmethod
    def get_list_student_by_teacher(teacher_id):
        result = list()
        try:
            ma_gvhd = TeacherModel.get_magvhd_by_id(teacher_id)
        except:
            return jsonify({"messgae": "Không tìm thấy mã giáo viên!", "code": 413}), 413
        students = StudentModel.get_student_by_magvhd(magvhd=ma_gvhd)
        for student in students:
            project = None
            if student.IDDeTai:
                project = ProjectModel.get_project_by_id(student.IDDeTai)
            data = {
                "masv": student.MaSV,
                "ten": student.Ten,
                "detai": project.Ten if project else "",
                "ghichu": project.GhiChu if project else ""
            }
            result.append(data)
        return jsonify({"messgae": "request thành công!", "data": result, "code": 200}), 200



