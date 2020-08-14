
def simple_add(a,b):
    ''' '''
    sum = 0
    buffer = 0
    try:
        sum = a + b + buffer
    except TypeError:
        print("Enter only numbers")

    return sum