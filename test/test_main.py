# content of test_sample.py
# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5


from main import calc_co2_emitted_driving, calc_co2_beef, calc_co2_chicken,\
    calc_co2_coffee


def test_co2_emitted_driving():
    assert calc_co2_emitted_driving(100,45) == 19.75

def test_co2_beef():
    assert calc_co2_beef(1) == 40.2

def test_co2_chicken():
    assert calc_co2_chicken(1) == 6.9
