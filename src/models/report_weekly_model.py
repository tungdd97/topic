from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class ReportWeeklyModel(BaseModel):
    Tuan = IntegerField()
    GhiChu = TextField()
    IDSinhVien = TextField()
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
