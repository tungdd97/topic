from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class UserModel(BaseModel):
    TaiKhoan = IntegerField()
    MatKhau = IntegerField()
    Quyen = TextField()
    LienKet = TextField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'User'

    @staticmethod
    def find_username_password(username, password):
        return UserModel.select().where(TaiKhoan=username, MatKhau=password).execute()

