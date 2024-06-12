
import math
def count_adjecent_words(words):

    pnt1=0
    pnt2=1
    counter = 0
    words=words+'0'
    while pnt1<len(words) and pnt2<len(words):
        if words[pnt1]!=words[pnt2]:
            pnt1+=1
            pnt2+=1
        else:
            if words[pnt1]==words[pnt2]:
                while words[pnt1]==words[pnt2] and pnt2<len(words):
                    pnt2+=1
                counter += pnt2-pnt1
                pnt1 = pnt2-1
    return counter



