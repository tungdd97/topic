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
    def get_teacher_by_lt_soluong_tids(soluong, codes):
        return TeacherModel.select().where(
            (TeacherModel.SoLuong < soluong) &
            (TeacherModel.ChucVu == "GiaoVien") & (TeacherModel.MaGV.in_(codes))
        ).execute()

    @staticmethod
    def get_id_by_ma(ma_gv):
        try:
            return TeacherModel.get(TeacherModel.MaGV == ma_gv).id
        except:
            return None

    @staticmethod
    def get_so_luong_by_ma(ma_gv):
        try:
            return TeacherModel.get(TeacherModel.MaGV == ma_gv).SoLuong
        except:
            print(f"Không tìm thấy số lượng của mã giáo viên {ma_gv}")
            return False

    @staticmethod
    def update_so_luong_by_magvhd(ma_gv, soluong=1):
        return TeacherModel.update(SoLuong=TeacherModel.SoLuong + soluong).where(TeacherModel.MaGV == ma_gv).execute()

    @staticmethod
    def insert_many_teacher(data_teacher):
        return TeacherModel.insert_many(data_teacher).execute()

    @staticmethod
    def insert_one_teacher(data_teacher):
        return TeacherModel.insert(data_teacher).execute()

    @staticmethod
    def get_magvhd_by_id(teacher_id):
        try:
            return TeacherModel.get(TeacherModel.id == int(teacher_id)).MaGV
        except:
            return None

    @staticmethod
    def get_teacher_by_where(where=None, skip=None, limit=None, is_full=False):
        if is_full:
            return TeacherModel.select().where(where).execute()
        return TeacherModel.select().where(where).offset(skip).limit(limit).execute()

    @staticmethod
    def count_teacher_by_where(where):
        return TeacherModel.select().where(where).count()
