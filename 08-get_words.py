def get_words(my_file=u"//home//betul//python//1.txt"):
    my_list=[]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:
        #print(line)
        words=line.split(" ")
        for word in words:
            #print(word)
            my_list.append(word)
    #print(contents)
    f.close()
    
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
get_hist(list_1)
