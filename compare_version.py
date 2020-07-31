class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        m, n = len(version1_list), len(version2_list)
        i = 0
        min_l = min(m, n)
        while i < min_l:
            v1, v2 = int(version1_list[i]), int(version2_list[i])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            i += 1
        if m < n:
            for i in range(m, n):
                if int(version2_list[i]) != 0:
                    return -1
        if m > n:
            for i in range(n, m):
                if int(version1_list[i]) != 0:
                    return 1
        return 0


if __name__ == '__main__':
    version1 = '1.0.1'
    version2 = '1'
    solu = Solution()
    print(solu.compareVersion(version1, version2))
