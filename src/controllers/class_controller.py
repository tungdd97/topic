from flask import jsonify
from src.models.class_model import ClassModel


class ClassController:

    @staticmethod
    def add_class():
        return jsonify({"message": "Tải hình ảnh không thành công!", "code": 413}), 413
