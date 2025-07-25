import os

if not os.path.exists("test"):
    os.makedirs("test")

print(os.path.exists("test/test.txt"))
