fibonacci_list = [0, 1]

def fibonacci(n, list):
    lenght = len(list)
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    elif n == lenght:
        print(list[-1])
        
    else:
        list.append(int(list[-1] + list[-2]))
        fibonacci(n, list)

fibonacci(7, fibonacci_list)