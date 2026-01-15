##words = string.split(" ")
##newstring = ""
##for i in words:
##    newstring += i[1]
##    newstring += i[2]
##    newstring += i[0]
##    newstring += i[3]
##    newstring += i[5]
##    newstring += i[4]
##    newstring+= " "
##print(newstring)
from textwrap import wrap
string = ""
words = wrap(string.replace(" ",""),5)
newstring = ""
for i in words:
    try:
        newstring += i[2]
        newstring += i[3]
        newstring += i[4]
        newstring += i[0]
        newstring += i[1]
        newstring += i[5]
        newstring+= " "
    except IndexError as error:
        pass
print(newstring.replace(" ",""))
