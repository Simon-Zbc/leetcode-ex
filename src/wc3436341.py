from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        res1, res2 = 0, 0
        l1, l2 = len(player1), len(player2)
        flg = 0
        for i in range(l1):
            res1 += player1[i]
            if flg > 0:
                res1 += player1[i]
            if player1[i] == 10:
                flg = 3
            flg -= 1
        flg = 0
        for i in range(l2):
            res2 += player2[i]
            if flg > 0:
                res2 += player2[i]
            if player2[i] == 10:
                flg = 3
            flg -= 1
        print(res1)
        print(res2)

        if res1 > res2:
            return 1
        elif res1 == res2:
            return 0
        else:
            return 2

s = Solution()
print(s.isWinner([7,7,4,7,7], [7,2,3,10,10]))
print(s.isWinner([9,7,10], [5,9,0]))
print(s.isWinner([10,2,2,3], [3,8,4,5]))