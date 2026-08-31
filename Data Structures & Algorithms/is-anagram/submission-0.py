class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters1 = dict()
        for i in s:
            if i in characters1:
                characters1[i] = characters1[i] + 1
            else:
                characters1[i] = 1
        characters2 = dict()
        for j in t:
            if j in characters2:
                characters2[j] = characters2[j] + 1
            else:
                characters2[j] = 1
        print(f'{characters1} {characters2}')
        if characters1 == characters2:
            return True
        return False