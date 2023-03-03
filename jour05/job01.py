def nombre(n):
    if n == 0: # 0! = 1
        return 1
    else:
        return int(n * nombre(n - 1))

print(nombre(4))