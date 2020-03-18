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
#print(a)
def read_input():
    with open("input.txt", "r", encoding="utf-8") as file:
        new_input = file.read()
        words = new_input.split("\n")
    return words
def len_control():
    last_word =list()
    input1 = read_input()
    for i in input1:
        i=i.split()
        if len(i)>5:
            last_word.append("error")
        else:
            last_word.append(i[-1])
    return last_word
print(len_control())
def after_word():
    output=open("output.txt","w")
    for last_word in len_control():
        after_word = {}
        if last_word=="error":
            output.write(last_word+" - ")
        else:
            output.write(last_word+" - ")
        for word in list_1:
            if word==last_word:
                index = list_1.index(word)
                sonrakiKelime = list_1[index + 1]
                list_1.remove(word)
                if sonrakiKelime in after_word:
                    after_word[sonrakiKelime] = after_word[sonrakiKelime] + 1
                else:
                    after_word[sonrakiKelime] = 1
        maxValue=0
        for i in after_word:
            print(after_word)
            if maxValue < after_word[i]:
                maxValue=after_word[i]
                onerilecekKelime=i
        if last_word!="error":
            output.write(onerilecekKelime)
            output.write("\n")
    return after_word
after_word()
