def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    square = list(map(lambda x: x**2, array1))

    return sorted(square) == sorted(array2)
