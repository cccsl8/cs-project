def toBinary(num):
    newNum = num // 2
    remainder = num % 2
    temp = 0
    final = ""
    while newNum > 0:
        if remainder != 0:
            temp = 1
        elif remainder == 0:
            temp = 0
        final = str(temp) + str(final)
        newNum = newNum // 2
        remainder = newNum % 2
    return final
