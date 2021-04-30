from src.api.uri import URI
from flask import Blueprint
from src.controllers.download_controller import DownloadController

download_mod = Blueprint(__name__, __name__)


@download_mod.route(URI.DOWNLOAD_IMAGE, methods=["GET"])
def download_image(week_id, image_id):
    return DownloadController.download_image(week_id, image_id)


@download_mod.route(URI.DOWNLOAD_FILE, methods=["GET"])
def download_file(week_id, file_id):
    return DownloadController.download_file(week_id, file_id)
