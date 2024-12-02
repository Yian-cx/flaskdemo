# API 接口说明文档 
## macos py版本3.12 mysql版本9.0.1
## http://127.0.0.1:5000/

## 1. 获取所有书籍

- **接口路径**: `/api/books/`
- **方法**: `GET`
- **请求参数**: 无

---

## 2. 添加书籍

- **接口路径**: `/api/books/`
- **方法**: `POST`
- **请求参数**:
  - `title`: 书名
  - `author`: 作者
  - `publication_date`: 出版日期
  - `isbn`: ISBN
  - `total_copies`: 总副本数
  - `available_copies`: 可用副本数

---

## 3. 更新书籍信息

- **接口路径**: `/api/books/{book_id}/`
- **方法**: `PUT`
- **请求参数**:
  - `title`: 书名
  - `author`: 作者
  - `publication_date`: 出版日期
  - `isbn`: ISBN
  - `total_copies`: 总副本数
  - `available_copies`: 可用副本数

---

## 4. 删除书籍

- **接口路径**: `/api/books/{book_id}/`
- **方法**: `DELETE`
- **请求参数**: 无

---

## 5. 获取单个书籍

- **接口路径**: `/api/books/{book_id}/`
- **方法**: `GET`
- **请求参数**: 无

---

## 6. 模糊查找书籍

- **接口路径**: `/api/books/search/`
- **方法**: `GET`
- **请求参数**:
  - `query`: 查询关键字（书名或作者）

---

## 7. 获取所有分类

- **接口路径**: `/api/categories/`
- **方法**: `GET`
- **请求参数**: 无

---

## 8. 添加分类

- **接口路径**: `/api/categories/`
- **方法**: `POST`
- **请求参数**:
  - `name`: 分类名
  - `description`: 分类描述

---

## 9. 获取单个分类

- **接口路径**: `/api/categories/{category_id}/`
- **方法**: `GET`
- **请求参数**: 无

---

## 10. 更新分类

- **接口路径**: `/api/categories/{category_id}/`
- **方法**: `PUT`
- **请求参数**:
  - `name`: 分类名
  - `description`: 分类描述

---

## 11. 删除分类

- **接口路径**: `/api/categories/{category_id}/`
- **方法**: `DELETE`
- **请求参数**: 无

---

## 12. 获取所有用户

- **接口路径**: `/api/users/`
- **方法**: `GET`
- **请求参数**: 无

---

## 13. 添加用户

- **接口路径**: `/api/users/`
- **方法**: `POST`
- **请求参数**:
  - `username`: 用户名
  - `password`: 密码
  - `email`: 邮箱
  - `role`: 角色（如：管理员、普通用户）

---

## 14. 获取单个用户

- **接口路径**: `/api/users/{user_id}/`
- **方法**: `GET`
- **请求参数**: 无

---

## 15. 更新用户信息

- **接口路径**: `/api/users/{user_id}/`
- **方法**: `PUT`
- **请求参数**:
  - `username`: 用户名
  - `password`: 密码
  - `email`: 邮箱
  - `role`: 角色（如：管理员、普通用户）

---

## 16. 删除用户

- **接口路径**: `/api/users/{user_id}/`
- **方法**: `DELETE`
- **请求参数**: 无

---

## 17. 获取所有评论

- **接口路径**: `/api/reviews/`
- **方法**: `GET`
- **请求参数**: 无

---

## 18. 添加评论

- **接口路径**: `/api/reviews/`
- **方法**: `POST`
- **请求参数**:
  - `book_id`: 书籍ID
  - `user_id`: 用户ID
  - `rating`: 评分
  - `content`: 评论内容

---

## 19. 获取单个评论

- **接口路径**: `/api/reviews/{review_id}/`
- **方法**: `GET`
- **请求参数**: 无

---

## 20. 更新评论

- **接口路径**: `/api/reviews/{review_id}/`
- **方法**: `PUT`
- **请求参数**:
  - `rating`: 评分
  - `content`: 评论内容

---

## 21. 删除评论

- **接口路径**: `/api/reviews/{review_id}/`
- **方法**: `DELETE`
- **请求参数**: 无

---

## 22. 获取所有日志

- **接口路径**: `/api/logs/`
- **方法**: `GET`
- **请求参数**: 无

---

## 23. 添加日志

- **接口路径**: `/api/logs/`
- **方法**: `POST`
- **请求参数**:
  - `user_id`: 用户ID
  - `action`: 动作类型
  - `details`: 详细描述
  - `ip_address`: 用户IP地址
  - `status`: 操作状态
  - `resource`: 资源类型

---

## 24. 获取单个日志

- **接口路径**: `/api/logs/{log_id}/`
- **方法**: `GET`
- **请求参数**: 无

---

## 25. 删除日志

- **接口路径**: `/api/logs/{log_id}/`
- **方法**: `DELETE`
- **请求参数**: 无

---

## 错误代码

| 错误码 | 描述            |
|-----|---------------|
| 400 | 请求参数错误，缺少必要字段 |
| 401 | 未经授权，缺少有效认证   |
| 404 | 请求的资源未找到      |
| 500 | 服务器错误，通常为内部错误 |