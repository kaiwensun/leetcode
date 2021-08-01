class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        edge = 0
        apples = 0
        while apples < neededApples:
            edge += 1
            apples += edge * edge * 12
        return edge * 8

