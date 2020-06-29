from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.res = []
        self.end_word = endWord
        if endWord not in wordList:
            return []
        self.min_num = float('inf')
        self.recursive(beginWord, wordList, [beginWord], 0)
        return self.res

    def recursive(self, start_word, word_list, trans, num):
        if start_word == self.end_word:
            if num < self.min_num:
                self.res.clear()
                self.min_num = num
            if num == self.min_num:
                self.res.append(trans)
            return
        for word in word_list:
            if self.can_transform(start_word, word):
                t1 = word_list.copy()
                t1.remove(word)
                t2 = trans.copy()
                t2.append(word)
                self.recursive(word, t1, t2, num+1)

    def can_transform(self, word_a, word_b):
        if len(word_a) != len(word_b):
            return False
        diff = 0
        for i in range(len(word_a)):
            if word_a[i] == word_b[i]:
                continue
            else:
                diff += 1
            if diff > 1:
                return False
        return True


class Solution2:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        self.begin_word = beginWord
        self.id_words = wordList
        if self.begin_word not in self.id_words:
            self.id_words.append(beginWord)
        self.word_ids = {self.id_words[i]: i for i in range(len(self.id_words))}
        self.edges = [[] for _ in range(len(self.id_words))]
        self.visited = [False for _ in range(len(self.id_words))]
        self.end_word = endWord
        self.prev = [[] for _ in range(len(self.id_words))]
        self.res = []
        self.construct_edges()
        self.bsf()
        self.reverse_bsf(self.word_ids[self.end_word], [self.end_word])
        return self.res

    def construct_edges(self):
        for i in range(len(self.id_words)):
            for j in range(i+1, len(self.id_words)):
                if self.can_transform(self.id_words[i], self.id_words[j]):
                    self.edges[i].append(j)
                    self.edges[j].append(i)

    def can_transform(self, word_a, word_b):
        if len(word_a) != len(word_b):
            return False
        diff = 0
        for i in range(len(word_a)):
            if word_a[i] == word_b[i]:
                continue
            else:
                diff += 1
            if diff > 1:
                return False
        return True

    def bsf(self):
        q = [self.begin_word]
        while len(q) > 0:
            last = []
            while len(q) > 0:
                a = q.pop(0)
                a_id = self.word_ids[a]
                last.append(a_id)
                self.visited[a_id] = True
            for last_id in last:
                for i in self.edges[last_id]:
                    if not self.visited[i]:
                        q.append(self.id_words[i])
                        if last_id not in self.prev[i]:
                            self.prev[i].append(last_id)

    def reverse_bsf(self, id, strs: List):
        if self.id_words[id] == self.begin_word:
            self.res.append(strs)
            return
        for p_id in self.prev[id]:
            s = strs.copy()
            s.insert(0, self.id_words[p_id])
            self.reverse_bsf(p_id, s)


if __name__ == '__main__':
    solu = Solution2()
    beginWord = "red"
    endWord = "tax"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    # wordList = ['a', 'b', 'c']
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    print(solu.findLadders(beginWord, endWord, wordList))
