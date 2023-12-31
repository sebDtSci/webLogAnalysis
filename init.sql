CREATE TABLE e_commerce_logs (
    accessed_date TIMESTAMP,
    duration_secs INT,
    network_protocol VARCHAR(10),
    ip VARCHAR(15),
    bytes INT,
    accessed_from VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    country VARCHAR(3),
    membership VARCHAR(20),
    language VARCHAR(20),
    sales NUMERIC(10, 4),
    returned VARCHAR(3),
    returned_amount NUMERIC(10, 2),
    pay_method VARCHAR(20)
);
