s = "GLOBAL VARIABLE!"


def func():
    global s
    s = 50
    print(s)


func()
print(s)


def my_local():
    mylocal = 10
    print(locals())
    print(globals())

my_local()


def hello(name="Vinay"):
    return "hello "+name


print(hello())


mynewgreet = hello

print(mynewgreet())


# Function within functions
def my_hello(name="vinay"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"
    # print(greet())
    # print(welcome())
    # print("End of my_hello()")
    if name == "vinay":
        return greet
    else:
        return welcome


x = my_hello()

print(x())


def hello2():
    return "HI VINAY!"


def other(func):
    print("HELLO")
    print(func())


other(hello2)


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

