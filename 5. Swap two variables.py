#Using 3rd variable

x = 13
y = 12

temp = x
print ("the value of temp variable is", temp)
x = y
print ("the value of x is", x)

y = temp
print ("the value of y is",y)

#Without using 3rd variable

x = 12
y = 13
x, y = y, x
print ("the value of x is", x)
print ("the value of y is", y)