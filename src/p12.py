## Runtime 89.8%
## Memory 67.5%
class Solution:
    def intToRoman(self, num: int) -> str:
        principle_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        res = ''
        for p in principle_map.keys():
            while p <= num:
                res += principle_map[p]
                num -= p
        return res