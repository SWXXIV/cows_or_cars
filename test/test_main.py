# content of test_sample.py
# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(3) == 5


from main import calc_co2_emitted_driving,\
    calc_co2_beef,\
    calc_co2_chicken,\
    calc_co2_coffee,\
    calc_beef_equivalent,\
    calc_vehicle_equivalent,\
    calc_chicken_equivalent


def test_calc_co2_emitted_driving():
    assert calc_co2_emitted_driving(100,45) == 19.75

def test_calc_co2_beef():
    assert calc_co2_beef(1) == 40.2

def test_calc_co2_chicken():
    assert calc_co2_chicken(1) == 6.9

def test_calc_co2_coffee():
    assert calc_co2_coffee(10) == 0.07

def test_calc_chicken_equivalent():
    assert calc_chicken_equivalent(10) == 1.45

def test_calc_beef_equivalent():
    assert calc_beef_equivalent(10) == 0.25

def test_calc_vehicle_equivalent():
    assert calc_vehicle_equivalent(100, 45) == 555.56
