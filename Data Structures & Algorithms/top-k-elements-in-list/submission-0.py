class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        x = len(nums)
        for n in nums:
            if n in freq:
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1

        buck = [[] for _ in range(len(nums) + 1)]

        for f in freq.keys():
            buck[freq[f]].append(f)

        ans = []
        for i in range(len(buck) - 1, 0, -1):
            for n in buck[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans