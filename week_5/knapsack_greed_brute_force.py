class Item (object):
    def __init__(self , n , v , w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName (self):
        return self.name
    def getValue (self):
        return self.value
    def getWeight (self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result

def value (item):
    return item.getValue()

def weightInverse (item):
    return 1.0/item.getWeight()

def density (item):
    return item.getValue()/item.getWeight()

def buildItems(names,values,weights):
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items

def greedy(items,maxWeight,keyFunction):
    itemsCopy = sorted(items , key = keyFunction , reverse = True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result,totalValue)

def testGreedy(items,constraint,keyFunction):
    taken,val = greedy(items,constraint,keyFunction)
    print ('Total value of items taken = ',val)
    for item in taken:
        print ('   ',item)

def testGreedys(names,values,weights,maxWeight = 20):
    items = buildItems(names,values,weights) # maddeler oluşturuluyor
    print('use greedy by value to fill knapsack of size',maxWeight) # sırt çantasını doldurmak için,maddeler sıralanırken keyFunction olarak value gönderiliyor ve değerlerine göre sıralandıklarında sırt çantasını dolduracak eleman sadece bilgisayar olmuş oluyor.
    testGreedy(items,maxWeight,value)
    print('\nuse greedy by weight to fill knapsack of size',maxWeight) # sıralamada kullanılacak keyfunction olarak weightInverse gönderiliyor.
    testGreedy(items,maxWeight,weightInverse)
    print('\nuse greedy by density to fill knapsack of size',maxWeight) #keyFunction = density
    testGreedy(items,maxWeight,density)

def chooseBest(pset , maxWeight , getVal , getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal >bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet,bestVal)

from pprint import pprint as pp
from itertools import chain,combinations
def genPowerSet(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
#pp(set(genPowerSet({1,2,3})))

def testBest(names,values,weights,maxWeight = 20):
    items = buildItems(names,values,weights)
    pset = genPowerSet(items)
    taken , val = chooseBest(pset , maxWeight , Item.getValue , Item.getWeight)
    print("total value of items taken = ",val)
    for item in taken:
        print(item)

names = ['clock','painting','radio','vase','book','computer']
values = [175,90,20,50,10,200]
weights = [10,9,4,2,1,20]

print("----SOLUTION WITH USING GREEDY ALGORITHM----\n")
testGreedys(names,values,weights)

print("----BRUTE - FORCE OPTIMAL SOLUTION TO THE 0/1 KNAPSACK PROBLEM----\n")
testBest(names,values,weights)

