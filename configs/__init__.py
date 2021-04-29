import os
from dotenv import load_dotenv

if not os.environ.get('TOPIC_HOME'):
    os.environ['TOPIC_HOME'], _ = os.path.split(os.path.dirname(os.path.abspath(__file__)))

LOCAL_ENV_FILE = 'local.env'
TEST_ENV_FILE = 'test.env'
ENV_FILE_PATH = os.environ.get('TOPIC') + '/' + TEST_ENV_FILE
load_dotenv(ENV_FILE_PATH)


class Application:
    WORKING_DIR = os.environ['TOPIC_HOME']


class MYSQLConf:
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT'))
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')

    if not MYSQL_USERNAME or not MYSQL_PASSWORD:
        MYSQL_URI = 'mysql://{}:{}/{}'.format(MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE)
    else:
        MYSQL_URI = 'mysql://{}:{}@{}:{}/{}'.format(MYSQL_USERNAME,
                                                    MYSQL_PASSWORD, MYSQL_HOST,
                                                    MYSQL_PORT, MYSQL_DATABASE)
