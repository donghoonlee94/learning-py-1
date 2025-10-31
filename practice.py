# Number
print(5)
print(-10)
print(3.14)
print(1000)

# String
print('zz'*100)

# Boolean
print(5> 10)
print(not(5> 10))
print(not False)
print(not True)
print(not 0)

# Variable  
animal = "dog"
name = "fire dog"
age = 2
hobby = "sleep"
is_adult = age >= 3

'''
print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "은 " + str(age) + "살이며, " + ("어른일까요?" if is_adult else "어린이일까요?"))
print(name + "은 " , age , "살이며, ", ("어른일까요?" if is_adult else "어린이일까요?"))

print(f"우리집 {animal}의 이름은 {name}이에요")
print(f"{name}은 {age}살이며, {'어른일까요?' if is_adult else '어린이일까요?'}")
'''

print(f"우리집 {animal}의 이름은 {name} 이에요")
print(f"{name}은 {age}살이며 {('어른' if is_adult else '어린애')}")