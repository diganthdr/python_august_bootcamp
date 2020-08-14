
my_variable = 20
print("Global block: my variable: ", my_variable, id(my_variable))

def some_function():
    '''
    doc
    '''
    #global my_variable #access global variable.
    my_variable = 30
    print("function block: my variable: ", my_variable, id(my_variable))
    another_f()
    x = 3
    if x == 3:
        my_variable = 40

        #print("if block: my variable: ", my_variable,id(my_variable))
        for i in range(1,5):
            my_variable = i
            print("for block: my variable: ", my_variable, id(my_variable))


def another_f():
    print("another one")
    print("another one 1")
    print("another one 2")

    try:
        fd = open("my_coins.py")
        print(3/0)
        print("STMT in TRY")
    except ZeroDivisionError:
        print("There was an attempt to divide a number by zero")

    except:
        print("Something went wrong")

    print("another one 3")
    print("another one 4")

some_function()