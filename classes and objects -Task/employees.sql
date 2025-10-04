-- Create the Employees table
DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    join_date DATE
);

INSERT INTO Employees (id, name, department, salary, join_date) VALUES
(101, 'Teju', 'IT', 70000, '2022-05-14'),
(102, 'poji', 'HR', 85000, '2023-01-20'),
(103, 'lokshit', 'Finance', 95000, '2023-08-12'),
(104, 'yashu', 'IT', 88000, '2024-02-01'),
(105, 'vyshu', 'HR', 60000, '2023-09-05');
--query 1
UPDATE Employees
SET salary = salary * 1.10
WHERE id = 101;

SELECT 'Query 1 – Employee 101 salary increased by 10%' AS Info;
SELECT * FROM Employees WHERE id = 101;
--query 2
INSERT INTO Employees (id, name, department, salary, join_date)
VALUES 
(107, 'Varsha', 'IT', 75000, '2023-05-10'),
(108, 'siva', 'HR', 68000, '2022-11-20'),
(109, 'Ravi', 'Finance', 82000, '2024-03-01');
SELECT 'Query 2 – After inserting multiple rows' AS Info;
SELECT * FROM Employees;
--query 3
ALTER TABLE Employees ADD email VARCHAR(100);
SELECT 'Query 3 – Added email column (success)' AS Info;
PRAGMA table_info(Employees);
--query 4
SELECT 'Query 4 – Employees earning more than average salary' AS Info;
SELECT * 
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
--query 5
SELECT 'Query 5 – Employees with second highest salary' AS Info;
SELECT * 
FROM Employees
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE salary < (SELECT MAX(salary) FROM Employees)
);
--query 6
SELECT 'Query 6 – Employees whose names start with V' AS Info;
SELECT * 
FROM Employees
WHERE name LIKE 'V%';
--query 7
SELECT 'Query 7 – Count of employees joined in 2023' AS Info;
SELECT COUNT(*) AS employees_joined_2023
FROM Employees
WHERE strftime('%Y', join_date) = '2023';
--query 8
SELECT 'Query 8 – Employees earning > 80 000 in IT or HR' AS Info;
SELECT * 
FROM Employees
WHERE salary > 80000 
  AND department IN ('IT', 'HR');
