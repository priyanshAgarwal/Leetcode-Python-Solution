
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


def minimalOperations(words):
    counter = [0] * len(words)

    for index, word in enumerate(words):
        count = 0
        i = 0
        while i < len(word) - 1:  # Iterate till second-to-last character
            if word[i] == word[i + 1]:
                count += 1
                i += 1  # Skip the next character since it's already accounted for
            i += 1

        counter[index] = math.ceil(count / 2)  # Take ceiling for odd repetitions
    return counter

words = ['add','boook','break','Maaaaaaiasasasas']
print(minimalOperations(words))