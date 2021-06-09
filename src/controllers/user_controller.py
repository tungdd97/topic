from flask import request, json, jsonify
from src.common.utils import get_current_time, generate_md5_by_str
from src.models.user_model import UserModel
from src.models.student_model import StudentModel
from src.models.teacher_model import TeacherModel


class UserController:

    @staticmethod
    def login():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        username = request_data.get("username")
        password = request_data.get("password")

        password_md5 = generate_md5_by_str(password)

        user_data = UserModel.find_username_password(
            username=username,
            password=password_md5
        )
        if not user_data:
            return jsonify({"message": "Không tìm thấy thông tin tài khoản!", "code": 413}), 413
        ma = None
        if user_data.Quyen == "giaovien":
            ma = TeacherModel.get_magvhd_by_id(int(user_data.LienKet))
        data = {
            "username": username,
            "permission": user_data.Quyen,
            "lienket": user_data.LienKet,
            "iddetai": "",
            "id_gvhd": "",
            "ma": ma
        }
        if user_data.Quyen == "sinhvien":
            student_data = StudentModel.get_student_by_id(student_id=user_data.LienKet)
            if student_data:
                data["ma"] = student_data.MaSV
                if student_data.IDDeTai:
                    data["iddetai"] = student_data.IDDeTai
                if student_data.MaGVHD:
                    teacher_id = TeacherModel.get_id_by_ma(student_data.MaGVHD)
                    if teacher_id:
                        data["id_gvhd"] = teacher_id
                check = int(user_data.LienKet)
                i = check - 3 if check >= 3 else check
                if int(i) == 0:
                    data["start_time_do_an"] = "01/05/2021"
                if int(i) == 1:
                    data["start_time_do_an"] = "19/03/2021"
                if int(i) == 2:
                    data["start_time_do_an"] = "25/12/2020"

        return jsonify({"message": "Đăng nhập thành công!", "data": data, "code": 200}), 200

    @staticmethod
    def register():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        username = request_data.get("username")
        password = request_data.get("password")
        permission = request_data.get("permission", "sinhvien")

        password_md5 = generate_md5_by_str(password)

        check_user_name = UserModel.find_username(
            username=username
        )
        if check_user_name:
            return jsonify({"message": f"Tài khoản {username} đã tồn tại!", "code": 413}), 413
        lienket = None
        if permission == "SinhVien":
            student_data = {
                "Ten": request_data.get("ten"),
                "MaSV": request_data.get("masv"),
                "SDT": request_data.get("sdt", ""),
                "Email": request_data.get("email", ""),
                "IDLop": request_data.get("idlop", ""),
                "MaGVHD": "",
                "IDDeTai": "",
                "TrangThai": "TaoMoi",
                "ThoiGianTao": get_current_time(),
                "ThoiGianCapNhat": get_current_time()
            }

            lienket = StudentModel.insert_one_student(data=student_data)
        if permission in ["GiaoVien", "TruongKhoa"]:
            teacher_data = {
                "Ten": request_data.get("ten"),
                "SoLuong": 0,
                "MaGV": request_data.get("magv"),
                "SDT": request_data.get("sdt"),
                "Email": request_data.get("email"),
                "ChucVu": permission,
                "TrangThai": "",
                "ThoiGianTao": get_current_time(),
                "ThoiGianCapNhat": get_current_time()
            }

            lienket = TeacherModel.insert_many_teacher(teacher_data)

        user_data = {
            "TaiKhoan": username,
            "MatKhau": str(password_md5),
            "Quyen": permission,
            "LienKet": lienket,
            "ThoiGianTao": get_current_time(),
            "ThoiGianCapNhat": get_current_time()
        }
        user_id = UserModel.insert_user(data_insert=user_data)
        if not user_id:
            return jsonify({"message": "Tạo mới thông tin tài khoản thành công!", "code": 413}), 413

        data = {
            "username": username,
            "permission": permission
        }
        return jsonify({"message": "Tạo mới tài khoản thành công!", "data": data, "code": 200}), 200
