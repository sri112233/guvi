x = float(input())
y = float(input())
z = float(input())
 
if (x > y) and (x > z):
   largest = x
elif (y > x) and (y > z):
   largest = y
else:
   largest = z
 
print("The largest number is",largest)
