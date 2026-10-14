from simpleintrest import simple_intrest

def test_SI():
    assert simple_intrest(2000,6,10) == 1200

def test_SIZero():
    assert simple_intrest(10000,0,0) == 0   