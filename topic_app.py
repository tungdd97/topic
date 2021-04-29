import os

os.environ['TOPIC_HOME'], _ = os.path.split(os.path.abspath(__file__))

from src.api.services import *
from flask_cors import CORS

CORS(app)


@app.before_request
def execute_before_request():
    """
    Thực thi trước khi xử lý request. Ví dụ: kết nối database.
    :return:
    """


@app.teardown_request
def execute_when(exec):
    """
    Thực thi khi một request bị ngắt. Ví dụ: ngắt kết nối database.
    :param exec:
    :return:
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
