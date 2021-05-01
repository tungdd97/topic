from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class TeacherModel(BaseModel):
    Ten = CharField()
    SoLuong = IntegerField()
    MaGV = TextField()
    SDT = TextField()
    Email = TextField()
    ChucVu = CharField()
    TrangThai = CharField()
    ThoiGianTao = TimestampField()
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

    @staticmethod
    def insert_many_teacher(data_teacher):
        return TeacherModel.insert_many(data_teacher).execute()

    @staticmethod
    def insert_one_teacher(data_teacher):
        return TeacherModel.insert(data_teacher).execute()

    @staticmethod
    def get_magvhd_by_id(teacher_id):
        return TeacherModel.get(TeacherModel.id == teacher_id).MaGV

