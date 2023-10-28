x = 3


def test_func():
    # global x
    x = x + 1
    print(x)


def test_func2():
    print(f"test_func2:: {x}")


test_func()
test_func2()
