from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2:
            return None
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)
            while l < r:
                mid = (l + r) // 2
                if numbers[i] + numbers[mid] == target:
                    return [i+1, mid+1]
                if numbers[i] + numbers[mid] > target:
                    r = mid
                elif numbers[i] + numbers[mid] < target:
                    l = mid + 1


if __name__ == '__main__':
    solu = Solution()
    numbers = [5, 25, 75]
    print(solu.twoSum(numbers, 100))
