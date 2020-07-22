from functools import reduce


class Solution
    def reverseWords(self, s: str) -> str:
        flag = True
        for i in range(len(s)):
            if s[i] != ' ':
                start = i
                flag = False
                break
        words = []
        if flag:
            return ''
        s += ' '
        s_ = start
        for i in range(s_, len(s)):
            if not flag and s[i] == ' ':
                words.append(s[start:i])
                flag = True
            if flag and s[i] != ' ':
                start = i
                flag = False
        reversed = words[::-1]
        return reduce(lambda x, y: x + ' ' + y, reversed)


if __name__ == '__main__':
    solu = Solution()
    s = ' hello world '
    print(solu.reverseWords(s))
