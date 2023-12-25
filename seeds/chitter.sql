CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    email TEXT,
    username VARCHAR(16),
    password TEXT
);

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE IF NOT EXISTS peeps (
    id SERIAL PRIMARY KEY,
    content VARCHAR(280),
    time_posted TIMESTAMP,
    user_id SMALLINT,
    CONSTRAINT fk_peep FOREIGN KEY (user_id)
        REFERENCES accounts(id)
        ON DELETE CASCADE
);