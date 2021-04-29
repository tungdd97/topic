from flask import request, json, jsonify
from src.common.utils import get_current_time
from src.models.student_model import StudentModel
from src.models.teacher_model import TeacherModel


class StudentController:

    @staticmethod
    def join_teacher():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        ma_sv = request_data.get("ma_sv")
        ma_gvhd = request_data.get("ma_gvhd")
        if not ma_gvhd or not ma_sv:
            return jsonify(
                {
                    "message": "Không thể tìm thấy thông tin liên kết! Vui lòng kiểm tra lại mã sinh viên hoặc mã giáo viên",
                    "code": 412}), 412
        StudentModel.update_request_join_by_student(
            ma_sv=ma_sv,
            ma_gvhd=ma_gvhd
        )
        return jsonify({"message": "Đã gửi yêu cầu!", "code": 200}), 200
