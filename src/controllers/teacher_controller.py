import json

from flask import request, jsonify
from src.common import SoLuongSV
from src.common.utils import get_current_time
from src.models.teacher_model import TeacherModel
from src.models.project_model import ProjectModel
from src.models.student_model import StudentModel
from src.models.comment_model import CommentModel


class TeacherController:

    @staticmethod
    def get_all_teacher_not_enough_student():
        soluong = request.args.get("soluong", SoLuongSV.GVTiepNhan)
        id_std = request.args.get("id_std")

        try:
            cap = StudentModel.get_level_student_id(student_id=id_std)
            all_code_teachers = list()
            all_project_teachers = ProjectModel.get_project_by_cap(cap)
            for project in all_project_teachers:
                all_code_teachers.append(project.ChiDinh)
            teachers = TeacherModel.get_teacher_by_lt_soluong_tids(
                soluong=soluong,
                codes=all_code_teachers
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
                "ghichu": project.GhiChu if project else "",
                "cap": student.Cap
            }
            result.append(data)
        return jsonify({"messgae": "request thành công!", "data": result, "code": 200}), 200

    @staticmethod
    def edit_project_by_teacher(teacher_id):
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412

        ma_sv = request_data.get("ma_sv")
        chuc_nang = request_data.get("chuc_nang")
        if not ma_sv or not chuc_nang:
            return jsonify({
                "message": "Không thể thực hiện chức năng này!. Vui lòng điền đầy đủ thông tin.", "code": 412
            }), 412
        if chuc_nang == "sua_de_tai":
            project_id = request_data.get("id_de_tai")
            if not project_id:
                return jsonify({
                    "message": "Không thể thực hiện chức năng này!. Vui lòng điền đầy đủ thông tin về đề tài",
                    "code": 412
                }), 412
            ma_gvhd = TeacherModel.get_magvhd_by_id(teacher_id)
            if not ma_gvhd:
                return jsonify({
                    "message": "Không tìm thấy mã giáo viên hướng dẫn!",
                    "code": 412
                }), 412
            StudentModel.update_project_by_teacher(
                masv=ma_sv,
                project_id=project_id
            )
            return jsonify({"message": "Đã sửa đề tài thành công!", "code": 200}), 200

        if chuc_nang == "bo_de_tai":
            ma_gvhd = TeacherModel.get_magvhd_by_id(teacher_id)
            if not ma_gvhd:
                return jsonify({
                    "message": "Không tìm thấy mã giáo viên hướng dẫn!",
                    "code": 412
                }), 412
            StudentModel.cancel_project_by_teacher(
                masv=ma_sv
            )
            return jsonify({"message": "Đã bỏ đề tài thành công!", "code": 200}), 200
        return jsonify({"message": "Chức năng không tồn tại vui lòng kiểm tra lại!", "code": 412}), 412

    @staticmethod
    def get_all_teacher():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412

        magv = request_data.get("ma_gv")
        ten_gv = request_data.get("ten_gv")
        sl = request_data.get("so_luong")
        page = request_data.get("page")
        per_page = request_data.get("per_page")

        where = "( TeacherModel.ChucVu == 'GiaoVien' )"

        if magv:
            where += " & ( TeacherModel.MaGV.contains(magv) )"

        if ten_gv:
            where += " & ( TeacherModel.Ten.contains(ten_gv) )"

        if sl:
            where += " & ( TeacherModel.SoLuong == int(sl) )"
        result = list()
        paging = dict()
        if where:
            where = eval(where)
        tong = TeacherModel.count_teacher_by_where(where)
        if tong == 0:
            return jsonify({"messgae": "request thành công!", "data": result, "code": 200}), 200
        if page == -1:
            teachers = TeacherModel.get_teacher_by_where(where=where, is_full=True)
        else:
            paging = TeacherController.generate_paging(
                page=page,
                per_page=per_page,
                sum_page=tong
            )
            skip = per_page * (page - 1)
            limit = per_page
            teachers = TeacherModel.get_teacher_by_where(where=where, skip=skip, limit=limit)
        for teacher in teachers:
            data = {
                "ten": teacher.Ten,
                "soluong": teacher.SoLuong,
                "magv": teacher.MaGV,
                "email": teacher.Email
            }
            result.append(data)
        return jsonify({"messgae": "request thành công!", "data": result, "paging": paging, "code": 200}), 200

    @staticmethod
    def generate_paging(page, per_page, sum_page):
        paging = dict()
        if page >= 0 and per_page:
            total_page = sum_page // per_page
            total_page = total_page if sum_page % per_page <= 0 else total_page + 1
            if sum_page == 0:
                page = 0
            paging = {
                "page": page,
                "per_page": per_page,
                "page_count": total_page,
                "total_count": sum_page,
            }
        return paging

    @staticmethod
    def get_list_message_dean():
        messages = CommentModel.find_list_message_by_type(loai_ghi_chu="sinh_vien_chua_nhan_do_an")
        result = list()
        for message in messages:
            data = {
                "masv": message.NguoiTaoGhiChu,
                "noi_dung": message.NoiDung
            }
            result.append(data)
        return jsonify({"messgae": "request thành công!", "data": result, "code": 200}), 200
