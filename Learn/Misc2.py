
def TestLambda():
    sqr = lambda i:i*i
    map_outputs = list(map(sqr, [1, 2, 3, 4]))    
    print(map_outputs)


def multiply2(x):
  return (x * 2)


def TestMap():
    # my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    # new_list = list(map(lambda x: x * 2 , my_list))
    # Output: [2, 10, 8, 12, 16, 22, 6, 24]
    # print(new_list)
    map_outputs = list(map(lambda x: x*x, [1, 2, 3, 4]))
    print(map_outputs)
    

# Program to double each item in a list using map()

# Program to show the use of lambda functions
# double = lambda x: x * 2
# Output: 10
# print(double(5))

#TestMap()
TestLambda()


