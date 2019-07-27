from name_and_main import one

print("TOP LEVEL two.py")

one.func()

if __name__ == '__main__':
    print("Two.py is being run directly")
else:
    print("two is being imported another")

