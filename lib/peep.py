from datetime import datetime

class Peep:

    def __init__(self, id, content, time, user_id):
        self.id = id
        self.content = content
        self.time = time
        self.user_id = user_id

    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time):
        if type(time) == str:
            self._time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            print(self._time)
            print(type(self._time))
        else:
            self._time = time

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Peep: {self.id} {self.content} {self.time} {self.user_id}"