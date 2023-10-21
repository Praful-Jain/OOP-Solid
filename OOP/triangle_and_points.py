import math
class Triangle:
    
    def __init__(self):
        self.points = []    # list of tuples
        
    def add_point(self,x,y):
        self.points.append((x,y))
        
    def calculate_distance(self,pt1,pt2):
        # Pythagorean theorem
        return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
        
    def perimeter(self):
        peri = 0
        if len(self.points) == 3:
            peri += self.calculate_distance(self.points[0],self.points[1])
            peri += self.calculate_distance(self.points[1],self.points[2])
            peri += self.calculate_distance(self.points[0],self.points[2])
        print('Perimeter of triangle = ',peri)
        
    def is_equal(self,obj):
        return self.points == obj.points
    
    def __eq__(self, obj) -> bool:
        return self.points == obj.points
        
t1 = Triangle()
t1.add_point(0,0)
t1.add_point(0,3)
t1.add_point(4,0)
t1.perimeter()  # task1

t2 = Triangle()
t2.add_point(1,2)
t2.add_point(2,1)
t2.add_point(1,5)
t2.perimeter()  # task2

# task3
if t1.is_equal(t2) :
    print("t1 and t2 are equal")
else:
    print("t1 and t2 are not equal")

t3 = Triangle()
t3.add_point(1,2)
t3.add_point(2,1)
t3.add_point(1,5)

# task4
if t1 == t3 :
    print("t1 and t3 are equal")
else:
    print("t1 and t3 are not equal")
    
# task5
if t1.is_equal(t3) :
    print("t1 and t3 are equal")
else:
    print("t1 and t3 are not equal")

# task6
if t3.is_equal(t1) :
    print("t3 and t1 are equal")
else:
    print("t3 and t1 are not equal")

# task7
if t1.__eq__(t3) :
    print("t1 and t3 are equal")
else:
    print("t1 and t3 are not equal")