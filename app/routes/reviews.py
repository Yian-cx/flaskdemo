from flask import Blueprint, request, jsonify
from app import db
from app.models import Review

bp = Blueprint('reviews', __name__)


# 查询所有评论
@bp.route('/', methods=['GET'])
def get_all_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])


# 根据 ID 查询单条评论
@bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify(review.to_dict())


# 新增评论
@bp.route('/', methods=['POST'])
def create_review():
    data = request.json
    new_review = Review(
        book_id=data.get('book_id'),
        user_id=data.get('user_id'),
        rating=data.get('rating'),
        review_text=data.get('review_text')
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201


# 修改评论
@bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    data = request.json
    review.rating = data.get('rating', review.rating)
    review.review_text = data.get('review_text', review.review_text)
    db.session.commit()
    return jsonify(review.to_dict())


# 删除单条评论
@bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": f"Review {review_id} deleted successfully."})


# 模糊查找评论（根据评论内容或评分范围）
@bp.route('/search', methods=['GET'])
def search_reviews():
    keyword = request.args.get('keyword', '')
    min_rating = request.args.get('min_rating', type=float)
    max_rating = request.args.get('max_rating', type=float)

    query = Review.query
    if keyword:
        query = query.filter(Review.review_text.like(f"%{keyword}%"))
    if min_rating is not None:
        query = query.filter(Review.rating >= min_rating)
    if max_rating is not None:
        query = query.filter(Review.rating <= max_rating)

    results = query.all()
    return jsonify([review.to_dict() for review in results])


# 批量删除评论
@bp.route('/delete_batch', methods=['POST'])
def delete_batch_reviews():
    ids = request.json.get('ids', [])
    reviews = Review.query.filter(Review.id.in_(ids)).all()
    for review in reviews:
        db.session.delete(review)
    db.session.commit()
    return jsonify({"message": f"Deleted {len(reviews)} reviews successfully."})
