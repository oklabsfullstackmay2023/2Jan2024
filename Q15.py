def myFunction():
    thislist = ['apple', 'grapes']
    thislist.insert(1, "orange")
    print(thislist)

    thislist = ['mango', "papaya"]
    thislist.insert(1, "apple")
    print(thislist)

    thislist = ['apple', "papaya", 'grapes']
    thislist[1] = 'mango'
    print(thislist)
    
    return [
        ['apple', 'orange', 'grapes'],
        ['apple', 'apple', 'orange', 'grapes'],
        ['apple', 'mango', 'grapes']
    ]

#2. function calling/invoking is many time process
result = myFunction()
print(result)
