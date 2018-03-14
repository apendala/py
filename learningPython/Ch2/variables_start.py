# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

 # re-declaring the variable works
f='abc'
print(f)

# # ERROR: variables of different types cannot be combined

# Python is a strong typed language even though you don't have to declare types when initializing
# Cannot mix types - so you must type cast things to be same type
print("this is a string3: " + str(123))


# Global vs. local variables in functions
def someFunction():
    # Note: 'f' is local to function.
    #f='def'
    #print("someFunction: Local function string: " + f)
    # If you want to make 'f' global, you need to explicitly say it is
    global f
    f='def'
    print("someFunction: Global function string: " + f)



someFunction()
print("Global function string: " + f)

# delete definition of a variable previously defined
del f
# print(f)