def make_readable_2(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds // 3600, seconds // 60 % 60, seconds % 60)


def make_readable_1(seconds):
    x = '{:02}'.format(seconds // 3600)
    print("hours: ", x)

def make_readable_2(seconds):
    x = '{:02}'.format(seconds // 60 % 60)
    print("mins:", x)

def make_readable_3(seconds):
    x = '{:02}'.format(seconds % 60)
    print("secs:", x)


make_readable_1(359999)
make_readable_2(359999)
make_readable_3(359999)

make_readable_1(86399)
make_readable_2(86399)
make_readable_3(86399)

make_readable_1(5)
make_readable_2(5)
make_readable_3(5)
