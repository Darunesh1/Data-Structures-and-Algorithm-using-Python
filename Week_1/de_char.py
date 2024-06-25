def del_char(s,c):
    if len(c)>1:
        return s
    return s.replace(c,"")


s = input()
c = input()
print(del_char(s,c))