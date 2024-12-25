a = 9**8 + 3**5 - 9
c = 0
while a > 0:
    if a % 3 == 2:
        c += 1
    a = a // 3
print(c)
