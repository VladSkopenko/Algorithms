from queue import Queue

q = Queue(maxsize=3)

q.put("a")
q.put("b")
print(q.full())
q.put("c")
print(q.full())
print(q.queue)
q.get()
print(q.queue)
print(q.empty())

"""
Очередь (queue) в Python - это структура данных, которая работает по принципу "первым пришел - первым вышел" 
(FIFO, First-In-First-Out). Это означает, что элементы добавляются в конец очереди и извлекаются из начала.
"""
