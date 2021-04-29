from flask import request, json, jsonify
from src.common.utils import get_current_time
from src.models.comment_model import CommentModel
from src.models.teacher_model import TeacherModel


class ContactController:

    @staticmethod
    def send_contact_bean():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        ma_sv = request_data.get("ma_sv")
        noi_dung = request_data.get("noi_dung")
        tra_ma_sv = True
        if not tra_ma_sv:
            return jsonify({"message": "Mã sinh viên không hợp lệ! Vui lòng kiểm tra lại", "code": 412}), 412
        NguoiNhanGhiChu = TeacherModel.get_id_dean()
        comment_id = CommentModel.insert_comment(
            NguoiTaoGhiChu=ma_sv,
            NguoiNhanGhiChu=NguoiNhanGhiChu,
            LoaiGhiChu="sinh_vien_chua_nhan_do_an",
            NoiDung=noi_dung,
            ThoiGianTao=get_current_time()
        )
        return jsonify({"message": "Tạo ghi chú thành công!", "code": 200}), 200
