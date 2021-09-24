# cook your dish here

"""
1859. Sorting the Sentence
Easy

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
 

Constraints:

2 <= s.length <= 200
s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
The number of words in s is between 1 and 9.
The words in s are separated by a single space.
s contains no leading or trailing spaces.

"""


#Method 1

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s[::-1].split() # Get the last number in front
        words.sort() # Sort by first letter
        result=[word[1:][::-1] for word in words] 
        # Only take from first element but also revese each letter 
        return(' '.join(result)) #Ther have to be space between each word.


#Method 2 Using Dictionaries (Much Faster Approach)
class Solution1(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_res={}
        res_str=''
        for word in s.split():
            dict_res[word[-1]]=word[:-1]
            # word[-1] gets the last alphabet from string
            # word[:-1] get the whole string excluding the last alphabet
        for i in sorted(dict_res):
            res_str+=dict_res[i]+' '
            
        return(strip(res_str))

        #return(' '.join(dict_res[i] for i in sorted(dict_res))) THis could also be used