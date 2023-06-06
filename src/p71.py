## Runtime 10.0%
## Memory 10.3%
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        path = path.split("/")
        for p in path:
            if res and p == "..":
                res.pop()
            elif p not in [".", "", ".."]:
                res.append(p)
        return "/" + "/".join(res)