
my_list = [3,4,5]
my_tuple = (3,4,5)
print("mylist: glob", my_list)

def my_fn(tmp_list):
    tmp_list[0] = 6


my_fn(my_list)
my_fn(my_tuple) #will throw error, becuase tuple is immutable
print(my_list)