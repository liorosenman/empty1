from enum import Enum
import json
class Car:
    def __init__(self, color, model, kind):
        self.color = color
        self.model = model
        self.kind = kind

    def __str__(self):
        return f"Car(color={self.color}, model={self.model}, kind={self.kind})"

    def to_dict(self):
        return {
            "color": self.color,
            "model": self.model,
            "kind": self.kind
        }

class Menu(Enum):
    PRINT = 1
    ADD = 2
    UPDATE = 3
    DELETE = 4
    AMOUNT = 5
    CLEAR = 6
    