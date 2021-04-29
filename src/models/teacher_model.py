from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class TeacherModel(BaseModel):
    id = IntegerField()
    Ten = IntegerField()
    SoLuong = IntegerField()
    MaGV = TextField()
    SDT = TextField()
    Email = TimestampField()
    ChucVu = TimestampField()
    TrangThai = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'GiaoVien'

    @staticmethod
    def get_id_dean():
        return TeacherModel.get(TeacherModel.ChucVu == 'TruongKhoa').id

    @staticmethod
    def get_teacher_by_soluong(soluong):
        return TeacherModel.select().where(
            (TeacherModel.SoLuong < soluong) &
            (TeacherModel.ChucVu == "GiaoVien")
        ).execute()

    @staticmethod
    def get_id_by_ma(ma_gv):
        return TeacherModel.get(TeacherModel.MaGV == ma_gv).id
