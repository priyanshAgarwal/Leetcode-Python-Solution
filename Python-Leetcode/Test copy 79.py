# cook your dish here

"""

"""
def longestPalindrome(s:str)->str:
    maxLenght = ''
    
    for i in range(1,len(s)):
        oddLength = expandAroundCentre(i,i,s)
        if len(oddLength)>len(maxLenght):
            maxLenght=oddLength

        evenLength = expandAroundCentre(i-1,i,s)
        if len(evenLength)>len(maxLenght):
            maxLenght=evenLength

    return maxLenght

def expandAroundCentre(left, right, s)->str:
    left = 0
    right = len(s)-1
    
    while left>0 and right<len(s) and s[left]==s[right]:
        left+=1
        right-=1
    return s[left:right+1]    
    

print(longestPalindrome('bb'))