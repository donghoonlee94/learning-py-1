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
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 35, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

wraith2.attack("1시")

wraith2.damaged(25)
wraith2.damaged(55)

firebat1 = Unit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
