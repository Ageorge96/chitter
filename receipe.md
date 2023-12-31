## STRAIGHT UP

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

## HARDER

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

## ADVANCED

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep



## Additional Notes
- You don't have to be logged in to see the peeps.
- Users sign up to chitter with their email, password, name and a username (e.g. samm@makersacademy.com, password123, Sam Morgan, sjmog).
- The username and email are unique.
- Peeps (posts to chitter) have the name of the user and their user handle.
- Your README should indicate the technologies used, and give instructions on how to install and run the tests.


nouns:
peep(post)
chitter
time
log in

Records  | Properties
peeps    | content, time
accounts | email, username, password


1. Can one peep have many accounts? No
2. Can one account have many peeps? Yes

-> Therefore,
-> An account HAS MANY peeps
-> An peep BELONGS TO an account

-> Therefore, the foreign key is on the peep table.


Table: peeps
id: serial
content: text
time_posted: datetime
user_id

Table: accounts
id: serial
email: text
username: varchar(16)
password:text





# SQL

CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    content VARCHAR(280),
    time_posted DATETIME,
    user_id VARCHAR(MAX)
)

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email TEXT,
    username VARCHAR(16),
    password TEXT
)

# Example tests


# ////////////////
# ////////////////

# Routes

#home page 
(index.html)
'/'

#sign up page
(sign_up.html)
'/sign_up

#login page
(login.html)
'/login'

#create post
(post.html)
'/make_post'

