import csv
import sys

with open(sys.argv[1]+'/input_hw_2.csv', 'r') as csvfile:
    separated_file = csvfile.readlines()
    separated_file = [row.split(';') for row in separated_file]
    departure_date_list = []
    for row in separated_file:
        departure_date_list.append(row[3])
    #print(separated_file)
    print(departure_date_list)
def get_departure_months():
    list_1 = [i.split('-') for i in departure_date_list]
    departure_date_months = []
    for i in list_1:
        departure_date_months.append(i[1])
    return departure_date_months
def get_histogram(date_list):
    my_histogram = {}
    for item in date_list:
        if (item in my_histogram):
            my_histogram[item] += 1
        else:
            my_histogram[item] = 1
    return my_histogram
list_of_months = get_departure_months()
hist_of_months = get_histogram(list_of_months)
print(hist_of_months)
#for key in hist_of_months.keys():
    #print(key, hist_of_months[key])
def bubble_sort(list_1):
    n = len(list_1)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(list_1[j] < list_1[j+1]):
                temp = list_1[j]
                list_1[j] = list_1[j+1]
                list_1[j+1] = temp
    return list_1
def get_mean(list_1):
    s,t = 0,0
    for item in list_1:
        s=s+1
        t=t+item
    my_mean = t/s
    return my_mean
def get_median(list_1):
    sorted_list = bubble_sort(list_1)
    print(sorted_list)
    n = len(sorted_list)
    if (n%2 == 1):
        middle = int(n/2) + 1
        median = sorted_list[middle-1]
    else:
        middle_1 = int(n/2)-1
        middle_2 = middle_1 +1
        median = (sorted_list[middle_1]+sorted_list[middle_2])/2
    return median
list_of_values = list(hist_of_months.values())
print("Value listesi:")
print(list_of_values)
print("Ortalama:")
print(get_mean(list_of_values))
print("Medyan:")
print(get_median(list_of_values))

with open(sys.argv[2]+'/180401020_hw_2_output.txt','w') as dosya:
    dosya.write("aritmetik ortalama : "+" "+str(get_mean(list_of_values)))
    dosya.write("medyan : "+" "+str(get_median(list_of_values)))
