import math


def distance(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


x1,x2 = input("Enter your first point like : x1 x2 ").split()
y1,y2 = input("Enter your second point like : y1 y2 ").split()

result = distance(int(x1),int( x2),int(y1), int(y2))
print(format(result,".2f"))