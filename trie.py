class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.tree
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t["Done"] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.tree
        for w in word:
            if w not in t:
                return False
            t = t[w]
        return True if "Done" in t else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.tree
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == "__main__":
    s = Trie()
    s.insert("apple")
    print(s.search("apple"))
    print(s.startsWith("app"))
    print(s.search("app"))
