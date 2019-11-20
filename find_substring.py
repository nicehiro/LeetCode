from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        nums = len(words)
        if nums == 0:
            return []
        length = len(words[0])
        res = []
        if len(s) - nums * length < 0:
            return res
        for i in range(len(s) - nums * length + 1):
            temp = words.copy()
            j = 0
            while j < nums:
                if s[i+j*length:i+(j+1)*length] not in temp:
                    break
                else:
                    temp.remove(s[i+j*length:i+(j+1)*length])
                    j += 1
            if j >= nums:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    st = 'wordgoodgoodgoodbestword'
    words = ["word","good","best","good"]
    print(s.findSubstring(st, words))