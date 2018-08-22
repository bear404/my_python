def re_str(string):
    if len(string)==1:
        return string
    else:
        return string[-1]+re_str(string[:-1])

print(re_str("abc123"))
