from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        return self.two_side(ratings)

    def bruse_force(self, ratings):
        high_s = 0
        update = False
        i = 1
        res = [1 for _ in range(len(ratings))]
        while i < len(ratings):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
                update = True
            elif ratings[i] == ratings[i-1]:
                high_s = i
            else:
                if update:
                    high_s = i - 1
                    update = False
                for j in range(i-1, high_s-1, -1):
                    if res[j] > res[j+1]:
                        break
                    res[j] += 1
            i += 1
        return sum(res)

    def two_side(self, ratings):
        res = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                res[i] = res[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)
        return sum(res)


if __name__ == '__main__':
    solu = Solution()
    ratings = [5, 4, 3, 2, 1, 3, 4, 5]
    # ratings = [1,3,2,2,1]
    # ratings = [1,2,3,1,0]
    print(solu.candy(ratings))
