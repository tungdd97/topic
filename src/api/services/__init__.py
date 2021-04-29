from src.api import app
from src.api.services.check_service import check_service_mod

v1_0_url_prefix = '/topic/api'

app.register_blueprint(check_service_mod, url_prefix=v1_0_url_prefix)