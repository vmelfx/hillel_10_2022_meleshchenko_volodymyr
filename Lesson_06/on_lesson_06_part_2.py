def logger(char: str):
    def wrapper(func):
        def inner():
            print(char * 10)
            func()
            print(char * 10)

        return inner

    return wrapper


@logger(char="%")
def greeting_john():
    print("Hello John!")


@logger(char="#")
def greeting_marry():
    print("Hello Marry!")


greeting_john()
greeting_marry()
