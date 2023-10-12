INSERT INTO "user" (first_name, last_name, phone, password, email, cart_id, address_id) VALUES
  ('Alice', 'Johnson', '555-1111', 'password123', 'alice.johnson@example.com', 9, 15),
  ('Bob', 'Smith', '555-2222', 'password456', 'bob.smith@example.com', 10, 16),
  ('Charlie', 'Brown', '555-3333', 'password789', 'charlie.brown@example.com', 11, 17),
  ('David', 'Wilson', '555-4444', 'passwordabc', 'david.wilson@example.com', 12, 18);

INSERT INTO "category" (name, sort_order, parent_category_id) VALUES
  ('Category A', 1, NULL),
  ('Category B', 2, NULL),
  ('Subcategory A', 1, 1),
  ('Subcategory B', 2, 1),
  ('Subcategory C', 3, 2);

INSERT INTO "product" (price, name, quantity, category_id, product_image_id) VALUES
  (19.99, 'Product 1', 100, 1, '99eead52-3deb-4c38-90e6-4b35d0211bca'),
  (29.99, 'Product 2', 50, 2, 'a9b03524-eeac-464e-9389-744d37abdce1'),
  (39.99, 'Product 3', 70, 3, 'ad2712dc-9df9-4970-b9da-a493afc7314b'),
  (49.99, 'Product 4', 30, 4, '99eead52-3deb-4c38-90e6-4b35d0211bca');

INSERT INTO "cart_product" (quantity, cart_id, product_id) VALUES
  (2, 9, 1),
  (1, 9, 2),
  (3, 10, 3),
  (2, 10, 4),
  (1, 11, 1),
  (2, 11, 2),
  (3, 12, 3),
  (1, 12, 4);

INSERT INTO "order" (total_price, billing_address_id, shipping_address_id, user_id) VALUES
  (19.99, 15, 15, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (39.99, 15, 16, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (59.99, 16, 15, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (79.99, 16, 16, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (99.99, 17, 17, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (119.99, 17, 18, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (139.99, 18, 17, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (159.99, 18, 18, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (179.99, 15, 15, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (199.99, 15, 16, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (219.99, 16, 15, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (239.99, 16, 16, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (259.99, 17, 17, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (279.99, 17, 18, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (299.99, 18, 17, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (319.99, 18, 18, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b');

INSERT INTO "order_product" (product_price, quantity, product_id, order_id) VALUES
  (19.99, 2, 1, 22),
  (29.99, 3, 2, 22),
  (39.99, 1, 3, 22),
  (49.99, 2, 4, 23),
  (14.99, 5, 1, 23),
  (24.99, 3, 2, 23),
  (34.99, 2, 3, 24),
  (44.99, 1, 4, 24),
  (12.99, 4, 1, 24),
  (22.99, 2, 2, 24),
  (32.99, 3, 3, 18),
  (42.99, 1, 4, 18),
  (11.99, 3, 1, 18),
  (21.99, 2, 2, 19),
  (31.99, 4, 3, 19),
  (41.99, 2, 4, 19),
  (9.99, 1, 1, 20),
  (19.99, 2, 2, 20),
  (29.99, 1, 3, 21),
  (39.99, 3, 4, 21);