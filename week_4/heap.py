def min_heapify(array,i):
    left = 2*i+1
    right = 2*i+2
    length = len(array)-1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i] , array[smallest] = array[smallest] , array[i]
        min_heapify(array,smallest)
#when exchange happens this method applies min_heapify to the node exchanged

def build_min_heap(array):
    for i in reversed(range(len(array)//2)): #reversed : tersten başla
        min_heapify(array,i)

#heap sort;bubble sort,insertion sort ve selection sort'tan daha etkin bir algoritmadır.
def heap_sort(array):
    array = array.copy() #copy() fonksiyonunu kullanarak yeni bir dizi ürettiğimde ve üzerinde değişiklikler yaptığımda orijinal dizi üzerinde bir değişiklik gerçekleşmez.
    build_min_heap(array)
    sorted_array = [] #aldığım sayıları atacağım diziyi oluşturdum.dizi boşsa append() kullanılamaz.
    for _ in range(len(array)): #kullanmadığı değişkene _ ismini veriyor.(for içinde i kullanımı olmadığı için)
        array[0] , array[-1] = array[-1] , array[0] #dizinin başı ile sonunu yer değiştirdi.array[-1] sondaki elemandır.
        sorted_array.append(array.pop()) #array.pop() sayesinde append ile sondaki elemanı aldı ve listeye ekledi.
        min_heapify(array,0)
    return sorted_array

"""
Place the new element in the next available
position in the array.
-Compare the new element with its parent. If the new element is smaller, than swap it with its parent.
-Continue this process until either
     - the new element’s parent is smaller than or equal to the new element, or
     - the new element reaches the root (index 0 of the array) 
"""
def insertItemToHeap(my_heap,item): # my_heap keyfi belirlediğim bir array'in heapify fonksiyonuna gönderilerek heap haline getirilmiş halinin listesidir.
    my_heap.append(item)
    index_of_item = len(my_heap)-1
    if index_of_item<=0:
        return
    parent_index = (index_of_item - 1)//2
    while True:
        if parent_index >= 0 and my_heap[parent_index] > my_heap[index_of_item]:
            my_heap[parent_index], my_heap[index_of_item] = my_heap[index_of_item], my_heap[parent_index]
            index_of_item = parent_index
            parent_index = (index_of_item - 1) // 2
        else:
            break

"""
Place the root element in a variable to return later.
- Remove the last element in the deepest level and move it to the root.
- While the moved element has a value greater than at least one of its children, swap this value with the smaller-valued
child.
- Return the original root that was saved. 
"""
def removeItemFrom(my_heap): # heap'ten ilk elemanı siler.
    root_element = my_heap[0]
    if len(my_heap)==0:
        return
    if len(my_heap)>1:
        my_heap[0], my_heap[-1] = my_heap[-1], my_heap[0]
    my_heap.pop()
    build_min_heap(my_heap)
    return root_element

my_array_1 = [8,10,3,4,7,14,1,2,16]
print("array:",my_array_1)

build_min_heap(my_array_1)
print("heap yapısına uygun olan array:",my_array_1)

print("sorted array:",heap_sort(my_array_1))

insertItemToHeap(my_array_1,5)
insertItemToHeap(my_array_1,56)
insertItemToHeap(my_array_1,-2)
insertItemToHeap(my_array_1,0)
insertItemToHeap(my_array_1,2)
insertItemToHeap(my_array_1,13)
insertItemToHeap(my_array_1,6)
insertItemToHeap(my_array_1,9)
print("yeni elemanların eklendiği heap yapısı:",my_array_1)

removeItemFrom(my_array_1) # minheap'ten ilk elemanı siler.
print("ilk elemanın silindiği yeni heap yapısı:",my_array_1)
