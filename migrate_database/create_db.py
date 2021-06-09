from src.models import db
from src.models.teacher_model import TeacherModel
from src.models.class_model import ClassModel
from src.models.comment_model import CommentModel
from src.models.project_model import ProjectModel
from src.models.report_model import ReportModel
from src.models.report_weekly_model import ReportWeeklyModel
from src.models.student_model import StudentModel
from src.models.user_model import UserModel


def create_db():
    db.create_tables([
        ProjectModel,
        ReportWeeklyModel,
        TeacherModel,
        StudentModel,
        ReportModel,
        CommentModel,
        UserModel
    ], safe=True)


if __name__ == "__main__":
    create_db()
