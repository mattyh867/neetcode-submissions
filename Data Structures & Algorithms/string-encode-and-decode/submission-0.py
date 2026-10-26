class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ''
        for s in strs:
            for c in s:
                r = r + chr(ord(c)+1)
            r = r + ' '
        r = r[:-1]
        return r

    def decode(self, s: str) -> List[str]:
        ans = ''
        for c in s:
            if c == ' ':
                ans = ans + ' '
            else:
                ans = ans + chr(ord(c)-1)
        return ans.split(' ')
