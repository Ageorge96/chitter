from lib.peeps_repo import PeepRepository, Peep
from datetime import datetime

def test_get_all_peeps(db_connection):
    db_connection.seed('seeds/test_chitter.sql')
    repo = PeepRepository(db_connection)
    peeps = repo.all()

    assert peeps == [
        Peep(1, 'My first peep', datetime(2023, 1, 12, 12, 30, 0), 1),
        Peep(2, 'WATCH A CHILD FALL INTO A LAMPPOST!! XD', datetime(2023, 2, 11, 9, 12, 0), 2),
        Peep(3, 'Any one been to that new chicken place in soho', datetime(2023, 5, 28, 11, 8, 0), 3),
        Peep(4, 'Feelinf a bit down today. Cant wait for tomorrow', datetime(2023, 5, 28, 16, 50, 0), 4),
        Peep(5, "Chitter doesnt feel the same", datetime(2023, 6, 20, 12, 30, 0), 1),
        Peep(6, 'Bearnado 4 sucked', datetime(2023, 7, 20, 18, 8, 0), 3),
        Peep(7, 'Any one else got their tickets yet', datetime(2023, 6, 9, 13, 37, 51), 5),
        Peep(8, 'Running away tonight', datetime(2023, 4, 21, 14, 53, 0), 2),
        Peep(9, 'Why cant my whole life be gamimg lol', datetime(2023, 6, 20, 12,30, 0), 6),
        Peep(10, 'Now my birthday is done im ready for Christmas!', datetime(2023, 6, 20, 12, 30, 0), 2),
        Peep(11, 'Someone save me from this uni lecture', datetime(2023, 6, 20, 12, 30, 0), 3)
    ]

def test_add_peep(db_connection):
    db_connection.seed('seeds/test_chitter.sql')
    repo = PeepRepository(db_connection)

    peep = Peep(None, 'First trip to the gym in 7 years, abosolutely shambolic performance', datetime(2023, 7, 13, 17, 43, 23), 5)
    repo.create(peep)

    peeps = repo.all()
    assert peeps == [
        Peep(1, 'My first peep', datetime(2023, 1, 12, 12, 30, 0), 1),
        Peep(2, 'WATCH A CHILD FALL INTO A LAMPPOST!! XD', datetime(2023, 2, 11, 9, 12, 0), 2),
        Peep(3, 'Any one been to that new chicken place in soho', datetime(2023, 5, 28, 11, 8, 0), 3),
        Peep(4, 'Feelinf a bit down today. Cant wait for tomorrow', datetime(2023, 5, 28, 16, 50, 0), 4),
        Peep(5, "Chitter doesnt feel the same", datetime(2023, 6, 20, 12, 30, 0), 1),
        Peep(6, 'Bearnado 4 sucked', datetime(2023, 7, 20, 18, 8, 0), 3),
        Peep(7, 'Any one else got their tickets yet', datetime(2023, 6, 9, 13, 37, 51), 5),
        Peep(8, 'Running away tonight', datetime(2023, 4, 21, 14, 53, 0), 2),
        Peep(9, 'Why cant my whole life be gamimg lol', datetime(2023, 6, 20, 12,30, 0), 6),
        Peep(10, 'Now my birthday is done im ready for Christmas!', datetime(2023, 6, 20, 12, 30, 0), 2),
        Peep(11, 'Someone save me from this uni lecture', datetime(2023, 6, 20, 12, 30, 0), 3),
        Peep(12, 'First trip to the gym in 7 years, abosolutely shambolic performance', datetime(2023, 7, 13, 17, 43, 23), 5)
    ]