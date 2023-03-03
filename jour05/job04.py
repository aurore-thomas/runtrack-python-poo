list = [3, 87, 9, 76, 6, 4, 1]

def number(list):
    if len(list) == 1:
        return list
    elif list[-1] > list[-2]:
        list.pop(-2)
    else:
        list.pop(-1)
    return number(list)

print(number(list))