# Read three sides
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Classify and print
isvalid = False
if a + b > c and a + c > b and b + c > a:
  isvalid = True
  if a == b == c:
    print("Equilateral")
  elif a == b or a == c or b == c:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Not a triangle")