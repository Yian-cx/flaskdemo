class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用 Flask-SQLAlchemy 的修改追踪
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cxypc@localhost/bookdb'  # 使用正确的数据库连接 URI