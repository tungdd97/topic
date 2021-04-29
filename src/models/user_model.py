from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class UserModel(BaseModel):
    id = IntegerField()
    TaiKhoan = IntegerField()
    MatKhau = IntegerField()
    Quyen = TextField()
    LienKet = TextField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'user'
