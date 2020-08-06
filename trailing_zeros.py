class Solution:
    def trailingZeroes(self, n: int) -> int:
        return self.effective(n)

    def effective(self, n):
        # O(logn)
        five_times = 5
        zero_count = 0
        while n >= five_times:
            zero_count += n // five_times
            five_times *= 5
        return zero_count


    def linear(self, n):
        # O(n)
        zero_count = 0
        for i in range(5, n+1, 5):
            current = i
            while current % 5 == 0:
                zero_count += 1
                current //= 5
        return zero_count
