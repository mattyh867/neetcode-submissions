class Solution:
    def isPalindrome(self, s: str) -> bool:
        n, l = len(s), 0
        r = n-1
        while l < r:
            print(f'l={s[l]} r={s[r]}')
            if s[l].isalnum() != True:
                l += 1
                continue
            if s[r].isalnum() != True:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True