print("circle area and perimeter calculator")
def area(pi,radius):
    return pi*radius*radius

def perim(pi, radius):
    return pi*2*radius

pi= 3.141592
radius= float(input("Enter radius: "))

print("area","=",area(pi,radius))
print("perimeter","=",perim(pi,radius))







