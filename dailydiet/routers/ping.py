from flask import Blueprint

bp = Blueprint("ping", __name__, url_prefix="/api/ping")


@bp.route("/", methods=("GET",))
def ping():
    return {"message": "pong"}
