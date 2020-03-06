#This code creates all possible sums and gives the maximum total value.
def my_f_1(liste):
    n=len(liste)
    maxSum=0
    for i in range(n):
        t=0
        for j in range(i,n):
            t=t+liste[j]
            if(t>maxSum):
                maxSum=t
    return maxSum
list_1=[4,-3,5,-2,-1,2,6,-2]
my_f_1(list_1)                       
