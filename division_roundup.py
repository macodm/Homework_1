print ("Division Round-Up Calculator")
def division(a,b):
    return a/b

import math

num_1 = float(input("Enter numerator: "))
num_2 = float(input("Enter denominator: "))

resul= math.ceil(division(num_1,num_2))
print(num_1, "/", num_2, "=", resul )

