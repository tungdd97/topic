from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from src.models.teacher_model import TeacherModel
from peewee import *
import json


class ProjectModel(BaseModel):
    Ten = CharField()
    MoTa = TextField()
    TrangThai = TextField()
    NguoiTao = TextField()
    Loai = CharField()
    GhiChu = TextField()
    Cap = CharField(max_length=2)
    ChiDinh = CharField()
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

    @staticmethod
    def get_all_project():
        return ProjectModel.select().execute()

    @staticmethod
    def get_project_by_teacher(teacher_id):
        return ProjectModel.select().where(ProjectModel.ChiDinh == teacher_id).execute()

    @staticmethod
    def insert_many_project(data_inserts):
        return ProjectModel.insert_many(data_inserts).execute()

    @staticmethod
    def get_project_by_id(project_id):
        return ProjectModel.get(ProjectModel.id == project_id)
