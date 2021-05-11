from flask import request, json, jsonify
from src.common.utils import get_current_time
from src.models.comment_model import CommentModel
from src.models.student_model import StudentModel
from src.controllers.file_controller import get_path_file
from src.models.teacher_model import TeacherModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.common import APP_FILE_DIR, APP_IMAGE_DIR


class StudentController:

    @staticmethod
    def join_teacher(student_id):
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        ma_gvhd = request_data.get("magv")
        if not ma_gvhd:
            return jsonify(
                {
                    "message": "Không thể tìm thấy thông tin liên kết! Vui lòng kiểm tra lại mã giáo viên",
                    "code": 412}), 412
        StudentModel.update_request_join_by_student(
            student_id=student_id,
            ma_gvhd=ma_gvhd
        )
        return jsonify({"message": "Đã gửi yêu cầu!", "code": 200}), 200

    @staticmethod
    def add_student():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        if isinstance(request_data, dict):
            request_data = [request_data]
        StudentController.save_student(request_data)
        return jsonify({"message": "Thêm sinh viên thành công!", "code": 200}), 200

    @staticmethod
    def save_student(students):
        all_insert_data = list()
        for data in students:
            all_insert_data.append({
                "Ten": data.get("ten"),
                "MaSV": data.get("masv"),
                "SDT": data.get("sdt", ""),
                "Email": data.get("email", ""),
                "IDLop": data.get("idlop", ""),
                "MaGVHD": "",
                "IDDeTai": "",
                "TrangThai": "TaoMoi",
                "ThoiGianTao": get_current_time(),
                "ThoiGianCapNhat": get_current_time()
            })
        if all_insert_data:
            StudentModel.insert_many_student(all_insert_data)

    @staticmethod
    def report_student(student_id):
        try:
            files = request.files.getlist('files')
            images = request.files.getlist('images')
            form_data = request.form
            week = form_data.get("week")
            note = form_data.get("note")
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412

        all_path_images = list()
        all_path_files = list()
        for image in images:
            folder_save = APP_IMAGE_DIR + "/" + str(student_id)

            filename = image.filename

            path_image_save = get_path_file(folder_save, filename, is_path_df=False)

            image.save(path_image_save)

            all_path_images.append(path_image_save)

        for file in files:
            folder_save = APP_FILE_DIR + "/" + str(student_id)

            filename = file.filename

            path_image_save = get_path_file(folder_save, filename, is_path_df=False)

            file.save(path_image_save)

            all_path_files.append(path_image_save)

        data_insert_report = {
            "Tuan": week,
            "GhiChu": note if note else "",
            "IDSinhVien": student_id,
            "HinhAnh": "<image_upload>".join(all_path_images),
            "File": "<file_upload>".join(all_path_files),
            "Url": "",
            "ThoiGianTao": get_current_time(),
            "ThoiGianCapNhat": get_current_time()
        }

        report_weekly_id = ReportWeeklyModel.insert_one(data_insert_report)
        if report_weekly_id:
            return jsonify({"message": "Upload thành công!", "code": 200}), 200
        return jsonify({"message": "Upload không thành công!", "code": 413}), 413

    @staticmethod
    def send_contact_bean():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        ma_sv = request_data.get("masv")
        noi_dung = request_data.get("noidung")
        tra_ma_sv = StudentModel.get_student_by_ma(masv=ma_sv)
        if not tra_ma_sv:
            return jsonify({"message": "Mã sinh viên không hợp lệ! Vui lòng kiểm tra lại", "code": 412}), 412
        NguoiNhanGhiChu = TeacherModel.get_id_dean()
        comment_id = CommentModel.insert_comment(
            NguoiTaoGhiChu=tra_ma_sv,
            NguoiNhanGhiChu=NguoiNhanGhiChu,
            LoaiGhiChu="sinh_vien_chua_nhan_do_an",
            NoiDung=noi_dung,
            ThoiGianTao=get_current_time()
        )
        return jsonify({"message": "Tạo ghi chú thành công!", "code": 200}), 200

    @staticmethod
    def get_list_student():
        result = list()
        param = request.args

        ten = param.get("ten")
        ma_sv = param.get("masv")
        lop = param.get("lop")
        trang_thai = param.get("trang_thai")
        gvhd = param.get("gvhd")
        page = param.get("page", 1)
        per_page = param.get("per_page", 10)

        page = 0

        paging = {
            "page": page,
            "per_page": per_page,
        }
        students = StudentModel.get_all_student()

        for student in students:
            data = {
                "masv": student.MaSV,
                "ten": student.Ten,
                "lop": "12312312",
                "hom_thu": "",
                "trang_thai": student.TrangThai,
                "gvhd": student.MaGVHD,
                "detai": "De tai"
            }
            result.append(data)
        return jsonify({"message": "Tạo ghi chú thành công!", "data": result, "paging": paging, "code": 200}), 200

    @staticmethod
    def update_request_select_project(student_id):
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        project_id = request_data.get("project_id")
        if not project_id:
            return jsonify(
                {
                    "message": "Không thể tìm thấy thông tin liên kết!",
                    "code": 412}), 412
        StudentModel.update_request_join_project(
            student_id=student_id,
            project_id=project_id
        )
        return jsonify({"message": "Đã gửi yêu cầu!", "code": 200}), 200
