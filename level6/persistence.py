def persistence(n):
    # your code
    if n < 10:
        return 0

    counter = 0

    while n >= 10:
        res = 1
        for i in str(n):
            res *= int(i)

        n = res
        counter += 1

    return counter
