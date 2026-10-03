class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        suf = [1]*len(nums)
        prod = 1
        for i in range(len(nums)):
            pre[i] = prod
            prod *= nums[i]
            
        prod = 1
        for i in range(len(nums) - 1,-1, -1):
            suf[i] = prod
            prod *= nums[i]
            
        res = [] 
        for i in range(len(nums)):
            res.append(pre[i]*suf[i])

        return res        