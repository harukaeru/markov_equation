while True:
    try:
        x = input()
    except EOFError:
        print('ok')
        exit()
    a = list(map(int, x.split()))
    assert a[0] * a[0] + a[1] * a[1] + a[2] * a[2] == 3 * a[0] * a[1] * a[2], a
