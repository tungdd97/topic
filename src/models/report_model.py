from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class ReportModel(BaseModel):
    IDSinhVien = IntegerField()
    IDGVHD = IntegerField()
    DiemLan1 = TextField()
    DiemLan2 = TextField()
    DieuKienBaoVe = CharField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'BaoCaoTong'

    @staticmethod
    def get_report_id_sinh_vien(id_sinh_vien):
        return ReportModel.get(ReportModel.IDSinhVien == id_sinh_vien)