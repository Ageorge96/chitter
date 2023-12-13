from lib.peep import Peep
from datetime import datetime

def test_new_peep():
    peep = Peep(1, 'Peep', datetime(2023, 6, 20, 12, 30, 0), 2)
    
    assert peep.content == 'Peep'
    assert str(peep.time) == '2023-06-20 12:30:00'
    assert peep.user_id == 2