# cook your dish here

"""
22. Generate Parentheses
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""


def generateParanthesis(n:int)->list:
    result = []
    stack = [('',0,0)]
    
    while stack:
        s, left, right = stack.pop()
        
        if len(s)==2*n:
            result.append(s)
            
        if left<n:
            stack.append((s+'(',left+1,right))
            
        if right<left:
            stack.append((s+')',left,right+1))

    
    return result


# print(generateParanthesis(2))
