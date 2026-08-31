class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compls = dict()
        
        for i in range(len(nums)):
            if nums[i] in compls.keys():
                return [compls[nums[i]], i]
            else:
                complement = target - nums[i]
                compls[complement] = i