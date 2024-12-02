# app/routes/categories.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Category

bp = Blueprint('categories', __name__)


# 获取所有分类
@bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': category.id,
        'name': category.name,
        'description': category.description
    } for category in categories])


# 获取单个分类信息
@bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get(id)
    if category:
        return jsonify({
            'id': category.id,
            'name': category.name,
            'description': category.description
        })
    return jsonify({'message': 'Category not found'}), 404


# 模糊查找分类（按名称）
@bp.route('/search', methods=['GET'])
def search_categories():
    query = request.args.get('query', '')
    categories = Category.query.filter(
        Category.name.like(f'%{query}%')
    ).all()

    return jsonify([{
        'id': category.id,
        'name': category.name,
        'description': category.description
    } for category in categories])


# 创建分类
@bp.route('/categoryAdd', methods=['POST'])
def create_category():
    data = request.get_json()
    new_category = Category(
        name=data['name'],
        description=data.get('description', '')
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully'}), 201


# 更新分类信息
@bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get(id)
    if category:
        data = request.get_json()
        category.name = data['name']
        category.description = data.get('description', category.description)
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'})
    return jsonify({'message': 'Category not found'}), 404


# 删除单个分类
@bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})
    return jsonify({'message': 'Category not found'}), 404


# 批量删除分类
@bp.route('/delete_multiple', methods=['DELETE'])
def delete_multiple_categories():
    ids = request.get_json().get('ids', [])
    categories = Category.query.filter(Category.id.in_(ids)).all()
    if categories:
        for category in categories:
            db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Categories deleted successfully'})
    return jsonify({'message': 'No categories found with provided IDs'}), 404
