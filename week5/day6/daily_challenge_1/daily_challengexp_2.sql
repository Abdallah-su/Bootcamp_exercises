CREATE TABLE product_orders(order_id SERIAL PRIMARY KEY);
CREATE TABLE items (item_id SERIAL PRIMARY KEY, order_id INTEGER REFERENCES product_orders(order_id), 
product_name TEXT NOT NULL, price DECIMAL NOT NULL, quantity INTEGER NOT NULL);
CREATE FUNCTION order_cost(target_order_id INT)
RETURNS DECIMAL AS $$
DECLARE 
 total_price DECIMAL;
BEGIN
 SELECT SUM(quantity * price) INTO total_price FROM items WHERE order_id =target_order_id;
 RETURN total_price;
END ;
$$ LANGUAGE plpgsql;

CREATE TABLE users (user_id SERIAL PRIMARY KEY, order_id INTEGER REFERENCES product_orders(order_id));
CREATE FUNCTION user_cost(target_user_id INT)
RETURN DECIMAL AS $$
DECLARE 
 total_user_cost DECIMAL;
BEGIN
 SELECT SUM (price * quantity) FROM product_orders where order_id =target_user_id;
 RETURN total_user_cost;
END;
$$ LANGUAGE plpgsql;
 