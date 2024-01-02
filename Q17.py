#1. Function Defination is one time process
def myFunction(*args):
    for arg in args:
        print(arg)
    
#2. Funtion callingl/invoking is many time process
result=myFunction(10, "Hello", [1, 2, 3], {"a": 1, "b": 2}, True)
print(result)