from app.calculation import Calculation


def test_calculation_creation():
    calc = Calculation("add", 2, 3, 5)
    assert calc.operation == "add"
    assert calc.a == 2
    assert calc.b == 3
    assert calc.result == 5


def test_to_dict_and_from_dict():
    calc = Calculation("multiply", 4, 5, 20)
    data = calc.to_dict()
    new_calc = Calculation.from_dict(data)

    assert new_calc.operation == "multiply"
    assert new_calc.result == 20