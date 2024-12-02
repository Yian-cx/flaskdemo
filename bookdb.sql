create table books
(
    id               int auto_increment
        primary key,
    title            varchar(255)  not null,
    author           varchar(255)  not null,
    publication_date date          null,
    isbn             varchar(255)  null,
    total_copies     int default 0 null,
    available_copies int default 0 null,
    constraint isbn
        unique (isbn)
);

create table categories
(
    id          int auto_increment
        primary key,
    name        varchar(100) not null,
    description varchar(255) null,
    constraint name
        unique (name)
);

create table logs
(
    id         int auto_increment
        primary key,
    user_id    int                                 not null,
    action     varchar(100)                        not null,
    details    varchar(255)                        null,
    ip_address varchar(50)                         null,
    status     varchar(50)                         not null,
    resource   varchar(100)                        not null,
    created_at timestamp default CURRENT_TIMESTAMP null
);

create table users
(
    id         int auto_increment
        primary key,
    username   varchar(255)                        not null,
    password   varchar(255)                        not null,
    email      varchar(255)                        null,
    created_at timestamp default CURRENT_TIMESTAMP null,
    constraint email
        unique (email),
    constraint username
        unique (username)
);

create table reviews
(
    id          int auto_increment
        primary key,
    user_id     int                                 not null,
    book_id     int                                 not null,
    review_text text                                null,
    rating      int                                 null,
    created_at  timestamp default CURRENT_TIMESTAMP null,
    constraint reviews_ibfk_1
        foreign key (user_id) references users (id),
    constraint reviews_ibfk_2
        foreign key (book_id) references books (id),
    check ((`rating` >= 1) and (`rating` <= 5))
);

create index book_id
    on reviews (book_id);

create index user_id
    on reviews (user_id);

-- Insert data into books table
INSERT INTO books (title, author, publication_date, isbn, total_copies, available_copies) VALUES
('Book Title 1', 'Author Name 1', '2021-01-01', '1234567890123', 10, 10),
('Book Title 2', 'Author Name 2', '2021-02-01', '1234567890124', 8, 8),
('Book Title 3', 'Author Name 3', '2021-03-01', '1234567890125', 5, 5),
('Book Title 4', 'Author Name 4', '2021-04-01', '1234567890126', 7, 7),
('Book Title 5', 'Author Name 5', '2021-05-01', '1234567890127', 6, 6);

-- Insert data into categories table
INSERT INTO categories (name, description) VALUES
('Category 1', 'Description for Category 1'),
('Category 2', 'Description for Category 2'),
('Category 3', 'Description for Category 3'),
('Category 4', 'Description for Category 4'),
('Category 5', 'Description for Category 5');

-- Insert data into logs table
INSERT INTO logs (user_id, action, details, ip_address, status, resource) VALUES
(1, 'CREATE', 'Log entry 1', '192.168.1.1', 'SUCCESS', 'Resource 1'),
(2, 'UPDATE', 'Log entry 2', '192.168.1.2', 'SUCCESS', 'Resource 2'),
(3, 'DELETE', 'Log entry 3', '192.168.1.3', 'SUCCESS', 'Resource 3'),
(4, 'CREATE', 'Log entry 4', '192.168.1.4', 'ERROR', 'Resource 4'),
(5, 'UPDATE', 'Log entry 5', '192.168.1.5', 'SUCCESS', 'Resource 5');

-- Insert data into users table
INSERT INTO users (username, password, email) VALUES
('user1', 'password1', 'user1@example.com'),
('user2', 'password2', 'user2@example.com'),
('user3', 'password3', 'user3@example.com'),
('user4', 'password4', 'user4@example.com'),
('user5', 'password5', 'user5@example.com');

-- Insert data into reviews table
INSERT INTO reviews (user_id, book_id, review_text, rating) VALUES
(1, 1, 'Great book!', 5),
(2, 2, 'Loved it!', 4),
(3, 3, 'Not bad.', 3),
(4, 4, 'Could be better.', 2),
(5, 5, 'Not my cup of tea.', 1);