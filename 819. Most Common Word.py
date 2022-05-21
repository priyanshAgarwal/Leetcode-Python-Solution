# cook your dish here

"""
819. Most Common Word
Easy

1164

2403

Add to List

Share
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

"""
from collections import Counter
import re


string='a quick brown fox jumps over the lazy dog'
hash_map=Counter(string)        
print(hash_map)



from collections import Counter
import re

# Method 1 (Delete a key, values from Hash_Map)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.findall('\w+',paragraph.lower())
        hash_map=Counter(paragraph)        
        for word in banned:
            del hash_map[word]
        return(hash_map.most_common(1)[0][0])
        # print(paragraph)


# Method 2 (Change in For loop)
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.findall('\w+',paragraph.lower())
        hash_map=Counter(paragraph)        
        for word,num in hash_map.most_common():   
            if word not in banned:
                return(word)



# Method 3 (Withot any External Functions)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        removePunctuationTable=str.maketrans("!?',;.", "      ")
        paragraph = paragraph.translate(removePunctuationTable).lower()
        hash_map={}
        
        for word in paragraph.split():
            if word not in banned:
                hash_map[word]=hash_map.get(word,0)+1
                
        return(max(hash_map,key=hash_map.get)) #Remember how you get maximum from a dictionary

