import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})' # !r chama __repr__ da variavel e não o __str__
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

if __name__=='__main__':
    v1 = Vector(2,4)
    v2 = Vector(2,1)

    # Addition
    v3 = v1 + v2
    print('v3: ',v3)

    # Absolute value
    print('abs: ',abs(Vector(3,4)))

    # Scalar multiplication:
    v4 = v1*3
    print('v4: ',v4)