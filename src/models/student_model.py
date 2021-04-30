from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class StudentModel(BaseModel):
    Ten = CharField()
    MaSV = CharField()
    SDT = TextField()
    Email = TextField()
    IDLop = IntegerField()
    MaGVHD = CharField()
    TrangThai = CharField()
    IDDeTai = CharField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'SinhVien'

    @staticmethod
    def update_request_join_by_student(ma_sv, ma_gvhd):
        return StudentModel.update(
            MaGVHD=ma_gvhd,
            TrangThai="YeuCau"
        ).where(StudentModel.MaSV == ma_sv).execute()

    @staticmethod
    def insert_many_student(data_students):
        return StudentModel.insert_many(data_students).execute()

    @staticmethod
    def get_student_by_magvhd(magvhd):
        return StudentModel.select().where(StudentModel.MaGVHD == magvhd).execute()

    @staticmethod
    def get_all_student():
        return StudentModel.select().execute()

    @staticmethod
    def get_student_by_id(student_id):
        return StudentModel.get(StudentModel.id == student_id)


