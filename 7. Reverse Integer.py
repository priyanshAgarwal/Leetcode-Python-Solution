class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign_negative=False
        x=abs(x)
        if(x<0):
            sign_negative=True
        while x>0:
            ans = ans * 10 + x % 10
            x=int(x/10)
        if(sign_negative==True):
            ans=-1*ans
        if ans >= 2**31-1 or ans <= -2**31: return 0
        else: return(ans) 



def rev(n):
    ans=0
    while n>0:
        n, digit=divmod(n,10)
        ans=ans*10+digit
    return ans
# a=Solution()
print(rev(123))