from flask import Flask, jsonify
from functools import wraps

app = Flask(__name__)


def build_response_susccess(message=None, data=None):
    result = {"code": 200}
    if message:
        result["message"] = message
    if data:
        result["data"] = data
    return result


@app.errorhandler(500)
def internal_server_error():
    return jsonify({"message": "Có lỗi phát sinh trong server!"}), 500


def try_catch_error(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return jsonify(f(*args, **kwargs)), 200
        except Exception as e:
            return internal_server_error(e)

    return decorated
