from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        for num in nums_set:
            if num-1 not in nums_set:
                curr_seq = 1
                curr_num = num
                while curr_num+1 in nums_set:
                    curr_seq += 1
                    curr_num += 1
                longest_seq = max(longest_seq, curr_seq)
        return longest_seq


if __name__ == '__main__':
    solu = Solution()
    nums = [100, 4, 200, 1, 2, 3]
    print(solu.longestConsecutive(nums))