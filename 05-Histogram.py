#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.
#An item has a key and the corresponding value expressed as a pair, key: value.

my_d={1:'bir',2:2,'3':'three'}
for key in my_d.keys():
    print(key,my_d[key])



1 in my_d #this returns True
if -10  not in my_d: 
    my_d[-10]=50
my_d #output is: {1: 'bir', 2: 2, '3': 'three', -10: 50}



def my_h(list_1): #my_histogram
    my_d={}
    for item in list_1:
        if item not in my_d:
            my_d[item]=1
        else:
            my_d[item]=my_d[item]+1
    return my_d
list_1=[1,4,7,84,3,62,23]
my_d=my_h(list_1)
print(my_d)



def lookup(d,v):
    for key in d:
        if d[key]==v:
            return key
    else:
        return -1
my_d
lookup(my_d,15)
