# FlaskDemo 项目

这是一个基于 Flask 框架开发的 RESTful API 项目，主要功能包括书籍管理、用户管理、评论管理、分类管理和日志记录等操作。

---

## 功能简介

- **书籍管理**：支持书籍的增删改查、模糊查询、多选删除等操作。
- **分类管理**：管理书籍的分类信息。
- **用户管理**：提供用户注册、登录、更新信息、删除用户等功能。
- **评论管理**：支持对书籍的评论操作，包括新增、查看、更新、删除等功能。
- **日志记录**：记录系统操作日志，用于后期审计或调试。

---

## 环境要求

- Python >= 3.9
- MySQL 数据库
- SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/bookdb'
---

## 安装步骤

### 1. 克隆项目
```bash
git clone https://github.com/your-repository/FlaskDemo.git
cd FlaskDemo