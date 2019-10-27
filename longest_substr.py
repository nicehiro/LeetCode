class Solution:
    """
    求字符串的最长字串问题

    滑动窗口
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        d = {}
        max_count = -1
        temp = 0
        while True:
            if i == len(s):
                if max_count < temp:
                    max_count = temp
                return max_count
            if d.get(s[i]) is None:
                d[s[i]] = i
                temp += 1
                i += 1
            else:
                i = d[s[i]] + 1
                d.clear()
                if max_count < temp:
                    max_count = temp
                temp = 0

if __name__ == '__main__':
    s = 'dddd'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
