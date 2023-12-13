from .peep import Peep

class PeepRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM peeps')

        peeps = []

        for row in rows:
            peep = Peep(row['id'], row['content'], row['time_posted'], row['user_id'])
            peeps.append(peep)

        return peeps
    
    def create(self, peep):
        self._connection.execute('INSERT INTO peeps (content, time_posted, user_id) VALUES (%s, %s, %s)', [peep.content, peep.time, peep.user_id])