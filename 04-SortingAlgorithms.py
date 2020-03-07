#Insertion Sort
def insertionSort(arr): 
    n=len(arr)
    for i in range(1,n): 
        key=arr[i]
        j=i-1
        while (j>=0 and key<arr[j]): 
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    for i in range(n): 
        print (arr[i]) 
arr1=[5,25,6,1,98,80,3,4,189,33]
insertionSort(arr1)


#Shell Sort:
def shellSort(arr):
    n=len(arr)
    gap=n//2 
    while gap>0:
        for i in range (gap,n):
            temp=arr[i]
            j=i
            while j>gap and arr[j-gap]>temp: 
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap//=2 
    for i in range(n):
        print (arr[i])
arr1=[5,25,6,1,98,80,3,4,189,33]
shellSort(arr1)


#Bubble Sort:
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
for i in range(len(arr)):
    print (arr[i])


#Selection Sort:
def selectionSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if A[min_index] > A[j]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
A = [64, 25, 12, 22, 11]
selectionSort(A)
for i in range(len(A)):
    print(A[i])






