from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class UserModel(BaseModel):
    TaiKhoan = CharField()
    MatKhau = CharField()
    Quyen = CharField()
    LienKet = CharField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'User'

    @staticmethod
    def find_username_password(username, password):
        return UserModel.select().where((UserModel.TaiKhoan == username) & (UserModel.MatKhau == password)).execute()

    @staticmethod
    def find_username(username):
        return UserModel.get(UserModel.TaiKhoan == username)

    @staticmethod
    def insert_user(data_insert):
        return UserModel.insert(data_insert).execute()
