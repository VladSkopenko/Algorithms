from dataclasses import dataclass


@dataclass
class User:
    """Дата классы отличная идея  что бы хранить данные так как есть встроенные __eq__ __str__ __repr__ __init__ __new__"""
    name: str
    age: int


alex = User('Alex', 23)
oleg = User("Oleg", 23)
print(alex.age == oleg.age)

