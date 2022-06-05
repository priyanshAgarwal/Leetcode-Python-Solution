# cook your dish here

"""

"""

s = "The quick brown fox jumps over the lazy dog."
print(s)

def count_common_word(s):
    count=dict()
    s=s.lower()
    words=s.split()
    for word in words:
        count[word]=count.get(word,0)+1
    
    print(count)
    print(max(count.items()),'Max Items')
    print(count.get(max(count)),"'Max value Using Get'")
    print(max(count),"'Max Key on dictionary'")
    print(count[max(count)])
    print(max(count,key=count.get))
    print(f"The most common word is '{sorted(count)[-1]}', with a count of {count[sorted(count)[-1]]}")
    return sorted(count)[-1]      
            
count_common_word(s)
