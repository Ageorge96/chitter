class UserdataRepository:
    def __init__(self, connection):
        self.connection = connection

    def new_user(self, username, email, password):
        self.connection.execute("INSERT INTO userdata (username, email, password) VALUES (%s, %s, %s)", [username, email, password])