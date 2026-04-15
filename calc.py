val = int(input("Enter number: "))
while True:
    print(val)
    if val == 1: break
    elif val % 2 == 0: val = int(val/2)
    else: val = int(3 * val + 1)
