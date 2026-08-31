class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, l, r = [1]*n, 1, 1
        for i in range(n):
            ans[i] = ans[i] * l
            ans[-(i+1)] = ans[-(i+1)] * r
            l = l * nums[i]
            r = r * nums[-(i+1)]            
        return ans