import hashlib


names = {"Nata": 16,
         "Alex": 17,
         "Vova": 18
         }

print(hash("Nata"))
print(hash("Alex"))
print(hash("Vova"))

hashed_nata = hashlib.sha256("Nata".encode())
print(hashed_nata)
print(hashed_nata.digest())
print(hashed_nata.hexdigest())

