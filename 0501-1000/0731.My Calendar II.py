# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)



class Node(object):
    def __init__(self, start, end, cover=1):
        self.start, self.end = start, end
        self.cover = cover
        self.left =  self.right = None
    def add(self, start, end, cover):
        start = max(start, self.start)
        end = min(end, self.end)
        if self.cover + cover >= 3:
            return None
        if start == self.start and end == self.end:
            node = self.copy()
            node.cover += cover
            return node
        elif start == self.start:
            node = Node(start, end, self.cover + cover)
            node.right = Node(end, self.end, self.cover)
            node.right.right = self.right
            node.left = self.left
            return node
        elif end == self.end:
            node = Node(start, end, self.cover + cover)
            node.left = Node(self.start, start, self.cover)
            node.left.left = self.left
            node.right = self.right
            return node
        else:
            node = Node(start, end, self.cover + cover)
            node.left = Node(self.start, start, self.cover)
            node.right = Node(end, self.end, self.cover)
            node.left.left = self.left
            node.right.right = self.right
            return node
    def copy(self):
        node = Node(self.start, self.end, self.cover)
        node.left, node.right = self.left, self.right
        return node
        
    def __repr__(self):
        return '(%s, %s, %s, %s, %s)' % (self.start, self.end, self.cover, self.left, self.right)

    def __str__(self):
        return repr(self)

class MyCalendarTwo(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        res = self.insert(self.root, start, end)
        self.root = res or self.root
        return bool(res)

    def insert(self, root, start, end, cover=1):
        if root is None:
            return Node(start, end, cover)
        if end > root.start and start < root.end:
            new_root = root.add(start, end, cover)
            if new_root is None:
                return None
        else:
            new_root = root.copy()
        lres = rres = True
        if start < root.start:
            lres = self.insert(new_root.left, start, min(end, root.start))
            new_root.left = lres
        if end > root.end:
            rres = self.insert(new_root.right, max(root.end, start), end)
            new_root.right = rres
        return lres and rres and new_root
