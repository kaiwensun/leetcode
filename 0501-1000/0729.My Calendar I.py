class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left =  self.right = None

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        res = self.insert(self.root, start, end)
        self.root = self.root or res
        return bool(res)

    def insert(self, root, start, end):
        if root is None:
            return Node(start, end)
        if end <= root.start:
            res = self.insert(root.left, start, end)
            root.left = root.left or res
            return res and root
        if start >= root.end:
            res = self.insert(root.right, start, end)
            root.right = root.right or res
            return res and root
