import json

from flask import jsonify, request

from src.common.utils import get_current_time
from src.models.student_model import StudentModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.models.report_model import ReportModel
from src.models.teacher_model import TeacherModel
from configs import Topic


class ReportWeeklyController:

    @staticmethod
    def get_report_by_week(teacher_id, week):
        try:
            args = request.args
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        results = list()
        report_weekly = ReportWeeklyModel.get_report_by_week(week=week)
        for report_week in report_weekly:
            ma_gv = TeacherModel.get_magvhd_by_id(teacher_id=teacher_id)
            sinhvien = StudentModel.get_student_by_id(report_week.IDSinhVien)
            if not ma_gv or sinhvien.MaGVHD != ma_gv:
                continue
            data = {
                "tuan": week,
                "masv": sinhvien.MaSV,
                "ten": sinhvien.Ten,
                "hinhanh": Topic.HOST + "/download/image/" + str(report_week.id) + "/" + str(
                    report_week.IDSinhVien) if report_week.HinhAnh else "",
                "file": Topic.HOST + "/download/file/" + str(report_week.id) + "/" + str(
                    report_week.IDSinhVien) if report_week.File else "",
                # "ghichu": report_week.GhiChu,
                "diem": report_week.Diem
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
    def update_information_report(week):
        try:
            request_data = request.data
            request_data = json.loads(request_data)
        except:
            return jsonify({"message": "Không thể lấy dữ liệu!", "code": 412}), 412
        ma_sv = request_data.get("ma_sv")
        ghi_chu = request_data.get("ghi_chu")
        diem = request_data.get("diem")
        if not diem or not ma_sv:
            return jsonify({"message": "Không tìm thấy mã sinh viên để cập nhật điểm!", "code": 412}), 412
        id_sv = StudentModel.get_student_by_ma(ma_sv)
        if not id_sv:
            return jsonify({"message": "Không tìm thấy mã sinh viên để cập nhật điểm!", "code": 412}), 412
        if week not in ["8", "16"]:
            ReportWeeklyModel.update_point_report(
                week=week,
                id_sv=id_sv,
                diem=diem,
                ghi_chu=ghi_chu
            )
        else:
            lan = 1
            if week == "16":
                lan = 2
            reports = ReportModel.get_report_id_sinh_vien(id_sinh_vien=id_sv)
            if not reports:
                data_insert_report = {
                    "IDSinhVien": id_sv,
                    "IDGVHD": "",
                    "DiemLan1": "",
                    "DiemLan2": "",
                    "DieuKienBaoVe": "",
                    "GhiChu": ghi_chu,
                    "ThoiGianTao": get_current_time(),
                    "ThoiGianCapNhat": get_current_time()
                }

                report_id = ReportModel.insert_one(data_insert_report)
            ReportModel.update_point_report(
                id_sinh_vien=id_sv,
                point=diem,
                lan=lan,
                ghi_chu=ghi_chu
            )
        return jsonify({"message": "Cập nhật thông tin thành công!", "code": 200}), 200

    @staticmethod
    def browse_report_weekly(teacher_id, masv):
        id_sinh_vien = StudentModel.get_student_by_ma(masv=masv)
        if not id_sinh_vien:
            return jsonify({"message": "Không tìm thấy thông tin sinh viên!", "code": 412}), 412
        reports = ReportWeeklyModel.get_report_by_student_id(student_id=id_sinh_vien)
        if not reports:
            return jsonify({"message": "Không tìm thấy thông tin báo cáo sinh viên!", "code": 412}), 412
        all_weekly = list()
        for report in reports:
            point = None
            if report.Tuan in ["8", "16"]:
                try:
                    points = ReportModel.get_report_id_sinh_vien(id_sinh_vien=id_sinh_vien)
                except:
                    points = None
                if points:
                    if report.Tuan == "8":
                        point = points.DiemLan1
                    if report.Tuan == "16":
                        point = points.DiemLan2
            else:
                point = report.Diem
            if not point:
                all_weekly.append(report.Tuan)
        for i in range(1, 21):
            if i not in all_weekly:
                all_weekly.append(i)

        return jsonify({"message": "lấy thông tin thành công!", "data": all_weekly, "code": 200}), 200

    @staticmethod
    def get_all_comment_by_student_id(student_id):
        reports = ReportWeeklyModel.get_report_by_student_id(student_id=student_id)
        if not reports:
            return jsonify({"message": "Không tìm thấy thông tin báo cáo sinh viên!", "code": 412}), 412
        all_comment = list()
        for report in reports:
            ghi_chu = None
            if report.Tuan in ["8", "16"]:
                try:
                    points = ReportModel.get_report_id_sinh_vien(id_sinh_vien=student_id)
                except:
                    points = None
                if points:
                    ghi_chu = points.GhiChu
            else:
                ghi_chu = report.GhiChu
            data = {
                "tuan": report.Tuan,
                "ghichu": ghi_chu
            }
            all_comment.append(data)

        return jsonify({"message": "lấy thông tin thành công!", "data": all_comment, "code": 200}), 200
