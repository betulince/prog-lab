"""
generate list with n items

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


"""
mode of a list  with histogram

"""
print("mode of a list with histogram:")

my_list_2=get_n_random_numbers(10,-5,5)
my_hist_d=my_frequency_with_dict(my_list_2)
print(my_hist_d)
my_hist_l=my_frequency_with_list_of_tuples(my_list_2)
print(my_hist_l)

def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        #print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max

print(my_mode_with_dict(my_hist_d))

my_list_100=get_n_random_numbers(100,-40,40)
my_hist_1=my_frequency_with_dict(my_list_100)
print(my_mode_with_dict(my_hist_1))

print("mode of a list with histogram(a list of tuples)")

my_list_3=get_n_random_numbers(10,-5,5)
my_hist_list=my_frequency_with_list_of_tuples(my_list_3)
print(my_hist_list)

def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max
print(my_mode_with_list(my_hist_list))

"""
linear search on list

"""
print("linear search on a list")

def my_linear_search(my_list,item_search):
    found=(-1,-1) #default,eğer listede yoksa
    for indis in my_list:
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)
            #break,uncomment for last found
    return found
my_list_4=get_n_random_numbers(10,-5,5)
print(my_list_4)
print(my_linear_search(my_list_4,2))

#mean of list
print("mean of list")

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_=t/s
    return mean_

my_list_5 = get_n_random_numbers(10, -50, 50)
print(my_list_5)
print(my_mean(my_list_5))

print("sort the list")

def my_bubble_sort(my_list):
    n=len(my_list)
    print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                #print("swap işlemi")
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list
my_list_6=get_n_random_numbers(4,-5,5)
print(my_list)
print(my_bubble_sort(my_list_6))

print("binary search on a sorted list")

def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)

    while low<=high:
        mid=(low+high) // 2
        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid]>item_search:
            high = mid-1
        else:
            low = mid+1
    return found #none

my_list_7=get_n_random_numbers(10,-5,5)
print("liste ",my_list_7)
my_list_8=my_bubble_sort(my_list_7)
print("sıralı liste ",my_list_8)
print(my_binary_search(my_list_8,3))

print("median of a list")

size = input("dizi boyutunu giriniz:")
size = int(size)  # convert to str to int

my_list_5 = get_n_random_numbers(size, -100, 100)


# print("liste:",my_list_5)

def my_median(my_list_5):
    my_list_6 = my_bubble_sort(my_list_5)
    print(my_list_6)
    n = len(my_list_6)
    if (n % 2 == 1):
        middle = int(n / 2) + 1
        median = my_list_6[middle - 1]
    else:
        middle_1 = int(n / 2) - 1
        middle_2 = middle_1 + 1
        median = (my_list_5[middle_1] + my_list_5[middle_2]) / 2
    return median
print("medyan degeri:", my_median(my_list_5))

