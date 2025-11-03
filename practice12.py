menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")
# print(menu)

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)


(name, age, hobby) = "김종국", 20, "코딩"
print(name, age, hobby)

locations = {
    (0, 0): "시작점",
    (10, 20): "목적지"
}
print(locations)
print(locations[(0, 0)])