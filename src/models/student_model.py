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
    def update_request_join_by_student(student_id, ma_gvhd):
        return StudentModel.update(
            MaGVHD=ma_gvhd,
            TrangThai="YeuCau"
        ).where(StudentModel.id == student_id).execute()

    @staticmethod
    def update_request_join_project(student_id, project_id):
        return StudentModel.update(
            IDDeTai=project_id,
            TrangThai="YeuCau"
        ).where(StudentModel.id == student_id).execute()

    @staticmethod
    def insert_many_student(data_students):
        return StudentModel.insert_many(data_students).execute()

    @staticmethod
    def insert_one_student(data):
        return StudentModel.insert(data).execute()

    @staticmethod
    def get_student_by_magvhd(magvhd):
        return StudentModel.select().where(StudentModel.MaGVHD == magvhd).execute()

    @staticmethod
    def get_all_student():
        return StudentModel.select().execute()

    @staticmethod
    def get_student_by_id(student_id):
        return StudentModel.get(StudentModel.id == student_id)

    @staticmethod
    def get_student_by_ma(masv):
        return StudentModel.get(StudentModel.MaSV == masv).id

    @staticmethod
    def update_project_by_teacher(masv, project_id):
        return StudentModel.update(
            IDDeTai=project_id
        ).where(StudentModel.MaSV == masv).execute()

    @staticmethod
    def cancel_project_by_teacher(masv):
        return StudentModel.update(
            IDDeTai=None
        ).where(StudentModel.MaSV == masv).execute()


