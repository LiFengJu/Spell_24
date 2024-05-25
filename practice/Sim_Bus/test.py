a = 10
def test():
    global a
    print(a)

test()
def test2():
    global a
    a = 20
    print(a)

test2()
test()