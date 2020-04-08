class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.best(s, t)

    def bad(self, s: str, t: str) -> str:
        i = 0
        l = len(s)
        r = ''
        while i < len(s) + 1 - len(t):
            if s[i] in t:
                res = t
                j = i
                while j < len(s):
                    if s[j] in t:
                        res = res.replace(s[j], '', 1)
                        if res == '':
                            if j+1-i <= l:
                                r = s[i:j+1]
                                l = j + 1 - i
                            break
                    j += 1
            i += 1
        return r

    def better(self, s: str, t: str) -> str:
        min_window = len(s)
        w_l = 0
        w_r = len(s)
        i = 0
        has_found = False
        while i < len(s):
            if s[i] in t:
                res = t
                j = i
                while j < min(i + min_window, len(s)):
                    if s[j] in t:
                        res = res.replace(s[j], '', 1)
                        if res == '':
                            has_found = True
                            min_window = j + 1 - i
                            w_l = i
                            w_r = j + 1
                            break
                    j += 1
            i += 1
        return s[w_l:w_r] if has_found else ''

    def best(self, s: str, t: str):
        l = r = 0
        res = ''
        if len(s) < len(t):
            return res
        # use two dict record needs charactors and current l & r charactors
        needs = {}
        for c in t:
            if needs.get(c):
                needs[c] = needs[c] + 1
            else:
                needs[c] = 1
        n = needs.copy()
        w = {}
        while r < len(s):
            # find max substring to satify needs
            while r < len(s) and not self.is_satify(n, w):
                if w.get(s[r]):
                    w[s[r]] = w[s[r]] + 1
                else:
                    w[s[r]] = 1
                r += 1
            if not self.is_satify(n, w):
                break
            # find min substring to not satify needs
            while self.is_satify(n, w):
                w[s[l]] = w[s[l]] - 1
                l += 1
            if len(res) == 0 or r+1-l < len(res):
                res = s[l-1:r]
        return res

    def is_satify(self, n: dict, w: dict):
        for k, v in n.items():
            if not w.get(k) or w[k] < v:
                return False
        return True


if __name__ == '__main__':
    solu = Solution()
    s = 'a'
    t = 'b'
    print(solu.minWindow(s, t))
