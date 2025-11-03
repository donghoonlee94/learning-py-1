from random import *

users = range(1, 21)
users = list(users) 
print(users, type(users))

shuffle(users)

winners = sample(users, 4)
print(f"치킨 당첨자 : {winners[0]}")
print(f"커피 당첨자 : {winners[1:]}")

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))