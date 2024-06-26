import math

class Triangle:
    
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
    def Is_valid(self):
        if (self.A + self.B > self.C) and (self.C + self.B > self.A) and (self.A + self.C > self.B):
            return "Valid"
        return "Invalid"
        
    def Side_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
            
        if self.A == self.B == self.C:
            return "Equilateral"
        elif self.A == self.B or self.C == self.A or self.B == self.C:
            return "Isosceles"
        else:
            return "Scalene"
            
    def Angle_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
            
        sides = sorted([self.A, self.B, self.C])
        a, b, c = sides[0], sides[1], sides[2]
        
        if a**2 + b**2 > c**2:
            return "Acute"
        elif a**2 + b**2 == c**2:
            return "Right"
        else:
            return "Obtuse"
            
    def Area(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
            
        s = (self.A + self.B + self.C) / 2
        area = math.sqrt(s * (s - self.A) * (s - self.B) * (s - self.C))
        return area


a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())