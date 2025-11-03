# # 마린
# # 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40
# speed = 1

# print("{0} 유닛이 생성되었습니다.".format(name))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage=10)

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 35, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)

