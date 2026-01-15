#from Luhn_algorithm import check_valid
import random
def gen_num(prefix):
    num = prefix
    amount = 15 - len(num)
    for i in range(amount):
        num = num + str(random.randint(1,9))
    multi = 1
    total = 0
    for i in range(len(num)):
        if multi == 2:
            multi = 1
        else:
            multi = 2
        result = int(num[::-1][i]) * multi
        if result >= 10:
            digits = str(result)
            total += int(digits[0]) + int(digits[1])
        else:
            total += result
    print(num + str((10-(total%10)))[-1])
#print(check_valid(num + str((10-(total%10)))))
a = int(input("number "))
for i in range(a):
    gen_num("")
