def get_name():
    print(f"{__name__=} inside function")


MY_VAR = 3


if __name__ == '__main__':
    get_name()

    assert get_name() == None

