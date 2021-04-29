from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class StudentModel(BaseModel):
    id = IntegerField()
    MaLop = IntegerField()
    TenLop = IntegerField()
    ThoiGianBDDoAn = TextField()
    ThoiGianKetThuc = TextField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'Lop'
