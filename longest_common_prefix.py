from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        min_len = min([len(x) for x in strs])
        length = len(strs)
        res = ''
        for i in range(min_len):
            temp = [s[i] for s in strs]
            if len(temp) > 0 and temp == [temp[0]] * length:
                res += temp[0]
            else:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    st = ["flower","flow","flight"]
    print(s.longestCommonPrefix(st))
