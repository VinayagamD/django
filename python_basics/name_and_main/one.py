def func():
    print("func() in one.py")


print("TOP LEVEL ONE")


if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")
