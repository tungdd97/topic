import os

os.environ['TOPIC_HOME'], _ = os.path.split(os.path.abspath(__file__))

from src.api.services import *
from flask_cors import CORS
from src.models import db
from src.models.teacher_model import TeacherModel
from src.models.class_model import ClassModel
from src.models.comment_model import CommentModel
from src.models.project_model import ProjectModel
from src.models.report_model import ReportModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.models.student_model import StudentModel
from src.models.user_model import UserModel

CORS(app)


@app.before_request
def execute_before_request():
    """
    Thực thi trước khi xử lý request. Ví dụ: kết nối database.
    :return:
    """
    db.create_tables([
        ProjectModel,
        ReportWeeklyModel,
        TeacherModel,
        StudentModel,
        ReportModel
    ], safe=True)


@app.teardown_request
def execute_when(exec):
    """
    Thực thi khi một request bị ngắt. Ví dụ: ngắt kết nối database.
    :param exec:
    :return:
    """
    if not db.is_closed():
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
