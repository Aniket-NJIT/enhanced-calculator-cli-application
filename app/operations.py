from abc import ABC, abstractmethod
from app.exceptions import OperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass # pragma: no cover

class Add(Operation):
    def execute(self, a, b): return a + b

class Subtract(Operation):
    def execute(self, a, b): return a - b

class Multiply(Operation):
    def execute(self, a, b): return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0: raise OperationError("Cannot divide by zero.")
        return a / b

class Power(Operation):
    def execute(self, a, b): return a ** b

class Root(Operation):
    def execute(self, a, b):
        if b == 0: raise OperationError("Cannot calculate the 0th root.")
        if a < 0 and b % 2 == 0: raise OperationError("Even root of negative number.")
        return a ** (1 / b)

class Modulus(Operation):
    def execute(self, a, b):
        if b == 0: raise OperationError("Modulo by zero.")
        return a % b

class IntDivide(Operation):
    def execute(self, a, b):
        if b == 0: raise OperationError("Integer division by zero.")
        return a // b

class Percent(Operation):
    def execute(self, a, b):
        if b == 0: raise OperationError("Base for percentage cannot be zero.")
        return (a / b) * 100

class AbsDiff(Operation):
    def execute(self, a, b): return abs(a - b)

class OperationFactory:
    _operations = {
        "add": Add(), "subtract": Subtract(), "multiply": Multiply(),
        "divide": Divide(), "power": Power(), "root": Root(),
        "modulus": Modulus(), "int_divide": IntDivide(),
        "percent": Percent(), "abs_diff": AbsDiff()
    }

    @staticmethod
    def get_operation(name: str) -> Operation:
        op = OperationFactory._operations.get(name.lower())
        if not op:
            raise OperationError(f"Unknown operation: {name}")
        return op