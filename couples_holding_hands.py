from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def check_couple(x, y):
            min_n, max_n = min(x, y), max(x, y)
            return True if min_n % 2 == 0 and max_n - min_n == 1 else False

        def find_partner(x):
            if x % 2 == 0:
                return x + 1
            else:
                return x - 1

        n = len(row)

        if n % 2 != 0:
            raise Exception("length of row should be divided by 2.")
        stack = []
        pos = {}
        for i in range(n // 2):
            if not check_couple(row[2 * i], row[2 * i + 1]):
                stack.append(2 * i)
                stack.append(2 * i + 1)
                pos[row[2 * i]] = 2 * i
                pos[row[2 * i + 1]] = 2 * i + 1

        res = 0
        while stack:
            p = stack.pop(0)
            a = row[p]
            changer_p = find_partner(p)
            changer_a = row[changer_p]
            partner_a = find_partner(a)
            partner_p = pos[partner_a]
            if changer_a == partner_a:
                continue
            row[changer_p] = partner_a
            row[partner_p] = changer_a
            pos[partner_a] = changer_p
            pos[changer_a] = partner_p
            res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    row = [0, 2, 4, 6, 7, 1, 3, 5]
    print(s.minSwapsCouples(row))
