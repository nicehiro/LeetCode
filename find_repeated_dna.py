from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # return self.brute_force(s)
        return self.hash_method(s)

    def brute_force(self, s: str):
        res = []
        for i in range(len(s)):
            for j in range(i+1, len(s)-9):
                if s[i:i+10] in res:
                    break
                if s[i:i+10] == s[j:j+10]:
                    res.append(s[i:i+10])
        return res

    def hash_method(self, s: str):
        res = []
        visited = set()
        for i in range(0, len(s)-9):
            if s[i:i+10] in visited and s[i:i+10] not in res:
                res.append(s[i:i+10])
            else:
                visited.add(s[i:i+10])
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "AAAAAAAAAAA"
    print(solu.findRepeatedDnaSequences(s))
