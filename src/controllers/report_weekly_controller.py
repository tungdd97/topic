import json

from flask import jsonify, request

from src.common.utils import get_current_time
from src.models.student_model import StudentModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.models.report_model import ReportModel
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
                "hinhanh": Topic.HOST + "/download/image/" + str(report_week.id) + "/" + str(
                    report_week.IDSinhVien) if report_week.HinhAnh else "",
                "file": Topic.HOST + "/download/file/" + str(report_week.id) + "/" + str(
                    report_week.IDSinhVien) if report_week.File else "",
                "ghichu": report_week.GhiChu,
            }
            if week in ["8", "16"]:
                try:
                    points = ReportModel.get_report_id_sinh_vien(report_week.IDSinhVien)
                except:
                    points = None
                point = ""
                if points:
                    if week == "8":
                        point = points.DiemLan1
                    if week == "16":
                        point = points.DiemLan2
                data["diem"] = point
                if data.get("diem") and float(data.get("diem")) > 5:
                    data["duyet"] = True

            results.append(data)
        return jsonify({"message": "request thành công!", "data": results, "code": 200}), 200

    @staticmethod
    def update_information_report(week_id, week):
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        ma_sv = request_data.get("ma_sv")
        ghi_chu = request_data.get("ghi_chu")
        if ghi_chu:
            ReportWeeklyModel.update_note_report(
                week_id=week_id,
                ghi_chu=ghi_chu
            )
        if week in ["8", "16"]:
            diem = request_data.get("diem")
            if diem and ma_sv:
                id_sv = StudentModel.get_student_by_ma(ma_sv)
                if not id_sv:
                    return jsonify({"message": "Không tìm thấy mã sinh viên để cập nhật điểm!", "code": 412}), 412
                lan = 1
                if week == "16":
                    lan = 2
                try:
                    reports = ReportModel.get_report_id_sinh_vien(id_sinh_vien=id_sv)
                except:
                    reports = None
                if not reports:
                    data_insert_report = {
                        "IDSinhVien": id_sv,
                        "IDGVHD": "",
                        "DiemLan1": "",
                        "DiemLan2": "",
                        "DieuKienBaoVe": "",
                        "ThoiGianTao": get_current_time(),
                        "ThoiGianCapNhat": get_current_time()
                    }

                    report_id = ReportModel.insert_one(data_insert_report)
                ReportModel.update_point_report(
                    id_sinh_vien=id_sv,
                    point=diem,
                    lan=lan
                )
        return jsonify({"message": "Cập nhật thông tin thành công!", "code": 200}), 200
