from flask import request, json, jsonify
from src.common.utils import get_current_time, generate_md5_by_str
from src.models.user_model import UserModel


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
        data = {
            "username": username,
            "permission": user_data.permission
        }
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
        user_data = {
            "username": username,
            "password": password_md5,
            "permission": permission
        }
        user_id = UserModel.insert_user(data_insert=user_data)
        if not user_id:
            return jsonify({"message": "Tạo mới thông tin tài khoản thành công!", "code": 413}), 413
        data = {
            "username": username,
            "permission": permission
        }
        return jsonify({"message": "Tạo mới tài khoản thành công!", "data": data, "code": 200}), 200
