from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class Calculation:
    operation: str
    operand_a: float
    operand_b: float
    result: float
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return asdict(self)