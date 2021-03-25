# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def flatten_list(self, nestedList: [NestedInteger]):
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.flatten_list(nestedList)

    def next(self) -> int:
        return self.stack[-1].getInteger()

    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            self.flatten_list(self.stack.pop(-1).getList())
        if self.stack and self.stack[-1].isInteger:
            return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
