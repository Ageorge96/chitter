CREATE SEQUENCE IF NOT EXISTS userdata_id_seq;
CREATE TABLE IF NOT EXISTS userdata (
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
        REFERENCES userdata(id)
        ON DELETE CASCADE
);