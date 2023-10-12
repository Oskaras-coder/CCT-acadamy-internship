CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE "address" (
    address_id SERIAL PRIMARY KEY,
    street VARCHAR(100) NOT NULL,
    city VARCHAR(60) NOT NULL,
    country VARCHAR(100) NOT NULL,
    zip INTEGER NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE "cart" (
    cart_id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE "user" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    cart_id SERIAL UNIQUE,
    address_id INTEGER UNIQUE,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$'),
    FOREIGN KEY (cart_id) REFERENCES "cart"(cart_id),
    FOREIGN KEY (address_id) REFERENCES "address"(address_id)
);


CREATE TABLE "product_image" (
    product_image_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    image_name VARCHAR(100) NOT NULL,
    url VARCHAR(255) NOT NULL
);


CREATE TABLE "category" (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sort_order INTEGER NOT NULL,
    parent_category_id INTEGER,
    FOREIGN KEY (parent_category_id) REFERENCES "category"(category_id)
);


CREATE TABLE "product" (
    product_id SERIAL PRIMARY KEY,
    price DECIMAL NOT NULL,
    name VARCHAR(50) NOT NULL,
    quantity INTEGER,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    category_id INTEGER,
    product_image_id UUID,
    FOREIGN KEY (category_id) REFERENCES "category"(category_id),
    FOREIGN KEY (product_image_id) REFERENCES "product_image"(product_image_id)
);


CREATE TABLE "cart_product" (
    quantity INTEGER,
    cart_id INTEGER,
    product_id SERIAL,
    FOREIGN KEY (cart_id) REFERENCES "cart"(cart_id),
    FOREIGN KEY (product_id) REFERENCES "product"(product_id)
);


CREATE TABLE "order" (
    order_number SERIAL PRIMARY KEY,
    total_price DECIMAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    billing_address_id INTEGER,
    shipping_address_id INTEGER,
    user_id UUID,
    FOREIGN KEY (billing_address_id) REFERENCES "address"(address_id),
    FOREIGN KEY (shipping_address_id) REFERENCES "address"(address_id),
    FOREIGN KEY (user_id) REFERENCES "user"(id)
);


CREATE TABLE "order_product" (
    product_price DECIMAL NOT NULL,
    quantity INTEGER NOT NULL,
    product_id SERIAL,
    order_id SERIAL,
    FOREIGN KEY (product_id) REFERENCES "product"(product_id),
    FOREIGN KEY (order_id) REFERENCES "order"(order_number)
);


-- Functions

SELECT *
FROM "user"
WHERE created_at >= NOW() - INTERVAL '1 month'
ORDER BY email DESC;

SELECT *
FROM "order"
ORDER BY total_price DESC
LIMIT 10;

SELECT SUM(total_price) AS total_sum
FROM "order"
WHERE created_at >= DATE_TRUNC('month', NOW()) - INTERVAL '1 month'
  AND created_at < DATE_TRUNC('month', NOW());

SELECT u.*, o.*
FROM "user" u
JOIN "order" o ON u.id = o.user_id
WHERE u.id = user_id
ORDER BY o.created_at DESC;