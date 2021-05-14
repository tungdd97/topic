from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class ReportWeeklyModel(BaseModel):
    Tuan = IntegerField()
    GhiChu = TextField()
    IDSinhVien = TextField()
    Diem = TextField()
    HinhAnh = TextField()
    File = TextField()
    Url = TextField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'BaoCaoTuan'

    @staticmethod
    def insert_one(data_insert):
        return ReportWeeklyModel.insert(data_insert).execute()

    @staticmethod
    def get_report_by_week(week):
        return ReportWeeklyModel.select().where(ReportWeeklyModel.Tuan == week).execute()

    @staticmethod
    def get_report_by_student_id(student_id):
        return ReportWeeklyModel.select().where(ReportWeeklyModel.IDSinhVien == student_id).execute()

    @staticmethod
    def get_report_by_id(week_id, image_id):
        return ReportWeeklyModel.get((ReportWeeklyModel.id == week_id) & (ReportWeeklyModel.IDSinhVien == image_id))

    @staticmethod
    def get_report_by_week_student_id(week, student_id):
        try:
            return ReportWeeklyModel.get(
                (ReportWeeklyModel.Tuan == int(week)) & (ReportWeeklyModel.IDSinhVien == student_id))
        except:
            return None

    @staticmethod
    def update_point_report(week, id_sv, diem):
        return ReportWeeklyModel.update(
            Diem=diem
        ).where((ReportWeeklyModel.Tuan == week) & (ReportWeeklyModel.IDSinhVien == id_sv)).execute()

    @staticmethod
    def update_file_report(week_id, ghi_chu, hinhanh, file, thoigiancapnhap):
        return ReportWeeklyModel.update(
            GhiChu=ghi_chu,
            HinhAnh=hinhanh,
            File=file,
            ThoiGianCapNhat=thoigiancapnhap,
        ).where(ReportWeeklyModel.id == week_id).execute()
