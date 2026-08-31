class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        ans = 0
        counter = 0
        hashTable = dict()

        for num in nums:
            hashTable[num] = True

        x = min(hashTable.keys())
        while len(hashTable) > 0:
            if x in hashTable.keys():
                hashTable.pop(x)
                counter += 1
                ans = max(ans, counter)
                x += 1
            elif len(hashTable) > 0:
                x = min(hashTable.keys())
                counter = 0
            else:
                print("HUT")
                ans = max(ans, counter)
                return ans

        ans = max(ans, counter)
        return ans