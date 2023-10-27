##inheritance OOP
##Home work. Creating triangle class and inheriting by circle class, square class, rectangle class
##each class has method to solve periphery and area
##Making Point class
import math
class Point:
    ##constructor
    def __init__(self,X,Y):
        self.x=X
        self.y=Y
    ##Static solve distant method from two points
    @staticmethod
    def distance(point1,point2):
        return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)
class Triangle:
    ##constructor
    def __init__(self,X1,Y1,X2,Y2,X3,Y3):
        self.pointA = Point(X1,Y1)
        self.pointB = Point(X2,Y2)
        self.pointC = Point(X3,Y3)
        AB= Point.distance(self.pointA,self.pointB)
        AC= Point.distance(self.pointA,self.pointC)
        BC= Point.distance(self.pointB,self.pointC)
        if(AB+AC>BC and AB+BC>AC and AC+BC>AB):
            print("Da tao thanh cong tam giac")
        else:
            print("Khong phai tam giac")
    ##static method periphery
    @staticmethod
    def solvePeriphery(pointA,pointB,pointC):
        AB= Point.distance(pointA,pointB)
        AC= Point.distance(pointA,pointC)
        BC= Point.distance(pointB,pointC)
        return AB+AC+BC
    @staticmethod
    def solveArea(pointA,pointB,pointC):
        AB= Point.distance(pointA,pointB)
        AC= Point.distance(pointA,pointC)
        BC= Point.distance(pointB,pointC)
        halfPeriphery= Triangle.solvePeriphery(pointA,pointB,pointC)/2
        return math.sqrt(halfPeriphery*(halfPeriphery-AB)*(halfPeriphery-AC)*(halfPeriphery-BC))
##class square inherit from triangle
class Square(Triangle):
    ##constructor
    def __init__(self,x1,y1,x2,y2):
        Triangle.__init__(self,x1,y1,x2,y2,0,0) 
    ##overide solvePeriphery method
    @staticmethod
    def solvePeriphery(pointA,pointB):
        return Point.distance(pointA,pointB)*4
    @staticmethod
    def solveArea(pointA, pointB):
        return Point.distance(pointA,pointB)**2
    



##test thu 
tamGiac= Triangle(0,1,1,0,0,0)
print("Tam Giac")
print("Chu Vi: ",tamGiac.solvePeriphery(tamGiac.pointA,tamGiac.pointB,tamGiac.pointC))
print("Dien Tich:",tamGiac.solveArea(tamGiac.pointA,tamGiac.pointB,tamGiac.pointC)) 
hinhVuong=Square(0,1,0,0)
print("Chu Vi:",Square.solvePeriphery(hinhVuong.pointA,hinhVuong.pointB))
print("Dien Tich:",Square.solveArea(hinhVuong.pointA,hinhVuong.pointB))