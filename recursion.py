def sum(x, y):
     if y == 0:
        return x;

    return 1 + sum(x, y-1)


def Fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 

print(Fibonacci(9))


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq.pop()

    lower_items = list()
    higher_items = list()

    for item in seq:
        if item < pivot:
            lower_items.append(item)
        else:
            higher_items.append(item)
    return quick_sort(lower_items) + [pivot] + quick_sort(higher_items)

seq = [4,5,1,2,33,6,4,1]
print(quick_sort(seq))
