#Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(map(str,s.split()))
        p=""
        x=" "
        for i in range(len(l)):
            a=l[i]
            if(i==(len(l)-1)):
                p=p+a[::-1]
            else:
                p=p+a[::-1]+x
        return(p)    
