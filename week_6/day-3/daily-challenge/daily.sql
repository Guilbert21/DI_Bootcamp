-- part 1 

-- 1
-- CREATE TABLE Customer (
--   id SERIAL PRIMARY KEY,
--   first_name VARCHAR(50),
--   last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE Customer_profile (
--   id SERIAL PRIMARY KEY,
--   isLoggedIn BOOLEAN DEFAULT false,
--   customer_id INTEGER REFERENCES Customer(id)
-- );

-- 2
-- INSERT INTO Customer (first_name, last_name) VALUES
--   ('John', 'Doe'),
--   ('Jerome', 'Lalu'),
--   ('Lea', 'Rive');

-- 3
-- INSERT INTO Customer_profile (isLoggedIn, customer_id) VALUES
--   (true, (SELECT id FROM Customer WHERE first_name = 'John')),
--   (false, (SELECT id FROM Customer WHERE first_name = 'Jerome')),
--   (false, (SELECT id FROM Customer WHERE first_name = 'Lea'));


-- 4
--   SELECT Customer.first_name 
-- FROM Customer
-- JOIN Customer_profile 
-- ON Customer.id = Customer_profile.customer_id 
-- WHERE Customer_profile.isLoggedIn = true;

-- part 2  

-- 1
-- CREATE TABLE Book (
--   book_id SERIAL PRIMARY KEY,
--   title VARCHAR(100) NOT NULL,
--   author VARCHAR(100) NOT NULL
-- );

-- 2
-- INSERT INTO Book (title, author) VALUES
--   ('Alice In Wonderland', 'Lewis Carroll'),
--   ('Harry Potter', 'J.K Rowling'),
--   ('To kill a mockingbird', 'Harper Lee');

-- 3
-- CREATE TABLE Student (
--   student_id SERIAL PRIMARY KEY,
--   name VARCHAR(50) NOT NULL UNIQUE,
--   age INTEGER NOT NULL CHECK (age <= 15)
-- );

-- 4
-- INSERT INTO Student (name, age) VALUES
--   ('John', 12),
--   ('Lera', 11),
--   ('Patrick', 10),
--   ('Bob', 14);

-- 5
-- CREATE TABLE Library (
--   book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--   student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--   borrowed_date DATE,
--   PRIMARY KEY (book_fk_id, student_fk_id)
-- );