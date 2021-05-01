from flask import request, json, jsonify
from src.common.utils import get_current_time
from src.models.student_model import StudentModel
from src.controllers.file_controller import get_path_file
from src.models.project_model import ProjectModel


class ProjectController:

    @staticmethod
    def get_all_project():
        result = list()
        try:
            projects = ProjectModel.get_all_project()
        except Exception as e:
            print(e)
            return jsonify({"message": "Có lỗi phát sinh trong server!", "code": 500}), 500
        for project in projects:
            result.append({
                "id": project.id,
                "Ten": project.Ten,
                "Mota": project.MoTa,
                "TrangThai": project.TrangThai,
                "GhiChu": project.GhiChu
            })
        return jsonify({"message": "request thành công!", "data": result, "code": 200}), 200

    @staticmethod
    def get_by_project_teacher(teacher_id):
        result = list()
        try:
            projects = ProjectModel.get_project_by_teacher(teacher_id)
        except Exception as e:
            print(e)
            return jsonify({"message": "Có lỗi phát sinh trong server!", "code": 500}), 500
        for project in projects:
            result.append({
                "id": project.id,
                "Ten": project.Ten,
                "Mota": project.MoTa,
                "TrangThai": project.TrangThai,
                "GhiChu": project.GhiChu
            })
        return jsonify({"message": "request thành công!", "data": result, "code": 200}), 200

    @staticmethod
    def add_project():
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        all_project_inserts = list()
        if isinstance(request_data, dict):
            request_data = [request_data]
        for data in request_data:
            all_project_inserts.append({
                "Ten": data.get("ten"),
                "MoTa": data.get("mota"),
                "TrangThai": "Chưa được chọn",
                "NguoiTao": data.get("nguoitao"),
                "Loai": data.get("loai", ""),
                "GhiChu": data.get("ghichu", ""),
                "ThoiGianTao": get_current_time(),
                "ThoiGianCapNhat": get_current_time()
            })
        if all_project_inserts:
            try:
                ProjectModel.insert_many_project(all_project_inserts)
            except Exception as e:
                print(e)
                return jsonify({"message": "Có lỗi phát sinh trong server!", "code": 500}), 500
        return jsonify({"message": "Tạo đề tài thành công!", "code": 200}), 200
