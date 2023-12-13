DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;


CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email TEXT,
    username VARCHAR(16),
    password TEXT
);

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    content VARCHAR(280),
    time_posted TIMESTAMP,
    user_id SMALLINT,
    CONSTRAINT fk_peep FOREIGN KEY (user_id)
        REFERENCES accounts(id)
        ON DELETE CASCADE
);


INSERT INTO accounts (email, username, password) VALUES
    ('Burgerpun@gotmail.com', 'SirPun', 'Q1w2e3r4'),
    ('Keyorpeele@hotmail.com', 'Keytle', 'L1k2j3h4'),
    ('Brusch@gotmail.com', 'Comby', 'Brusch92'),
    ('maliao1@hotmail.com','Presigirl', 'avocadoToast22'),
    ('loganbb@hotmail.co.uk', 'LoGoon', 'Viper98king'),
    ('Missmenot@gotmail.com', 'Cowboybebop', 'Sandwich72');


INSERT INTO peeps (content, time_posted, user_id) VALUES
    ('My first peep', '2023-01-12 12:30:00', 1),
    ('WATCH A CHILD FALL INTO A LAMPPOST!! XD', '2023-02-11 09:12:00', 2),
    ('Any one been to that new chicken place in soho', '2023-05-28 11:08:00', 3),
    ('Feelinf a bit down today. Cant wait for tomorrow', '2023-05-28 16:50:00', 4),
    ('Chitter doesnt feel the same', '2023-06-20 12:30:00', 1),
    ('Bearnado 4 sucked', '2023-07-20 18:08:00', 3),
    ('Any one else got their tickets yet', '2023-06-09 13:37:51', 5),
    ('Running away tonight', '2023-04-21 14:53:00', 2),
    ('Why cant my whole life be gamimg lol', '2023-06-20 12:30:00', 6),
    ('Now my birthday is done im ready for Christmas!', '2023-06-20 12:30:00', 2),
    ('Someone save me from this uni lecture', '2023-06-20 12:30:00', 3);