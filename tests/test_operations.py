import pytest
from app.operations import OperationFactory
from app.exceptions import OperationError

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (-1, 1, 0),
    (0.5, 0.5, 1.0)
])
def test_add(a, b, expected):
    op = OperationFactory.get_operation("add")
    assert op.execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (0, 5, -5)
])
def test_subtract(a, b, expected):
    op = OperationFactory.get_operation("subtract")
    assert op.execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10)
])
def test_multiply(a, b, expected):
    op = OperationFactory.get_operation("multiply")
    assert op.execute(a, b) == expected

def test_divide():
    op = OperationFactory.get_operation("divide")
    assert op.execute(10, 2) == 5.0
    with pytest.raises(OperationError):
        op.execute(10, 0)

def test_power():
    op = OperationFactory.get_operation("power")
    assert op.execute(2, 3) == 8

def test_root():
    op = OperationFactory.get_operation("root")
    assert op.execute(9, 2) == 3.0
    with pytest.raises(OperationError):
        op.execute(9, 0)
    with pytest.raises(OperationError):
        op.execute(-9, 2)

def test_modulus():
    op = OperationFactory.get_operation("modulus")
    assert op.execute(10, 3) == 1
    with pytest.raises(OperationError):
        op.execute(10, 0)

def test_int_divide():
    op = OperationFactory.get_operation("int_divide")
    assert op.execute(10, 3) == 3
    with pytest.raises(OperationError):
        op.execute(10, 0)

def test_percent():
    op = OperationFactory.get_operation("percent")
    assert op.execute(50, 200) == 25.0
    with pytest.raises(OperationError):
        op.execute(50, 0)

def test_abs_diff():
    op = OperationFactory.get_operation("abs_diff")
    assert op.execute(5, 10) == 5
    assert op.execute(10, 5) == 5

def test_factory_invalid_operation():
    with pytest.raises(OperationError):
        OperationFactory.get_operation("non_existent_op")