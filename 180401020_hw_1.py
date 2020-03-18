def get_words():
    my_list=[]
    for i in range(1,10):
        with open("{}.txt".format(i),"r",encoding="utf-8") as f:
            contents=f.read()
            words=contents.split()
            for word in words:
                my_list.append(word)
    return my_list
def get_hist(my_list):
    my_hist={}
    for w in my_list:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist[w]=1
    return my_hist
list_1=get_words()
a=get_hist(list_1)
print(a)
kelime=input("lütfen string giriniz!= ")
def sonInputaGit(kelime):   
    kelimeler=kelime.split()
    n=len(kelimeler)
    if n>=5:
        return "kelime sayısı beşten fazla olamaz"
    else:
        return kelimeler[-1]
def inout_output(in_1,out):
    inputs=open("input.txt","w")
    inputs.write(in_1)
    inputs.write("\n")
    output=open("output.txt","w")
    output.write(in_1+"-"+out)
    output.write("\n")
    inputs.close()
    output.close()
def nextword():
    nextList=list()
    sonkelime=sonInputaGit(kelime)
    for kelime_1 in list_1:
        if kelime_1==sonkelime:
            index=list_1.index(kelime_1)
            sonrakiKelime=list_1[index+1]
            nextList.append(sonrakiKelime)
            list_1.remove(kelime_1)
    return nextList
sonrakiKelimeListesi=nextword()
maxValue=0
print(sonrakiKelimeListesi)
for i in sonrakiKelimeListesi:
    if maxValue<a[i]:
        maxValue=a[i]
        onerilecekKelime=i
print(onerilecekKelime)
inout_output(kelime,onerilecekKelime)
