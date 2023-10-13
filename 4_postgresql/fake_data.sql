INSERT INTO "user" (first_name, last_name, phone, password, email, cart_id, address_id) VALUES
  ('Alice', 'Johnson', '555-1111', 'password123', 'alice.johnson@example.com', 9, 15),
  ('Bob', 'Smith', '555-2222', 'password456', 'bob.smith@example.com', 10, 16),
  ('Charlie', 'Brown', '555-3333', 'password789', 'charlie.brown@example.com', 11, 17),
  ('David', 'Wilson', '555-4444', 'passwordabc', 'david.wilson@example.com', 12, 18);

INSERT INTO "cart" DEFAULT VALUES;
INSERT INTO "cart" DEFAULT VALUES;
INSERT INTO "cart" DEFAULT VALUES;
INSERT INTO "cart" DEFAULT VALUES;

INSERT INTO "category" (name, sort_order, parent_category_id) VALUES
  ('Category A', 1, NULL),
  ('Category B', 2, NULL),
  ('Subcategory A', 1, 1),
  ('Subcategory B', 2, 1),
  ('Subcategory C', 3, 2);

INSERT INTO "product" (price, name, quantity, category_id, product_image_id) VALUES
  (19.99, 'Cups', 100, 1, '99eead52-3deb-4c38-90e6-4b35d0211bca'),
  (29.99, 'Spoons', 50, 2, 'a9b03524-eeac-464e-9389-744d37abdce1'),
  (39.99, 'Knives', 70, 3, 'ad2712dc-9df9-4970-b9da-a493afc7314b'),
  (49.99, 'Plates', 30, 4, '99eead52-3deb-4c38-90e6-4b35d0211bca');

INSERT INTO "cart_product" (quantity, cart_id, product_id) VALUES
  (2, 9, 1),
  (1, 9, 2),
  (3, 10, 3),
  (2, 10, 4),
  (1, 11, 1),
  (2, 11, 2),
  (3, 12, 3),
  (1, 12, 4);


INSERT INTO "product_image" (image_name, url) VALUES
  ('Image 1', 'https://example.com/image1.jpg'),
  ('Image 2', 'https://example.com/image2.jpg'),
  ('Image 3', 'https://example.com/image3.jpg');


INSERT INTO "order" (total_price, billing_address_id, shipping_address_id, user_id)
VALUES
  (219.92, 15, 15, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (119.98, 15, 16, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (159.95, 16, 16, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (379.94, 17, 17, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (99.95, 16, 17, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (159.97, 17, 16, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (319.96, 15, 17, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (139.95, 17, 18, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (299.95, 18, 18, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (119.97, 18, 17, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (599.90, 15, 18, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (219.92, 16, 18, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (199.97, 18, 15, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (219.93, 18, 16, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (239.97, 18, 18, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (99.95, 17, 15, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b'),
  (159.97, 15, 15, '41373d4c-19e3-45e6-b0d6-819f5664fe67'),
  (319.96, 16, 16, '870a50c7-ba3b-40e5-86c7-bb0c300f7a80'),
  (139.95, 17, 17, 'c577f1f1-cb30-4a75-9bb0-d700a0c97208'),
  (299.95, 18, 18, 'c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b');

INSERT INTO "order_product" (product_price, quantity, product_id, order_id) VALUES
  (19.99, 5, 1, 73),
  (39.99, 3, 2, 73),
  (59.99, 2, 3, 74),
  (79.99, 1, 4, 75),
  (19.99, 4, 1, 75),
  (39.99, 2, 2, 76),
  (59.99, 1, 3, 76),
  (79.99, 3, 4, 76),
  (19.99, 5, 1, 77),
  (39.99, 1, 2, 78),
  (59.99, 2, 3, 78),
  (79.99, 4, 4, 79),
  (19.99, 3, 1, 80),
  (39.99, 2, 2, 80),
  (59.99, 5, 3, 81),
  (79.99, 1, 4, 82),
  (19.99, 2, 1, 82),
  (39.99, 3, 2, 83),
  (59.99, 4, 3, 83),
  (79.99, 3, 4, 84),
  (19.99, 5, 1, 85),
  (39.99, 3, 2, 85),
  (59.99, 2, 3, 86),
  (79.99, 1, 4, 87),
  (19.99, 4, 1, 87),
  (39.99, 2, 2, 87),
  (59.99, 1, 3, 87),
  (79.99, 3, 4, 88),
  (19.99, 5, 1, 89),
  (39.99, 1, 2, 90),
  (59.99, 2, 3, 91),
  (79.99, 4, 4, 91),
  (19.99, 3, 1, 92);