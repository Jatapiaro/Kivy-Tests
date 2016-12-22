from Models.Point import Point
class Profile(object):

    def __init__(self,center=None,points=None):

        if center is None:
            self.center = Point(0,0)
        else:
            self.center = center

        if points is None:
            self.points = []
        else:
            self.points = points


    def add_point(self,point):
        self.points.append(point)

    def __repr__(self):
        return "Center of profile: "+str(self.center)+" with points -->"+str(self.points)





