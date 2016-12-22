from Models.Point import Point
from Models.Profile import Profile

point = Point(1,2)
point2 = Point(1,3)
point3 = Point(1,4)
point4 = Point(1,5)
point5 = Point(1,6)
point6 = Point(1,7)

profile = Profile()

profile.center = Point(6,6)

profile.add_point(point)
profile.add_point(point2)
profile.add_point(point3)
profile.add_point(point4)
profile.add_point(point5)
profile.add_point(point6)

print(profile)