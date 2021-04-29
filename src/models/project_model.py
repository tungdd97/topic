from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from src.models.teacher_model import TeacherModel
from peewee import *
import json


class ProjectModel(BaseModel):
    id = IntegerField()
    Ten = IntegerField()
    MoTa = IntegerField()
    TrangThai = TextField()
    NguoiTao = TextField()
    Loai = CharField()
    GhiChu = TextField()
    ThoiGianTao = TimestampField()
    ThoiGianCapNhat = TimestampField()

    class Meta:
        table_name = 'DeTai'

    @staticmethod
    def get_project_by_teachers():
        return ProjectModel.select(ProjectModel, TeacherModel.id).where(
            (ProjectModel.Loai == "GiaoVien") & (
                ProjectModel.NguoiTao.in_(TeacherModel.id)
            )
        ).execute()

    @staticmethod
    def get_project_by_one_teacher(ma_gvhd):
        return ProjectModel.select(ProjectModel).where(
            (ProjectModel.Loai == "GiaoVien") & (
                ProjectModel.NguoiTao == ma_gvhd
            )
        ).execute()