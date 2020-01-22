print("Mini Calculator")
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y

print("1. Add", "2. Substract", "3. Division", "4. Multiplication")
choice= (input("Choose operation: "))
num_1= (float(input("First number: ")))
num_2= (float(input("Second number: ")))

if choice=="1":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice== "2":
    print(num_1,"-",num_2,"=",substract(num_1,num_2))
elif choice== "3":
    print(num_1,"/",num_2,"=",division(num_1,num_2))
elif choice== "4":
    print(num_1,"*",num_2,"=",multiplication(num_1,num_2))
else:
    print("Invalid input")

