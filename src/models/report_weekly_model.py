from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class ReportWeeklyModel(BaseModel):
    id = IntegerField()
    Tuan = IntegerField()
    GhiChu = IntegerField()
    IDSinhVien = TextField()
    HinhAnh = TextField()
    File = TimestampField()
    Url = TimestampField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'BaoCaoTuan'
