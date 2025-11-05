# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# import travel.vietnam
# trip_to = travel.vietnam.VietnamPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel.vietnam import VietnamPackage
# trip_to = VietnamPackage()
# trip_to.detail()

print(f"practice36.py의 __name__ = {__name__}")
print("=" * 50)

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))
print(inspect.getfile(vietnam))