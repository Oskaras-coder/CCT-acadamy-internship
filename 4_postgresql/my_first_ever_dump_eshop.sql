--
-- PostgreSQL database dump
--

-- Dumped from database version 13.12 (Debian 13.12-1.pgdg120+1)
-- Dumped by pg_dump version 13.12 (Debian 13.12-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: address; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.address (
    address_id integer NOT NULL,
    street character varying(100) NOT NULL,
    city character varying(60) NOT NULL,
    country character varying(100) NOT NULL,
    zip integer NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.address OWNER TO postgres;

--
-- Name: address_address_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.address_address_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.address_address_id_seq OWNER TO postgres;

--
-- Name: address_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.address_address_id_seq OWNED BY public.address.address_id;


--
-- Name: cart; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cart (
    cart_id integer NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.cart OWNER TO postgres;

--
-- Name: cart_cart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cart_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cart_cart_id_seq OWNER TO postgres;

--
-- Name: cart_cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart.cart_id;


--
-- Name: cart_product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cart_product (
    quantity integer,
    cart_id integer,
    product_id integer NOT NULL
);


ALTER TABLE public.cart_product OWNER TO postgres;

--
-- Name: cart_product_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cart_product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cart_product_product_id_seq OWNER TO postgres;

--
-- Name: cart_product_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cart_product_product_id_seq OWNED BY public.cart_product.product_id;


--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    category_id integer NOT NULL,
    name character varying(100) NOT NULL,
    sort_order integer NOT NULL,
    parent_category_id integer
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_category_id_seq OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_category_id_seq OWNED BY public.category.category_id;


--
-- Name: order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."order" (
    order_number integer NOT NULL,
    total_price numeric NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    billing_address_id integer,
    shipping_address_id integer,
    user_id uuid
);


ALTER TABLE public."order" OWNER TO postgres;

--
-- Name: order_order_number_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_order_number_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_order_number_seq OWNER TO postgres;

--
-- Name: order_order_number_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_order_number_seq OWNED BY public."order".order_number;


--
-- Name: order_product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_product (
    product_price numeric NOT NULL,
    quantity integer NOT NULL,
    product_id integer NOT NULL,
    order_id integer NOT NULL
);


ALTER TABLE public.order_product OWNER TO postgres;

--
-- Name: order_product_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_product_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_product_order_id_seq OWNER TO postgres;

--
-- Name: order_product_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_product_order_id_seq OWNED BY public.order_product.order_id;


--
-- Name: order_product_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.order_product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_product_product_id_seq OWNER TO postgres;

--
-- Name: order_product_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.order_product_product_id_seq OWNED BY public.order_product.product_id;


--
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    product_id integer NOT NULL,
    price numeric NOT NULL,
    name character varying(50) NOT NULL,
    quantity integer,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    category_id integer,
    product_image_id uuid
);


ALTER TABLE public.product OWNER TO postgres;

--
-- Name: product_image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_image (
    product_image_id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    image_name character varying(100) NOT NULL,
    url character varying(255) NOT NULL
);


ALTER TABLE public.product_image OWNER TO postgres;

--
-- Name: product_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_product_id_seq OWNER TO postgres;

--
-- Name: product_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_product_id_seq OWNED BY public.product.product_id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone character varying(50),
    password character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    cart_id integer NOT NULL,
    address_id integer
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: user_cart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_cart_id_seq OWNER TO postgres;

--
-- Name: user_cart_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_cart_id_seq OWNED BY public."user".cart_id;


--
-- Name: address address_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address ALTER COLUMN address_id SET DEFAULT nextval('public.address_address_id_seq'::regclass);


--
-- Name: cart cart_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart ALTER COLUMN cart_id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);


--
-- Name: cart_product product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_product ALTER COLUMN product_id SET DEFAULT nextval('public.cart_product_product_id_seq'::regclass);


--
-- Name: category category_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN category_id SET DEFAULT nextval('public.category_category_id_seq'::regclass);


--
-- Name: order order_number; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order" ALTER COLUMN order_number SET DEFAULT nextval('public.order_order_number_seq'::regclass);


--
-- Name: order_product product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product ALTER COLUMN product_id SET DEFAULT nextval('public.order_product_product_id_seq'::regclass);


--
-- Name: order_product order_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product ALTER COLUMN order_id SET DEFAULT nextval('public.order_product_order_id_seq'::regclass);


--
-- Name: product product_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product ALTER COLUMN product_id SET DEFAULT nextval('public.product_product_id_seq'::regclass);


--
-- Name: user cart_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN cart_id SET DEFAULT nextval('public.user_cart_id_seq'::regclass);


--
-- Data for Name: address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.address (address_id, street, city, country, zip, created_at, updated_at) FROM stdin;
15	123 Main St	Exampleville	Exampleland	12345	2023-10-12 11:33:47.773623+00	2023-10-12 11:33:47.773623+00
16	456 Elm St	Sampletown	Sampleland	67890	2023-10-12 11:33:47.773623+00	2023-10-12 11:33:47.773623+00
17	789 Oak St	Testville	Testland	10111	2023-10-12 11:33:47.773623+00	2023-10-12 11:33:47.773623+00
18	101 Pine St	Demo City	Demoland	54321	2023-10-12 11:33:47.773623+00	2023-10-12 11:33:47.773623+00
19	456 Elm St	Vilnius	Lithuania	13841	2023-10-13 11:55:26.500467+00	2023-10-13 11:55:26.500467+00
\.


--
-- Data for Name: cart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cart (cart_id, created_at, updated_at) FROM stdin;
9	2023-10-12 11:34:00.926572+00	2023-10-12 11:34:00.926572+00
10	2023-10-12 11:34:00.926572+00	2023-10-12 11:34:00.926572+00
11	2023-10-12 11:34:00.926572+00	2023-10-12 11:34:00.926572+00
12	2023-10-12 11:34:00.926572+00	2023-10-12 11:34:00.926572+00
13	2023-10-13 11:53:07.468546+00	2023-10-13 11:53:07.468546+00
\.


--
-- Data for Name: cart_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cart_product (quantity, cart_id, product_id) FROM stdin;
2	9	1
1	9	2
3	10	3
2	10	4
1	11	1
2	11	2
3	12	3
1	12	4
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (category_id, name, sort_order, parent_category_id) FROM stdin;
1	Category A	1	\N
2	Category B	2	\N
3	Subcategory A	1	1
4	Subcategory B	2	1
5	Subcategory C	3	2
\.


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."order" (order_number, total_price, created_at, billing_address_id, shipping_address_id, user_id) FROM stdin;
73	219.92	2023-10-13 08:09:10.756679+00	15	15	41373d4c-19e3-45e6-b0d6-819f5664fe67
74	119.98	2023-10-13 08:09:10.756679+00	15	16	870a50c7-ba3b-40e5-86c7-bb0c300f7a80
75	159.95	2023-10-13 08:09:10.756679+00	16	16	c577f1f1-cb30-4a75-9bb0-d700a0c97208
76	379.94	2023-10-13 08:09:10.756679+00	17	17	c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b
77	99.95	2023-10-13 08:09:10.756679+00	16	17	41373d4c-19e3-45e6-b0d6-819f5664fe67
78	159.97	2023-10-13 08:09:10.756679+00	17	16	870a50c7-ba3b-40e5-86c7-bb0c300f7a80
79	319.96	2023-10-13 08:09:10.756679+00	15	17	c577f1f1-cb30-4a75-9bb0-d700a0c97208
80	139.95	2023-10-13 08:09:10.756679+00	17	18	c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b
81	299.95	2023-10-13 08:09:10.756679+00	18	18	41373d4c-19e3-45e6-b0d6-819f5664fe67
82	119.97	2023-10-13 08:09:10.756679+00	18	17	870a50c7-ba3b-40e5-86c7-bb0c300f7a80
83	599.90	2023-10-13 08:09:10.756679+00	15	18	c577f1f1-cb30-4a75-9bb0-d700a0c97208
84	219.92	2023-10-13 08:09:10.756679+00	16	18	c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b
85	199.97	2023-10-13 08:09:10.756679+00	18	15	41373d4c-19e3-45e6-b0d6-819f5664fe67
86	219.93	2023-10-13 08:09:10.756679+00	18	16	870a50c7-ba3b-40e5-86c7-bb0c300f7a80
87	239.97	2023-10-13 08:09:10.756679+00	18	18	c577f1f1-cb30-4a75-9bb0-d700a0c97208
88	99.95	2023-10-13 08:09:10.756679+00	17	15	c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b
89	159.97	2023-10-13 08:09:10.756679+00	15	15	41373d4c-19e3-45e6-b0d6-819f5664fe67
90	319.96	2023-10-13 08:09:10.756679+00	16	16	870a50c7-ba3b-40e5-86c7-bb0c300f7a80
91	139.95	2023-10-13 08:09:10.756679+00	17	17	c577f1f1-cb30-4a75-9bb0-d700a0c97208
92	299.95	2023-10-13 08:09:10.756679+00	18	18	c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b
\.


--
-- Data for Name: order_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_product (product_price, quantity, product_id, order_id) FROM stdin;
19.99	5	1	73
39.99	3	2	73
59.99	2	3	74
79.99	1	4	75
19.99	4	1	75
39.99	2	2	76
59.99	1	3	76
79.99	3	4	76
19.99	5	1	77
39.99	1	2	78
59.99	2	3	78
79.99	4	4	79
19.99	3	1	80
39.99	2	2	80
59.99	5	3	81
79.99	1	4	82
19.99	2	1	82
39.99	3	2	83
59.99	4	3	83
79.99	3	4	84
19.99	5	1	85
39.99	3	2	85
59.99	2	3	86
79.99	1	4	87
19.99	4	1	87
39.99	2	2	87
59.99	1	3	87
79.99	3	4	88
19.99	5	1	89
39.99	1	2	90
59.99	2	3	91
79.99	4	4	91
19.99	3	1	92
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (product_id, price, name, quantity, created_at, updated_at, category_id, product_image_id) FROM stdin;
1	19.99	Cup	100	2023-10-12 11:47:45.157348+00	2023-10-12 11:47:45.157348+00	1	99eead52-3deb-4c38-90e6-4b35d0211bca
2	39.99	Fork	50	2023-10-12 11:47:45.157348+00	2023-10-12 11:47:45.157348+00	2	a9b03524-eeac-464e-9389-744d37abdce1
3	59.99	Spoon	70	2023-10-12 11:47:45.157348+00	2023-10-12 11:47:45.157348+00	3	ad2712dc-9df9-4970-b9da-a493afc7314b
4	79.99	Plate	30	2023-10-12 11:47:45.157348+00	2023-10-12 11:47:45.157348+00	4	99eead52-3deb-4c38-90e6-4b35d0211bca
\.


--
-- Data for Name: product_image; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_image (product_image_id, image_name, url) FROM stdin;
ad2712dc-9df9-4970-b9da-a493afc7314b	Image 1	https://example.com/image1.jpg
a9b03524-eeac-464e-9389-744d37abdce1	Image 2	https://example.com/image2.jpg
99eead52-3deb-4c38-90e6-4b35d0211bca	Image 3	https://example.com/image3.jpg
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, first_name, last_name, phone, password, email, created_at, updated_at, cart_id, address_id) FROM stdin;
41373d4c-19e3-45e6-b0d6-819f5664fe67	Alice	Johnson	555-1111	password123	alice.johnson@example.com	2023-10-12 11:36:04.400244+00	2023-10-12 11:36:04.400244+00	9	15
870a50c7-ba3b-40e5-86c7-bb0c300f7a80	Bob	Smith	555-2222	password456	bob.smith@example.com	2023-10-12 11:36:04.400244+00	2023-10-12 11:36:04.400244+00	10	16
c577f1f1-cb30-4a75-9bb0-d700a0c97208	Charlie	Brown	555-3333	password789	charlie.brown@example.com	2023-10-12 11:36:04.400244+00	2023-10-12 11:36:04.400244+00	11	17
c775ca4e-6a72-4153-8f9f-2fd5d0a0f90b	David	Wilson	555-4444	passwordabc	david.wilson@example.com	2023-10-12 11:36:04.400244+00	2023-10-12 11:36:04.400244+00	12	18
975795e8-3edb-4fda-a292-10769c97b092	Oskaras	Safinas	9192-2133	hehehe	os@example.com	2023-10-13 11:55:49.105791+00	2023-10-13 11:55:49.105791+00	13	19
\.


