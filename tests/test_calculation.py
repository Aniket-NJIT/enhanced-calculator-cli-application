from app.calculation import Calculation

def test_calculation_instantiation():
    calc = Calculation("add", 5, 5, 10)
    assert calc.operation == "add"
    assert calc.operand_a == 5
    assert calc.operand_b == 5
    assert calc.result == 10
    assert calc.timestamp is not None  # Timestamp should be auto-generated

def test_calculation_to_dict():
    calc = Calculation("subtract", 10, 5, 5)
    calc_dict = calc.to_dict()
    assert calc_dict["operation"] == "subtract"
    assert calc_dict["result"] == 5