class Unit:
    def __init__(self):
        print("Unit 생성자")    
        super().__init__()

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        super().__init__()
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        print("FlyableUnit 생성자")
        super().__init__()

drop_ship = FlyableUnit()