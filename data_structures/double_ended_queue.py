from collections import deque

d = deque()

d.append(4)  # додати в кінець
d.appendleft(-2)  # додати в початок

print(d)
d.pop()  # видалити з кінця
print(d)
d.popleft()  # видалити з початку
print(d)

d.extend([1, 2, 3])  # додати список
d.extendleft([-5, -6, -7, 3])  # додати список зліва
print(d)
d.rotate(2)  # Останні 2 стають на перші 2
print(d)
d.rotate(-2)  # перші 2 стають на останні 2
print(d)
print(d.count(3))
