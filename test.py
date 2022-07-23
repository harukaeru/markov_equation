cache = set()

while True:
    try:
        x = input()
    except EOFError:
        print('ok')
        exit()
    a = list(map(int, x.split()))

    t = tuple(sorted(a))
    if t in cache:
        raise Exception('Already existed', t)
    cache.add(t)
    assert a[0] * a[0] + a[1] * a[1] + a[2] * a[2] == 3 * a[0] * a[1] * a[2], a
