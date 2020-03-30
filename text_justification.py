from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        temp = []
        w = maxWidth
        total_l = 0

        temp.append(words[0])
        total_l += len(words[0])
        w -= len(words[0])
        for i in range(1, len(words)):
            word = words[i]
            l = len(word)
            if w < l+1:
                # rearrange temp
                r = self.rearrange(temp, maxWidth, total_l)
                res.append(r)
                temp = [word]
                w = maxWidth - l
                total_l = l
                continue
            total_l += l
            w = w - l - 1
            temp.append(word)
        if len(temp) > 0:
            r = self.rearrange(temp, maxWidth, total_l, True)
            res.append(r)
        return res
        
    def rearrange(self, s, w, l, is_last=False):
        n = len(s)
        st = ''
        free = w - l
        if n == 1:
            st = s[0] + ' ' * free
            return st
        other_space = free // (n - 1)
        long_space_n = free % (n - 1)
        first_space = other_space + 1 if long_space_n != 0 else other_space
        last_space = 0
        if is_last:
            other_space = first_space = 1
            last_space = free - (n - 1)
        st += s[0] + ' ' * first_space
        i = 1
        while i < n - 1:
            space = first_space if i < long_space_n else other_space
            st += s[i] + ' ' * space
            i += 1
        st += s[n-1] + ' ' * last_space
        return st


if __name__ == "__main__":
    s = Solution()
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print(s.fullJustify(words, maxWidth))