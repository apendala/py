#
# Example file for working with functions
#

### define a basic function
def func1():
    print("I am a function")
    return 0


# executes a function.  statement in function will be printed
func1()

# execute a function but also prints out the return value of the function
print (func1())

# print the function definition value (which is 0x1024606....) but not execute it
print (func1)




### function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2 )

# executes a function.  statement in function will be printed
func2(11, 22)

# execute a function but also prints out the return value of the function
print(func2(12,24))





### function that returns a value
def cube (arg1):
    return arg1*arg1*arg1

# execute a function but also prints out the return value of the function
print(cube(2)) # output = 8




### function with default value for an argument
def power(num, x=1):
    result=1

    # syntax for range([start], stop[, step])
    for i in range(x):
        result=result * num
    return result

# call function without a value of x, which will use the default
print(power(2)) # output = 2

# call a function with a value of x set to 3
print(power(2,4))  # output = 16

# call a function and specify different order of arguments
print(power(x=5, num=2)) # output = 32




### function with variable number of arguments

def multi_add(*args):  # *args means a variable number of args will be passed
    result=0
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,4))
