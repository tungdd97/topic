from src.api import app
from src.api.services.check_service import check_service_mod
from src.api.services.student_blueprint import student_mod
from src.api.services.project_blueprint import project_mod
from src.api.services.teacher_blueprint import teacher_mod
from src.api.services.download_blue_print import download_mod
from src.api.services.report_weekly_blueprint import report_weekly_mod
from src.api.services.report_blueprint import report_mod
from src.api.services.user_blueprint import user_mod
from src.api.services.comment_service import comment_service_mod

v1_0_url_prefix = '/topic/api'

app.register_blueprint(check_service_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(student_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(project_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(teacher_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(download_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(report_weekly_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(user_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(report_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(comment_service_mod, url_prefix=v1_0_url_prefix)
