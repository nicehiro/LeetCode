class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.hard(nums)

    def easy(self, nums):
        db = {}
        for n in nums:
            if n in db:
                db[n] += 1
            else:
                db[n] = 1
            if db[n] == 3:
                db.pop(n)
        return [*db][0]

    def hard(self, nums):
        seen_once = seen_twice = 0
        for n in nums:
            seen_once = ~seen_twice & (seen_once ^ n)
            seen_twice = ~seen_once & (seen_twice ^ n)
        return seen_once



if __name__ == '__main__':
    solu = Solution()
    nums = [2,2,3,2]
    print(solu.singleNumber(nums))
