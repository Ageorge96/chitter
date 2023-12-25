from datetime import datetime

class Peep:

    def __init__(self, id, content, time_of_post, user_id):
        self.id = id
        self.content = content
        self.time_of_post = time_of_post
        self.user_id = user_id
        

    @property
    def time_of_post(self):
        return self._time_of_post
    
    @time_of_post.setter
    def time_of_post(self, time_of_post):
        dt_format = "%a, %d %B, %Y %H:%M:%S"

        if type(time_of_post) == str:
            datetime_format = datetime.strptime(time_of_post, "%Y-%m-%d %H:%M:%S")

            self._time_of_post = datetime_format.strftime(dt_format)
            #print(self._time_of_post)
            #print(type(self._time_of_post))
        else:
            print(type(time_of_post))
            self._time_of_post = time_of_post.strftime(dt_format)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Peep: {self.id} {self.content} {self.time_of_post} {self.user_id}"