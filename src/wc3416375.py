class Solution:
    def addMinimum(self, word: str) -> int:
        res = 0
        l = len(word)
        i = 0
        while i < l:
            if word[i] == "a":
                if word[i+1:i+2] == "b":
                    if word[i+2:i+3] == "c":
                        i += 3
                    else:
                        res +=1
                        i += 2
                elif word[i+1:i+2] == "a" or not word[i+1:i+2]:
                    res +=2
                    i += 1
                else:
                    res +=1
                    i += 2
            elif word[i] == "b":
                if word[i+1:i+2] == "c":
                    res +=1
                    i += 2
                else:
                    res +=2
                    i += 1
            else:
                res +=2
                i += 1
        return res