--
-- Name: address_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.address_address_id_seq', 19, true);


--
-- Name: cart_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cart_cart_id_seq', 13, true);


--
-- Name: cart_product_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cart_product_product_id_seq', 1, false);


--
-- Name: category_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_category_id_seq', 5, true);


--
-- Name: order_order_number_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_order_number_seq', 92, true);


--
-- Name: order_product_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_product_order_id_seq', 1, false);


--
-- Name: order_product_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.order_product_product_id_seq', 1, false);


--
-- Name: product_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_product_id_seq', 4, true);


--
-- Name: user_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_cart_id_seq', 1, false);


--
-- Name: address address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (address_id);


--
-- Name: cart cart_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (cart_id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (category_id);


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (order_number);


--
-- Name: product_image product_image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_image
    ADD CONSTRAINT product_image_pkey PRIMARY KEY (product_image_id);


--
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (product_id);


--
-- Name: user user_address_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_address_id_key UNIQUE (address_id);


--
-- Name: user user_cart_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_cart_id_key UNIQUE (cart_id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: cart_product cart_product_cart_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_product
    ADD CONSTRAINT cart_product_cart_id_fkey FOREIGN KEY (cart_id) REFERENCES public.cart(cart_id);


--
-- Name: cart_product cart_product_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_product
    ADD CONSTRAINT cart_product_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(product_id);


--
-- Name: category category_parent_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_parent_category_id_fkey FOREIGN KEY (parent_category_id) REFERENCES public.category(category_id);


--
-- Name: order order_billing_address_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_billing_address_id_fkey FOREIGN KEY (billing_address_id) REFERENCES public.address(address_id);


--
-- Name: order_product order_product_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product
    ADD CONSTRAINT order_product_order_id_fkey FOREIGN KEY (order_id) REFERENCES public."order"(order_number);


--
-- Name: order_product order_product_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_product
    ADD CONSTRAINT order_product_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.product(product_id);


--
-- Name: order order_shipping_address_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_shipping_address_id_fkey FOREIGN KEY (shipping_address_id) REFERENCES public.address(address_id);


--
-- Name: order order_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: product product_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(category_id);


--
-- Name: product product_product_image_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_product_image_id_fkey FOREIGN KEY (product_image_id) REFERENCES public.product_image(product_image_id);


--
-- Name: user user_address_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_address_id_fkey FOREIGN KEY (address_id) REFERENCES public.address(address_id);


--
-- Name: user user_cart_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_cart_id_fkey FOREIGN KEY (cart_id) REFERENCES public.cart(cart_id);


--
-- PostgreSQL database dump complete
--

