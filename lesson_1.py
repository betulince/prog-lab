"""
subject:
1.generate list with n items

"""
import random
print(random.random())
s=random.randint(1,100) #random bir integer sayı üretir.
print(s)

def get_n_random_numbers(n,minimum,maximum):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(minimum,maximum))
    return numbers
my_list=get_n_random_numbers(15,-4,4)
print(sorted(my_list))
"""
histogram with two methods

"""
#for a list [0,-4,8,-1,0,-3,6,3,0,1]
#get the histogram with array of tuples format
histogram_1=[(-4,1),(-3,1),(-1,1),(0,2),(1,1),(3,1),(6,1),(8,1)]
print(type(histogram_1)) #liste şeklinde

def my_frequency_with_dict(list):
    frequency_dict={} #dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict

print(my_frequency_with_dict(my_list))

def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]+=1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])

    return frequency_list

my_list_1=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
print("my list:")
print(my_list_1)
result_1=my_frequency_with_dict(my_list_1)
result_2=my_frequency_with_list_of_tuples(my_list_1)
print("frequency with dictionary:")
print(result_1)
print("frequency with list of tuples:")
print(result_2)