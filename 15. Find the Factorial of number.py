num = int(input("enter a number here : "))

fact = 1

if num < 0:
    print("factorial of 0 does nopt exist")
if num == 0:
    print("factorial of 0 is", 1)
if num > 0:
    for i in range (1,num+1):
        fact = fact * i
print ("the factorial of the given number is", fact)

#______________Using Recursion_______________


def fact (a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))
    
num = int(input("enter a number here : "))

result = fact(num)

print("The factorial of the given number is", result)
    