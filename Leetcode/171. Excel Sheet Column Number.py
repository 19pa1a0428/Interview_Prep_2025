class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        n=len(columnTitle)
        for x in columnTitle:
            ans=ans+(ord(x)-ord("A")+1)*26**(n-1)
            n-=1
        return ans
