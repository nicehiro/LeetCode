class Solution:
    def calculate(self, s: str) -> int:
        num, sign = 0, "+"
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c != " ":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = c

        if sign == "+":
            stack.append(num)
        elif sign == "-":
            stack.append(-num)
        elif sign == "*":
            stack[-1] *= num
        else:
            stack[-1] = int(stack[-1] / num)
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.calculate("14-3 / 2"))
