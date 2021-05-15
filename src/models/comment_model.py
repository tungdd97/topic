from playhouse.shortcuts import model_to_dict

from src.models import BaseModel
from peewee import *
import json


class CommentModel(BaseModel):
    NguoiTaoGhiChu = CharField()
    NguoiNhanGhiChu = IntegerField()
    LoaiGhiChu = TextField()
    NoiDung = TextField()
    ThoiGianTao = TimestampField()

    class Meta:
        table_name = 'GhiChu'

    @staticmethod
    def insert_comment(NguoiTaoGhiChu, NguoiNhanGhiChu, LoaiGhiChu, NoiDung, ThoiGianTao):
        data_insert = {
            "NguoiTaoGhiChu": NguoiTaoGhiChu,
            "NguoiNhanGhiChu": NguoiNhanGhiChu,
            "LoaiGhiChu": LoaiGhiChu,
            "NoiDung": NoiDung,
            "ThoiGianTao": ThoiGianTao
        }
        return CommentModel.insert(data_insert).execute()

    @staticmethod
    def find_list_message_by_type(loai_ghi_chu):
        return CommentModel.select().where(CommentModel.LoaiGhiChu == loai_ghi_chu).execute()
