
my_variable = 20
print("Global block: my variable: ", my_variable, id(my_variable))

def some_function():
    #global my_variable #access global variable.
    my_variable = 30
    print("function block: my variable: ", my_variable, id(my_variable))

    x = 3
    if x == 3:
        my_variable = 40

        #print("if block: my variable: ", my_variable,id(my_variable))
        for i in range(1,5):
            my_variable = i
            print("for block: my variable: ", my_variable, id(my_variable))

some_function()