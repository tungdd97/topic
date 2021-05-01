from configs import MYSQLConf

from peewee import *
from playhouse.db_url import connect

db = connect(MYSQLConf.MYSQL_URI)
DATE_TIME_FORMAT_UTC = "%Y-%m-%dT%TZ"


class BaseModel(Model):
    class Meta:
        database = db
