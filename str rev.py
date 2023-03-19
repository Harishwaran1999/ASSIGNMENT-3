def reverse_rec(str):
    if len(str)==0:
        return str
    else:
        return reverse_rec(str[1:]) +str[0]
print(reverse_rec("1234abcd"))