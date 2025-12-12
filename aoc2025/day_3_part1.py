def bank(a):
    # a = "811111111111119"
    num1 = 0
    num2 = 0
    for i, c in enumerate(a[:-1]):
        if int(c) > num1:
            # print(b)
            num1 = int(c)
    second_bank = a.find(str(num1))
    a = a[second_bank + 1 :]
    # a = a.replace(str(num1),"")
    # print(a)
    for b in a:
        if int(b) > num2:
            # print(b)
            num2 = int(b)
    new_num = int(f"{num1}{num2}")
    return new_num


batteries = []
while True:
    try:
        line = input()
    except EOFError:
        break
    batteries.append(line)
total = 0
for b in batteries:
    total += bank(b)
print(total)
# for b in a[:-1]:
#     if b > num1:
#         num1 = b
#     if
