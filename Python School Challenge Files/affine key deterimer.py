string = "MRS ADA"
to = "RYP VUV"
chars = list("abcdefghijklmnopqrstuvwxyz")
def to_ascii_num(char):
    counter = 0
    for i in chars:
        if char.lower() == i:
            return counter
        counter+=1
def num_to_ascii(num):
    return chars[num]
        
for a in range(1,27,2):
    for b in range(26):
        newstring = ""
        for v in range(len(string)):
            if string[v].lower() in chars:
                ascii_val = to_ascii_num(string[v])
                y = ((a*ascii_val)+b) % 26
                newstring += num_to_ascii(y)
            else:
                newstring += string[v]
        if newstring == to.lower():
            print(a,b)
