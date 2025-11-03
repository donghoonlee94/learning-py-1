cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)

cabinet["C-20"] = "조세호"
print(cabinet)

print("C-20" in cabinet)

cabinet[3] = "김태호1"

# del cabinet["C-20"]
# print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

