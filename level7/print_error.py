def printer_error(s):
    control = []
    err = 0
    size = len(s)
    for word in range(ord('a'), ord('n')):
        control.append(chr(word))
    for i in s:
        if i not in control:
            err += 1
    return str(err) + "/" + str(size)

#Other solutions:

#Option 1:

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

#Option 2:

def printer_error_2(s):
    control = list(map(chr, range(ord('a'), ord('n'))))
    err = sum(1 for i in s if i not in control)
    return f"{err}/{len(s)}"