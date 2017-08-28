import math

class Vector:


    def __init__(self, x_value, y_value):
        self.x, self.y = x_value, y_value

    def normalize(self):
        magnitude = math.sqrt((self.x ** 2) + (self.y ** 2))
        self.x = ((self.x**2)/magnitude)
        self.y = ((self.y**2)/magnitude)

    def multiply(self, value):
        self.x = self.x * value
        self.y = self.y * value

    def dot(self, otherVector):
        self.x =+ otherVector.x
        self.y =+ otherVector.y

<<<<<<< HEAD
    #def rotate(self, angle):
      # oldX = self.x
       #oldY = self.y
       # self.x = (oldX*math.cos(angle))-(oldY*math.sin(angle))
       # self.y = (oldX*math.sin(angle))+(oldY*(math.cos(angle)))
<<<<<<< HEAD
=======

>>>>>>> Partical-implementation
=======
    #def rotate(self, angle):
     #   oldX = self.x
      #  oldY = self.y
       # self.x = (oldX*math.cos(angle))-(oldY*math.sin(angle))
        #self.y = (oldX*math.sin(angle))+(oldY*(math.cos(angle)))
>>>>>>> 5721d767854510da4fa1c2330d2dfc9174f67f3e


