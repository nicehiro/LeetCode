from typing import List
from functools import reduce, cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return self.method2(nums)

    def method1(self, nums):
        def compare(x: int, y: int) -> int:
            x, y = str(x), str(y)
            a, b = x + y, y + x
            for i in range(len(a)):
                if int(a[i]) > int(b[i]):
                    return 1
                elif int(a[i]) < int(b[i]):
                    return -1
            return 0

        res = sorted(nums, key=cmp_to_key(compare), reverse=True)
        res = str(reduce(lambda x, y: str(x) + str(y), res))
        for i in range(len(res) - 1):
            if res[i] != "0":
                return res[i:]
        return res[-1:]

    def method2(self, nums):
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        res = "".join(sorted(map(str, nums), key=key)).lstrip("0")
        return res or "0"


if __name__ == "__main__":
    solu = Solution()
    nums = [0, 0]
    print(solu.largestNumber(nums))
