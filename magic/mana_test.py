from magic import database
from magic import mana

def  test_simple():
    do_test('U', ['U'])
    do_test('{U}', ['U'])
    try:
        do_test('Not a mana symbol sequence', None)
        assert False
    except mana.InvalidManaCostException:
        assert True

def test_twobrid():
    do_test('2/W2/W2/W', ['2/W', '2/W', '2/W'])

def  test_twodigit():
    do_test('{15}', ['15'])

def test_gleemax():
    do_test('1000000', ['1000000'])

def test_x():
    do_test('X', ['X'])

def test_multicolor_x():
    do_test('XRB', ['X', 'R', 'B'])

def test_phyrexian():
    do_test('U/P', ['U/P'])

def test_porcelain_legionnaire():
    do_test('{2}{W/P}', ['2', 'W/P'])

def test_norns_annex():
    do_test('{3}{W/P}{W/P}', ['3', 'W/P', 'W/P'])

def test_slitherhead():
    do_test('{B/G}', ['B/G'])

def test_everything():
    rs = database.DATABASE.execute('SELECT name, mana_cost FROM face')
    for row in rs:
        if row['mana_cost']:
            print(row['name'])
            print(row['mana_cost'])
            mana.parse(row['mana_cost'])

def test_colors():
    assert mana.colors(['9', 'W', 'W', 'R']) == {'required': {'W', 'R'}, 'also': set()}
    assert mana.colors(['2/W', 'G', 'X']) == {'required': {'G'}, 'also': {'W'}}
    assert mana.colors(['U/P', 'R/P']) == {'required': set(), 'also': {'U', 'R'}}
    assert mana.colors(['X']) == {'required': set(), 'also': set()}
    assert mana.colors(['B/R']) == {'required': set(), 'also': {'B', 'R'}}

def do_test(s, expected):
    symbols = mana.parse(s)
    assert symbols == expected or print('\nInput: {s}\nExpected: {expected}\n  Actual: {actual}'.format(s=s, expected=expected, actual=symbols))
