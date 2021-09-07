def display(*args): 
    """ Using normal argument only passing value """
    print("Using args")
    for arg in args:
        print(arg)


display("Hello", "World")


def another_display(**kwargs):
    """ passing key value pair argument """
    print("\n\nusing kwargs")
    for key, value in kwargs.items():
        print(key, value)


another_display(name="John", age=13)
