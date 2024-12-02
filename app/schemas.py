from marshmallow import Schema, fields


class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    publication_date = fields.Date()
    isbn = fields.Str()


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)
