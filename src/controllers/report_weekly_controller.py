from flask import jsonify
from src.models.student_model import StudentModel
from src.models.report_weekly_model import ReportWeeklyModel
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
                "hinhanh": Topic.HOST + "/download/image/" + str(report_week.id) + "/" + str(report_week.IDSinhVien) if report_week.HinhAnh else "",
                "file": Topic.HOST + "/download/file/" + str(report_week.id) + "/" + str(report_week.IDSinhVien) if report_week.File else "",
                "ghichu": report_week.GhiChu,
            }
            results.append(data)
        return jsonify({"message": "request thành công!", "data": results, "code": 200}), 200
