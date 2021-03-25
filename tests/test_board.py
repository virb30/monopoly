from monopoly import Board, Player, RealState


def test_init():
    players = ()
    properties = ()
    b = Board(players, properties, bonus=1)

    assert b.players == {}
    assert b.properties == ()
    assert b.bonus == 1


def test_move():
    p = Player(0)
    r = RealState(100, 10)
    b = Board([p], [r])

    assert b.move(p, 1) == r

    assert b.move(p, 1) == r
    assert p.balance == 100


def test_len():
    r = RealState(100, 10)
    b = Board([], [r])

    assert len(b) == 1


def test_remove():
    p = Player(0)
    b = Board([p], [])

    b.remove(p)
    assert len(b.players) == 0


