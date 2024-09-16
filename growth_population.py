def nb_year(p0, percent, aug, p):
    i = 0
    x = 0

    if x < p:
        print(x)
        x = p0 + p0 * percent / 100 + aug
        i += 1
    
    print(i)
    return i

nb_year(1500, 5, 100, 5000) # 15