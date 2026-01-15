from textwrap import wrap
string = ""
string1 = string[:int(len(string)/2)]
string2 = string[int(len(string)/2):]
newstring = ""
for b in range(len(string1)):
    newstring += string1[b] + string2[b]

print(newstring)
string = wrap(string,3)
equiv = {}
found = []
counter = 0
newstring = ""
for i in string:
    if i not in found:
        found.append(i)
        equiv[i] = counter
        counter += 1
print(equiv)
chars = list("abcdefghijklmnopqrstuvwxyz")
def num_to_ascii(num):
    return chars[num]
asciistring = ""
for i in string:
    asciistring += num_to_ascii(equiv[i])
print(asciistring)

def to_ascii_num(char):
    counter = 0
    for i in chars:
        if char.lower() == i:
            return counter
        counter+=1

string1 = "abcdefghijklmnopqrstuvwxyz"
string2 ="mydearstchlnopiubgvfwkxjzq"
key = " "*26
for v in range(len(string2)):
    print(string1[v])
    key = key[:to_ascii_num(string2[v])] + string1[v] + key[to_ascii_num(string2[v]) + 1:]
print(key)
