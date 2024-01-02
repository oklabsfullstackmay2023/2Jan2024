# 1. Function Definition is one time process
def myFunction():
    thisdict = {
        "name": 'Vishal',
        "age": 14,
        "city": "Neemuch"
    }
    print(thisdict)

    thisdict = {
        'name': 'Alex',
        'age': 25,
        "country": 'Paris'
    }
    return thisdict 

thistdict = {
    "name": "Pat Cummins",
    "age": 25,
    "country": "Australia"
}
print(thistdict)

# 2. Function calling/invoking is many time process
result = myFunction() 
print(result)  
