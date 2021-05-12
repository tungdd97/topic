import os
from dotenv import load_dotenv

if not os.environ.get('TOPIC_HOME'):
    os.environ['TOPIC_HOME'], _ = os.path.split(os.path.dirname(os.path.abspath(__file__)))

LOCAL_ENV_FILE = 'local.env'
TEST_ENV_FILE = 'test.env'
ENV_FILE_PATH = os.environ.get('TOPIC_HOME') + '/' + LOCAL_ENV_FILE
load_dotenv(ENV_FILE_PATH)


class Application:
    WORKING_DIR = os.environ['TOPIC_HOME']


class MYSQLConf:
    MYSQL_URI = os.environ.get("MYSQL_URI")


class Topic:
    HOST = os.environ.get("HOST")


class File:
    IMAGE = 'image'
    FILE = 'file'
    ZIP = "zip"
