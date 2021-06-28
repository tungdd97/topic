from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class ReportModel(BaseModel):
    IDSinhVien = CharField()
    IDGVHD = CharField()
    DiemLan1 = TextField()
    DiemLan2 = TextField()
    GhiChu = TextField()
    DieuKienBaoVe = CharField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'BaoCaoTong'

    @staticmethod
    def insert_one(data_insert):
        return ReportModel.insert(data_insert).execute()

    @staticmethod
    def get_report_id_sinh_vien(id_sinh_vien):
        try:
            return ReportModel.get(ReportModel.IDSinhVien == str(id_sinh_vien))
        except:
            return None

    @staticmethod
    def update_point_report(id_sinh_vien, point, ghi_chu,lan=1):
        if lan == 1:
            return ReportModel.update(
                DiemLan1=point,
                GhiChu=ghi_chu
            ).where(ReportModel.IDSinhVien == str(id_sinh_vien)).execute()
        if lan == 2:
            return ReportModel.update(
                DiemLan2=point,
                GhiChu=ghi_chu
            ).where(ReportModel.IDSinhVien == str(id_sinh_vien)).execute()

