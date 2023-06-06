from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        target = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            target.append(mat[i])
        for j in range(n):
            l = []
            for i in range(m):
                l.append(mat[i][j])
            target.append(l)
        res = m * n - 1
        # for i in range(m + n):
        #     ans = 0
        #     for j in range(len(target[i])):
        #         ans = max(ans, arr.index(target[i][j]))
        #     res = min(res, ans)

        for i in range(len(arr)):
            for j in range(m + n):
                if arr[i] in target[j]:
                    target[j].remove(arr[i])
                    if target[j] == []:
                        return i
        return res
    
s = Solution()
print(s.firstCompleteIndex([15,25,4,11,9,7,20,1,6,14,21,18,24,2,12,17,19,22,16,10,5,8,23,3,13], [[3,1,25,14,16],[24,20,9,19,13],[10,22,18,12,2],[6,5,17,23,11],[4,8,15,21,7]]))