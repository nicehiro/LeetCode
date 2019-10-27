class Solution:
    def longestPalindrome_1(self, s: str) -> str:
        res = ''
        max_res = -1
        d = {}
        for i in range(len(s)):
            d.clear()
            k1, k2, end = i, len(s)-1, len(s)-1
            while k1 < k2:
                if s[k1] == s[k2]:
                    k1 += 1
                    k2 -= 1
                else:
                    k1 = i
                    k2 = end - 1
                    end = end - 1

            l = len(s[i:end+1])
            if l > max_res:
                res = s[i:end+1]
                max_res = l
        return res


    def longestPalindrome(self, s: str) -> str:
        new_s = '#'
        max_len = -1
        max_j = max_k = -1
        for c in s:
            new_s += c + '#'
        for i in range(len(new_s)):
            j, k = i - 1, i + 1
            temp = 1
            while j >= 0 and k < len(new_s) and new_s[j] == new_s[k]:
                temp += 2
                j -= 1
                k += 1
            if temp > max_len:
                max_len = temp
                max_j = j + 1
                max_k = k - 1
        res = new_s[max_j:max_k+1].replace('#', '')
        if res == '' and len(res) > 0:
            res = s[0]
        return res


    def manacher(self, s: str) -> str:
        """Manacher Algorithm
        边界值也不能直接不求
        """
        new_s = '#'
        for c in s:
            new_s += c + '#'
        max_right = -1
        max_mid = -1
        l = len(new_s)
        palind_list = []
        for c in range(l):
            if c < max_right:
                temp = min(palind_list[2 * max_mid - c], max_right - c)
                i = c - temp
                j = c + temp
            else:
                temp = 0
                i = j = c
            while i >= 0 and j < l and new_s[i] == new_s[j]:
                temp += 1
                i -= 1
                j += 1
            palind_list.append(temp)
            if j-1 > max_right:
                max_right = j - 1
                max_mid = c
        return palind_list


if __name__ == '__main__':
    s = Solution()
    st = 'babad'
    print(s.manacher(st))
