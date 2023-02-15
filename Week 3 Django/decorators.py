def announce(f):
    def wrapper():
        print("Before runing fun")
        f()
        print("After running function")
    return wrapper


@announce
def hello():
    print("Hello world")


hello()

print(hello)


def b_test():
    return print("Just Testing")


print(b_test)




