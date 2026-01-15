from math import sqrt
def isRightTriangle(a,b,c):
    c = sqrt((a**2)+(b**2))
    if c.is_integer():
        return True
def can_form_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
counter = 0
smallest = 9999999
a = 2024
for b in range(2024143):
    c = sqrt((2024**2)+(b**2))
    if c.is_integer() and b > 0 and isRightTriangle(a, b, c) and can_form_triangle(a, b,c):
        if b <= smallest:
            smallest = b
        counter += 1
        print(b,c)
print(22, counter)
