import itertools
combinations = list(itertools.product(range(1,7), repeat=5))
def can_form_triangle(arr):
    for a, b, c in itertools.combinations(arr, 3):
        if a + b > c and a + c > b and b + c > a:
            return True
    return False
counter = 0
for i in combinations:
    if not can_form_triangle(i):
        print(i)
        counter+=1
print(counter)
