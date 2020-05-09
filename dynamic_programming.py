import random
def fibonacci(value):
    #print("current call is: ",value)
    if value == 0 or value == 1:
        return 1
    else:
        return fibonacci(value-1) + fibonacci(value-2)
#value = int(input("please give me a number: "))
#print(fibonacci(value))

"""
fibonacci_fast fonksiyonu sayesinde ağaç yapısı şeklindeki tekrarlı çağırımları engellemiş oluyoruz.
örneğin; fibonacci_fast(3)'ü hafızaya alıyor ve onu test ederek varsa onu test et yoksa recursive olarak fonksiyona devam et.
n adımda tamamlanır.

"""
def fibonacci_fast(value , memory = {}):
    #print("current call :",value)
    if value == 0 or value == 1:
        return 1
    try:
        return memory[value]
    except KeyError:
        result = fibonacci_fast(value - 1) + fibonacci_fast(value-2)
        memory[value] = result
        return result

#value2 = int(input("give me a number again: "))
#print(fibonacci_fast(value2))

class Item(object):
    def __init__(self,n,v,w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self): #this function converts Python objects into strings
        result = '<' + self.name + ', ' + str(self.value) + ', '+str(self.weight) + '>'
        return result
def value(item):
    return item.getValue()
def weight(item):
    return item.getWeight()

def maxVal(toConsider,avail):
    if toConsider == [] or avail == 0: #çantaya konulan eşya yok veya çantada yer yok
        return (0,()) # 0 , o anki duruma dair boş bir tuple
    elif toConsider[0].getWeight() > avail: #il elemanın ağırlığı listenin kapasitesinden büyük
        result = maxVal(toConsider[1:],avail) #ilk eleman hariç listenin kalan elemanları tekrar fonksiyona gönder
    else: # ilk elemanın ağırlığı çantanın kapasitesine uygun
        nextItem = toConsider[0] #ilk elemanı nextItemda tut
        withVal,withToTake = maxVal(toConsider[1:],avail-nextItem.getWeight()) #ilk elemanın ağırlığını kapasiteden çıkarıp(çünkü çantaya alındı) kalan elemanları tekrar fonksiyona gönder
        withVal += nextItem.getValue() #ilk elemanın çantaya alındığı durum
        withoutVal,withoutToTake = maxVal(toConsider[1:],avail) #ilk elemanı çantaya almadığı durum
        #en iyi durumu seçmek için:
        if withVal > withoutVal:
            result = (withVal,withToTake+(nextItem,))
        else:
            result = (withoutVal,withoutToTake)
    return result

def smallTest():
    names = ['a','b','c','d']
    vals = [6,7,8,9]
    weights = [3,3,12,25]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    val,taken = maxVal(Items,5) #çantanın kapasitesi 5
    for item in taken:
        print(item)
    print("total value of items taken = ",val)
smallTest()

#bu algoritmayı çok fazla sayıdaki örnekler için kullanmak istersek:
def buildManyItems(numItems , maxVal , maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i),random.randint(1,maxVal),random.randint(1,maxWeight)))
    return items

def bigTest(numItems): #item sayısını parametre olarak alıyor.
    items = buildManyItems(numItems,10,10)
    val,taken = maxVal(items,40)
    print("items taken")
    for item in taken:
        print(item)
    print("total value of items taken = ",val)

bigTest(4)

#memo zaten çözülmüş olan alt problemlerin çözümlerini takip etmek için ekstra bir parametredir
def fastMaxVal(toConsider , avail , memo = {}): #memo sadece recursive çağırımlarda kullanılıyor,toConsider itemların bir listesi, avail de ağırlık
    if(len(toConsider) , avail) in memo: #başlangıçta memoda mı diye bak
        result = memo[(len(toConsider),avail)] # len(toConsider) ifadesi dikkate alınacak öğeleri temsil etmenin kısa ve öz bir yoludur.
    #memeoda yoksa aşağıdaki işlemleri yap:
    elif toConsider == [] or avail == 0:
        result = (0,())
    elif toConsider[0].getWeight() > avail:
        result = fastMaxVal(toConsider[1:] , avail , memo)
    else:
        nextItem = toConsider[0]
        withVal , withToTake = fastMaxVal(toConsider[1:] , avail - nextItem.getWeight() , memo)
        withVal += nextItem.getValue()

        withoutVal , withoutToTake = fastMaxVal(toConsider[1:] , avail , memo)

        if withVal > withoutVal:
            result = (withVal , withoutToTake + (nextItem,))
        else:
            result = (withoutVal , withoutToTake)
    memo[(len(toConsider),avail)] = result #en son bulduğun resultı memeoya al
    return result









































