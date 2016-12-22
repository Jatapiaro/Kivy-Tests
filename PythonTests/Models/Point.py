class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "["+str(self.x)+","+str(self.y)+"]\n"

    def __lt__ (self, other):
        return other.x>self.x

    def __gt__ (self, other):
        return self.x>self.x

    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y

    def __ne__ (self, other):
        return not self.__eq__(other)