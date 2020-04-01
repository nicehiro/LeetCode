from functools import reduce


class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        res = ['/']
        while i < len(path):
            if i == len(path)-1:
                res = self.concat(res)
                return res
            j = i + 1
            while j < len(path) and path[j] != '/':
                j += 1
            t = path[i+1 : j]
            if t == '.':
                pass
            elif t == '':
                pass
            elif t == '..':
                # reverse a level
                if len(res) > 1:
                    res.pop(-1)
            else:
                res.append(t)
            i = j
        res = self.concat(res)
        return res

    def concat(self, s):
        if len(s) == 1:
            return s[0]
        s = reduce(lambda x, y: x + '/' + y, s)
        return s[1:]


if __name__ == "__main__":
    s = Solution()
    st = "/a//b////c/d//././/.."
    print(s.simplifyPath(st))
