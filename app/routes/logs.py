from flask import request

from flask import Blueprint, jsonify

from app import db
from app.models import Log

bp = Blueprint('logs', __name__)


@bp.route('/', methods=['GET'])
def get_logs():
    logs = Log.query.all()
    return jsonify([log.to_dict() for log in logs])


@bp.route('/<int:log_id>', methods=['GET'])
def get_log(log_id):
    log = Log.query.get_or_404(log_id)  # 获取指定ID的日志
    return jsonify(log.to_dict())

@bp.route('/', methods=['POST'])
def create_log():
    data = request.get_json()  # 获取请求的JSON数据
    new_log = Log(
        user_id=data['user_id'],
        action=data['action'],
        details=data['details'],
        ip_address=data['ip_address'],
        status=data['status'],
        resource=data['resource']
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify(new_log.to_dict()), 201


@bp.route('/search', methods=['GET'])
def search_logs():
    user_id = request.args.get('user_id')
    action = request.args.get('action')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Log.query

    if user_id:
        query = query.filter(Log.user_id == user_id)
    if action:
        query = query.filter(Log.action.like(f'%{action}%'))
    if start_date and end_date:
        query = query.filter(Log.timestamp.between(start_date, end_date))

    logs = query.all()
    return jsonify([log.to_dict() for log in logs])