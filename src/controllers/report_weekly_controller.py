from flask import request, json, jsonify
from src.common.utils import get_current_time
from src.models.comment_model import CommentModel
from src.models.student_model import StudentModel
from src.controllers.file_controller import get_path_file
from src.models.teacher_model import TeacherModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.models.report_model import ReportModel
from src.common import APP_FILE_DIR, APP_IMAGE_DIR
from configs import Topic


class ReportWeeklyController:

    @staticmethod
    def get_report_by_week(week):
        results = list()
        report_weekly = ReportWeeklyModel.get_report_by_week(week=week)
        for report_week in report_weekly:
            sinhvien = StudentModel.get_student_by_id(report_week.IDSinhVien)
            data = {
                "tuan": week,
                "masv": sinhvien.MaSV,
                "ten": sinhvien.Ten,
                "hinhanh": Topic.HOST + "/download/image/" + str(report_week.id) + "/" + str(report_week.IDSinhVien),
                "file": Topic.HOST + "/download/file/" + str(report_week.id) + "/" + str(report_week.IDSinhVien),
                "ghichu": report_week.GhiChu,
            }
            results.append(data)
        return jsonify({"message": "request thành công!", "data": results, "code": 200}), 200
