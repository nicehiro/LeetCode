class Solution:
    def removeDuplicates(self, S: str) -> str:
        def recursive(s):
            n = len(s)
            res = ""
            last = None
            i = 0
            flag = False
            while i < len(s):
                if last == None or s[i] != last:
                    res += s[i]
                    last = s[i]
                else:
                    flag = True
                    res = res[:-1]
                    last = None
                i += 1
            return recursive(res) if flag else res

        # return recursive(S)
        return self.method2(S)

    def method2(self, S: str):
        stack = []
        n = len(S)
        for i in range(n):
            if not stack or S[i] != stack[-1]:
                stack.append(S[i])
            else:
                stack.pop(-1)
        res = ""
        for s in stack:
            res += s
        return res


if __name__ == "__main__":
    s = Solution()
    S = "abbaca"
    print(s.removeDuplicates(S))
