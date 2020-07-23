from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.nums = nums
        return self.iteration2()

    def recursive(self, s, e):
        if e - s == 1:
            return self.nums[s]
        if e <= s:
            return 0
        i = e - 1
        connect_product = max_connect_product = self.nums[i]
        while i > s:
            connect_product *= self.nums[i-1]
            max_connect_product = max(max_connect_product, connect_product)
            i -= 1
        return max(self.recursive(s, e-1), max_connect_product, self.nums[e-1])

    def iteration(self):
        max_products = [0 for _ in range(len(self.nums))]
        min_products = [0 for _ in range(len(self.nums))]
        max_products[0] = self.nums[0]
        min_products[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            max_products[i] = max(max_products[i-1] * self.nums[i], self.nums[i], min_products[i-1] * self.nums[i])
            min_products[i] = min(max_products[i-1] * self.nums[i], self.nums[i], min_products[i-1] * self.nums[i])
        return max(max_products)

    def iteration2(self):
        max_product = min_product = res = self.nums[0]
        for i in range(1, len(self.nums)):
            a, b = max_product, min_product
            max_product = max(a * self.nums[i], self.nums[i], b * self.nums[i])
            min_product = min(a * self.nums[i], self.nums[i], b * self.nums[i])
            res = max(res, max_product)
        return res


if __name__ == '__main__':
    solu = Solution()
    nums = [-4, -3, -2]
    print(solu.maxProduct(nums))
