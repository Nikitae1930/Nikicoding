class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
           
        @cache
        def dp(i, maxnum, minnum):
            # return the longest subarray ended at i, maxnum: maximum number we can choose, minnum: minimum number we can choose
            ans=1
            if i>=1:
                if nums[i]==nums[i-1]:
                    ans+=dp(i-1, maxnum, minnum)
                if minnum<=nums[i-1]<nums[i]:
                    ans+=dp(i-1, min(maxnum, nums[i-1]+2), minnum)
                if nums[i]<nums[i-1]<=maxnum:
                    ans+=dp(i-1, maxnum, max(minnum, nums[i-1]-2))
            return ans
        
        return sum([dp(i, nums[i]+2, nums[i]-2) for i in range(len(nums))])
        