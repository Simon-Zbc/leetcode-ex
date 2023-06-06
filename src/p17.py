from typing import List


## Runtime 75.4%
## Memory 65.6%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(letters[digits[0]])
        else:
            last = list(letters[digits[-1]])
            prev_digits = self.letterCombinations(digits[:-1])
            return [p + l for l in last for p in prev_digits]