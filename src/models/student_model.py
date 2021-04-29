from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class StudentModel(BaseModel):
    id = IntegerField()
    Ten = IntegerField()
    MaSV = IntegerField()
    SDT = TextField()
    Email = TextField()
    IDLop = IntegerField()
    MaGVHD = CharField()
    TrangThai = CharField()
    IDDeTai = CharField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'SinhVien'

    @staticmethod
    def update_request_join_by_student(ma_sv, ma_gvhd):
        return StudentModel.update(
            MaGVHD=ma_gvhd,
            TrangThai="YeuCau"
        ).where(StudentModel.MaSV == ma_sv).execute()
