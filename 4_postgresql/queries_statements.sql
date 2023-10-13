--3.1. Get all users who were created within the last month and sorted by their emails from Z to A order
SELECT *
FROM "user"
WHERE created_at >= NOW() - INTERVAL '1 month'
ORDER BY email DESC;

--3.2. Get top 10 biggest orders within the system
SELECT *
FROM "order"
ORDER BY total_price DESC
LIMIT 10;

--3.3. Get a total sum of last month's orders
SELECT SUM(total_price) AS total_sum
FROM "order"
WHERE created_at >= DATE_TRUNC('month', NOW()) - INTERVAL '1 month'

--3.4. Select specific user with all his orders together ordered by order date descending

SELECT u.id AS user_id, u.first_name, u.last_name, o.order_number, o.created_at, o.total_price
FROM "user" u
JOIN "order" o ON u.id = o.user_id
WHERE u.id = '41373d4c-19e3-45e6-b0d6-819f5664fe67'
ORDER BY o.created_at DESC;