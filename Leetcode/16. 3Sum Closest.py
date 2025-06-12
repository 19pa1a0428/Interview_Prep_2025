#3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0 
        j = len(nums)-1
        closesum = 1000
        while i < j:
            k = i+1
            while k<j:
                cursum =nums[k]+nums[i]+nums[j]
                if cursum == target:
                    return (cursum)
                elif  abs(cursum-target)<abs(closesum - target):
                    closesum = cursum
                elif(cursum < target):
                    k+=1
                else:
                    j-=1
            i+=1
            j = len(nums)-1
 
        return closesum
