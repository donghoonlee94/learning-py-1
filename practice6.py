python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True
print(len(python)) # 17
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n") # 5
print(index) # 5
index = python.index("n", index + 1) # 15
print(index) # 15
print(python.find("Java")) # -1
# print(python.index("Java")) # ValueError: substring not found
print("h1")

print(python.count("n")) # 2