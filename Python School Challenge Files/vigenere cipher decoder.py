string, key = "", ""
newstring = ""
chars = list("abcdefghijklmnopqrstuvwxyz")
def to_ascii_num(char):
    counter = 0
    for i in chars:
        if char.lower() == i:
            return counter
        counter+=1

def num_to_ascii(num):
    if num >= 25:
        return chars[num%25]
    return chars[num]

keycount = 0
for i in range(len(string)):
    if string[i] == " ":
        newstring += " "
    else:
        newstring += num_to_ascii(to_ascii_num(string[i]) - to_ascii_num(key[keycount]))
        if keycount >= len(key)-1:
            keycount = 0
        else:
            keycount += 1
print(newstring)
