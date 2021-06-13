from os.path import basename
from zipfile import ZipFile

from flask import jsonify, send_file
from src.models.report_weekly_model import ReportWeeklyModel
from src.common.utils import get_current_time
from src.common import APP_ZIP_DIR
from src.controllers.file_controller import get_path_file


class DownloadController:

    @staticmethod
    def download_image(week_id, image_id):
        try:
            report = ReportWeeklyModel.get_report_by_id(week_id, image_id)
        except Exception as e:
            print(e)
            return jsonify({"message": "Có lỗi phát sinh trong server!", "code": 500}), 500
        image_path = report.HinhAnh
        if not image_path:
            return jsonify({"message": "Không tồn tại hình ảnh báo cáo!", "code": 413}), 413
        try:
            # folder = str(get_current_time())
            # path_file_zip = APP_ZIP_DIR + "/" + folder
            # path_file_save = get_path_file(path_file_zip, file_name=folder + ".zip", is_path_df=False)
            # with ZipFile(path_file_save, "w") as zip_new:
            #     for image in image_path.split("<image_upload>"):
            #         zip_new.write(image, basename(image))
            return send_file(image_path, as_attachment=True)
        except FileNotFoundError as f:
            print(f)
            return jsonify({"message": "Tải hình ảnh không thành công!", "code": 413}), 413

    @staticmethod
    def download_file(week_id, file_id):
        try:
            report = ReportWeeklyModel.get_report_by_id(week_id, file_id)
        except Exception as e:
            print(e)
            return jsonify({"message": "Có lỗi phát sinh trong server!", "code": 500}), 500
        file_path = report.File
        if not file_path:
            return jsonify({"message": "Không tồn tại file báo cáo!", "code": 413}), 413
        try:
            # folder = str(get_current_time())
            # path_file_zip = APP_ZIP_DIR + "/" + folder
            # path_file_save = get_path_file(path_file_zip, file_name=folder + ".zip", is_path_df=False)
            # with ZipFile(path_file_save, "w") as zip_new:
            #     for file in file_path.split("<file_upload>"):
            #         zip_new.write(file, basename(file))
            return send_file(file_path, as_attachment=True)
        except FileNotFoundError:
            return jsonify({"message": "Tải file báo cáo không thành công!", "code": 413}), 413