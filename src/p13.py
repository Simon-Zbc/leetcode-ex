## Runtime 46.1%
## Memory 67.1%
class Solution:
    def romanToInt(self, s: str) -> int:
        principle_map = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }
        res = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in principle_map and i+1 < len(s):
                res += principle_map[s[i:i+2]]
                i += 2
            else:
                res += principle_map[s[i]]
                i += 1
        return res