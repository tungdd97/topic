from src.api import app
from src.api.services.check_service import check_service_mod
from src.api.services.student_blueprint import student_mod
from src.api.services.project_blueprint import project_mod
from src.api.services.teacher_blueprint import teacher_mod

v1_0_url_prefix = '/topic/api'

app.register_blueprint(check_service_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(student_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(project_mod, url_prefix=v1_0_url_prefix)
app.register_blueprint(teacher_mod, url_prefix=v1_0_url_prefix)
