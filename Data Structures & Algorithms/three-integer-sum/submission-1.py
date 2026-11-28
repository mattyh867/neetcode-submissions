class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for i in range(len(nums)):
            numMap = dict()
            for j in range(len(nums)):
                if j != i:
                    complement = 0 - nums[i] - nums[j]
                    if complement in numMap:
                        res.append([i, numMap[complement], j])
                    numMap[nums[j]] = j

        return res