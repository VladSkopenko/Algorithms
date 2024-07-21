from dataclasses import dataclass
from abc import ABC


@dataclass
class User(ABC):
    """Дата классы отличная идея  что бы хранить данные так как есть встроенные __eq__ __str__ __repr__ __init__
    __new__"""
    name: str
    age: int


class Buyer(User):
    pass


alex = User('Alex', 23)
oleg = User("Oleg", 23)
b_alex = Buyer('Alex', 23)
