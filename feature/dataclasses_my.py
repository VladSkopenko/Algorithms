from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=False)
class User(ABC):
    """Дата классы отличная идея  что бы хранить данные так как есть встроенные __eq__ __str__ __repr__ __init__
    __new__"""
    name: str
    age: int

    def get_info(self):
        ...


# @dataclass # Стоит добавить опять если надо пересоздать методы , если становится больше полей, иначе можно не добавлять
class Buyer(User):
    def get_info(self):
        print("Buyer", self.name, self.age)


alex = User('Alex', 23)
oleg = User("Oleg", 23)
b_alex = Buyer('Alex', 23)
alex.name = "ased"
print(alex == oleg)
print(alex == b_alex)
print(b_alex.get_info())
