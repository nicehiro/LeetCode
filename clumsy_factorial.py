class Solution:
    def clumsy(self, N: int) -> int:
        return self.method2(N)

    def method1(self, N):
        s = [i + 1 for i in range(N)]
        ops = ["*", "/", "+", "-"]
        s_ = []
        # calc * /
        for i in range(N - 1):
            op = ops[i % 4]
            l = s.pop()
            if op == "*":
                r = s.pop()
                s.append(l * r)
            elif op == "/":
                r = s.pop()
                s.append(l // r)
            else:
                s_.insert(0, l)
        # calc + -
        if len(s_) == 0:
            return s[0]
        s_.insert(0, s[0])
        n = len(s_)
        ops = ["+", "-"]
        for i in range(n - 1):
            op = ops[i % 2]
            l = s_.pop()
            r = s_.pop()
            if op == "+":
                s_.append(l + r)
            elif op == "-":
                s_.append(l - r)
        return s_[0]

    def method2(self, N):
        s = []
        nums = [i for i in range(N, 0, -1)]
        ops = ["*", "/", "+", "-"]
        s.append(nums[0])
        i = 1
        while i < N:
            op = ops[(i - 1) % len(ops)]
            if op == "*":
                l = s.pop()
                s.append(l * nums[i])
            elif op == "/":
                l = s.pop()
                s.append(int(l / nums[i]))
            elif op == "+":
                s.append(nums[i])
            else:
                s.append(-nums[i])
            i += 1
        return sum(s)

    def method3(self, N):
        res = []
        res.append(N)
        i = 1
        while i < N:
            op = (i - 1) % 4
            if op == 0:
                p = res.pop()
                res.append(p * (N - i))
            elif op == 1:
                p = res.pop()
                res.append(int(p / (N - i)))
            elif op == 2:
                res.append(N - i)
            elif op == 3:
                res.append(i - N)
            i += 1
        return sum(res)


if __name__ == "__main__":
    s = Solution()
    print(s.clumsy(4))
