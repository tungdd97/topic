from configs import File
import os


from configs import Application

WORKING_DIR = Application.WORKING_DIR

APP_IMAGE_DIR = os.path.join(WORKING_DIR, File.IMAGE)
APP_FILE_DIR = os.path.join(WORKING_DIR, File.FILE)


os.makedirs(APP_IMAGE_DIR, exist_ok=True)
os.makedirs(APP_FILE_DIR, exist_ok=True)


class SoLuongSV:
    GVTiepNhan = 26
