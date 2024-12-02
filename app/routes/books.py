# app/routes/books.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Book

bp = Blueprint('books', __name__)


# 获取所有图书
@bp.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'publication_date': book.publication_date.strftime('%Y-%m-%d'),
        'isbn': book.isbn,
        'total_copies': book.total_copies,
        'available_copies': book.available_copies
    } for book in books])


# 获取单个图书信息
@bp.route('/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book:
        return jsonify({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'publication_date': book.publication_date.strftime('%Y-%m-%d'),
            'isbn': book.isbn,
            'total_copies': book.total_copies,
            'available_copies': book.available_copies
        })
    return jsonify({'message': 'Book not found'}), 404


# 模糊查找图书（按标题或作者）
@bp.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    books = Book.query.filter(
        Book.title.like(f'%{query}%') | Book.author.like(f'%{query}%')
    ).all()

    return jsonify([{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'publication_date': book.publication_date.strftime('%Y-%m-%d'),
        'isbn': book.isbn,
        'total_copies': book.total_copies,
        'available_copies': book.available_copies
    } for book in books])


# 创建图书
@bp.route('/bookAdd', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        publication_date=data['publication_date'],
        isbn=data['isbn'],
        total_copies=data['total_copies'],
        available_copies=data['available_copies']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'}), 201


# 更新图书信息
@bp.route('/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book:
        data = request.get_json()
        book.title = data['title']
        book.author = data['author']
        book.publication_date = data['publication_date']
        book.isbn = data['isbn']
        book.total_copies = data['total_copies']
        book.available_copies = data['available_copies']
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'}), 404


# 删除单本图书
@bp.route('/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'}), 404


# 批量删除图书
@bp.route('/delete_multiple', methods=['DELETE'])
def delete_multiple_books():
    ids = request.get_json().get('ids', [])
    books = Book.query.filter(Book.id.in_(ids)).all()
    if books:
        for book in books:
            db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Books deleted successfully'})
    return jsonify({'message': 'No books found with provided IDs'}), 404
