def recursion_test(x):
    if x == 1:
        return x
    return x * recursion_test(x-1)
print(recursion_test(5))
