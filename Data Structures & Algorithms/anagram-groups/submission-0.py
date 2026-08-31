class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = dict()
        alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for word in strs:
            freq = {}
            for f in alph:
                freq[f] = 0
            for s in word:
                freq[s] = freq[s] + 1
            f = tuple(freq.values())
            if f in words:
                words[f].append(word)
            else:
                words[f] = [word]
        
        ans = []
        for a in words.values():
            ans.append(a)
        return ans