from flask import Blueprint, request, jsonify
from app.models import db, User  # 假设 User 是 User 表对应的模型类

bp = Blueprint('users', __name__)


# 获取所有用户
@bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


# 根据 ID 获取用户
@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200


# 创建新用户
@bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],  # 假设存储的是明文，实际应进行加密
            is_active=data.get('is_active', True)
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# 更新用户信息
@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    try:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)  # 同样建议加密处理
        user.is_active = data.get('is_active', user.is_active)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# 删除用户
@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# 模糊查询用户
@bp.route('/search', methods=['GET'])
def search_users():
    query = request.args.get('query', '')
    users = User.query.filter(User.username.like(f'%{query}%')).all()
    return jsonify([user.to_dict() for user in users]), 200


# 批量删除用户
@bp.route('/bulk-delete', methods=['POST'])
def bulk_delete_users():
    ids = request.json.get('ids', [])
    if not ids:
        return jsonify({"error": "No IDs provided"}), 400
    try:
        User.query.filter(User.id.in_(ids)).delete(synchronize_session='fetch')
        db.session.commit()
        return jsonify({"message": "Users deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
