class Point:
    def __init__(self,x,y):
        self.x_cord=x
        self.y_cord=y

    def __str__(self):
        return '<{},{}>'.format(self.x_cord,self.y_cord)


    def euclidean_distance(self,other):
        return ((self.x_cord-other.x_cord)**2 + (self.y_cord-other.y_cord)**2)**0.5       


    def distance_from_origin(self):
        return (self.x_cord**2 + self.y_cord**2)*0.5
        # return self.euclidean_distance(Point(0,0))

    
    
        


class Line:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return "{}x + {}y + c = 0".format(self.a,self.b,self.c)


    def point_on_line(line,point):
            if line.a*point.x_cord + line.b*point.y_cord +line.c==0:
                return("lies on the line")
            else:
                return("does not lies on the line")

    def shortese_path(line,point):
        return abs(line.a*point.x_cord + line.b*point.y_cord + line.c )/(line.a**2 + line.b**2)**0.5



p1=Point(1,2)
p2=Point(3,4)
print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())

l1=Line(2,3,5)
print(l1.point_on_line(p1))
print(l1.shortese_path(p1))