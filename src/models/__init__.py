from configs import MYSQLConf

from peewee import *
from playhouse.db_url import connect

db = connect("postgres://prhcrvkizthnpb:204c48536596197ef6e11be06f2f2943fba6f32ab851ad7de6b8c494c4728416@ec2-52-21-252-142.compute-1.amazonaws.com:5432/d3ih0qshmtqert")
DATE_TIME_FORMAT_UTC = "%Y-%m-%dT%TZ"


class BaseModel(Model):
    class Meta:
        database = db
