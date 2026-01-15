#num = "5401274300046450"
def check_valid(num):
    ver = num[0:-1]
    multi = 1
    total = 0
    for i in range(len(ver)):
        if multi == 2:
            multi = 1
        else:
            multi = 2
        result = int(ver[::-1][i]) * multi
        if result >= 10:
            digits = str(result)
            total += int(digits[0]) + int(digits[1])
        else:
            total += result
    validation_num = (10-(total%10))
    valid = int(str((10-(total%10)))[-1]) == int(num[-1])
    return valid

#print(check_valid(""))
