-- 创建商品表
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL
);

-- 创建商品特征表（未启用）
CREATE TABLE IF NOT EXISTS ProductFeature (
    product_id INTEGER NOT NULL,
    feature TEXT NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(id)
);

-- 创建会员表
CREATE TABLE IF NOT EXISTS Member (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    balance REAL NOT NULL,
    register_date DATE NOT NULL,
    last_date DATE NOT NULL,
    eye_left REAL NOT NULL,
    eye_right REAL NOT NULL,
    pupil REAL NOT NULL
);

-- 创建订单表
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    create_date DATE NOT NULL,
    member_id INTEGER,
    total_price REAL NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Member(id)
);

-- 规则表
CREATE TABLE IF NOT EXISTS RechargeRules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INTEGER UNIQUE,
    bonus INTEGER
);

-- 创建管理员表
CREATE TABLE IF NOT EXISTS Admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- 测试数据
-- 插入商品信息
INSERT INTO Product (name, price) VALUES ('Glasses Model A', 150.0);
INSERT INTO Product (name, price) VALUES ('Glasses Model B', 200.0);
INSERT INTO Product (name, price) VALUES ('Glasses Model C', 250.0);
INSERT INTO Product (name, price) VALUES ('Glasses Model D', 300.0);
INSERT INTO Product (name, price) VALUES ('Glasses Model E', 350.0);

-- 插入商品特征信息
INSERT INTO ProductFeature (product_id, feature, value) VALUES (1, '{Weight: 28.0, Color: Red}', 30.5);
INSERT INTO ProductFeature (product_id, feature, value) VALUES (2, '{Weight: 30.0, Color: Blue}', 28.0);
INSERT INTO ProductFeature (product_id, feature, value) VALUES (2, '{Weight: 8.0, Color: Green}', 25.0);
INSERT INTO ProductFeature (product_id, feature, value) VALUES (3, '{Weight: 98.0, Color: Black}', 32.0);
INSERT INTO ProductFeature (product_id, feature, value) VALUES (3, '{Weight: 58.0, Color: White}', 27.5);

-- 插入会员信息
INSERT INTO Member (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil)
VALUES ('Alice', '1234567890', 100.0, '2024-06-07', '2024-06-10', 1.0, 1.0, 2.5);
INSERT INTO Member (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil)
VALUES ('Bob', '0987654321', 200.0, '2024-06-07', '2024-06-10', 0.9, 1.1, 2.4);
INSERT INTO Member (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil)
VALUES ('Charlie', '1122334455', 150.0, '2024-06-08', '2024-06-10', 1.2, 1.0, 2.6);
INSERT INTO Member (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil)
VALUES ('David', '2233445566', 180.0, '2024-06-09', '2024-06-10', 0.8, 1.0, 2.3);
INSERT INTO Member (name, phone, balance, register_date, last_date, eye_left, eye_right, pupil)
VALUES ('Eve', '3344556677', 250.0, '2024-06-09', '2024-06-10', 1.1, 1.1, 2.7);

-- 插入订单信息
INSERT INTO Orders (create_date, member_id, total_price)
VALUES ('2023-06-01', 1, 150.0);
INSERT INTO Orders (create_date, member_id, total_price)
VALUES ('2023-06-02', 2, 200.0);
INSERT INTO Orders (create_date, member_id, total_price)
VALUES ('2023-06-03', 3, 250.0);
INSERT INTO Orders (create_date, member_id, total_price)
VALUES ('2023-06-04', 4, 300.0);
INSERT INTO Orders (create_date, member_id, total_price)
VALUES ('2023-06-05', 5, 350.0);

INSERT INTO Admin (id, username, password) VALUES (0, 'admin', 'password');
INSERT INTO Admin (username, password) VALUES ('saler', 'password');
