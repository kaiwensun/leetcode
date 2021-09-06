class LockingTree:

    def __init__(self, parent: List[int]):
        N = len(parent)
        self.parent = parent
        self.locked_by = [None] * N
        self.locked_subtrees = [set() for _ in range(N)]

    def lock(self, num: int, user: int) -> bool:
        if self.locked_by[num] is None:
            self.locked_by[num] = user
            p = self.parent[num]
            while p != -1:
                self.locked_subtrees[p].add(num)
                num, p = p, self.parent[p]
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by[num] == user:
            self.locked_by[num] = None
            if not self.locked_subtrees[num]:
                p = self.parent[num]
                while p != -1:
                    self.locked_subtrees[p].remove(num)
                    if self.locked_subtrees[p] or self.locked_by[p] is not None:
                        break
                    num, p = p, self.parent[p]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked_by[num] is not None:
            return False
        if not self.locked_subtrees[num]:
            return False
        p = self.parent[num]
        while p != -1:
            if self.locked_by[p] is not None:
                return False
            p = self.parent[p]

        def unlock_all(num):
            self.locked_by[num] = None
            for child in self.locked_subtrees[num]:
                unlock_all(child)
            self.locked_subtrees[num].clear()

        unlock_all(num)
        self.lock(num, user)
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

