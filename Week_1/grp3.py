def shuffle(a, b):
    if len(a) <= 1 and len(b) <= 1:
        return a + b  # Combine the remaining elements if both lists have at most one element left
    if len(a) <= 1:
        return a + [b[0]] + shuffle([], b[1:])  # If a is exhausted, concatenate the rest of b
    if len(b) <= 1:
        return [a[0]] + b + shuffle(a[1:], [])  # If b is exhausted, concatenate the rest of a

    return [a[0], b[0]] + shuffle(a[1:], b[1:])  # Regular case

L1 = eval(input("Enter first list: "))
L2 = eval(input("Enter second list: "))
print(shuffle(L1, L2))
