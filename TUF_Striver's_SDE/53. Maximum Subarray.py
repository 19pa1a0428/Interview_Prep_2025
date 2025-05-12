##Brute Force --> will lead to time limit exceeded
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                summ = sum(nums[i:j+1])
                maxx = max(summ, maxx)
        return maxx
        



##Optimal approach
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            maxx = max(summ,maxx)

            if summ <0:
                summ = 0

        return maxx
        
