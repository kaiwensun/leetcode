class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            j = len(row) - 1
            for i in range(len(row) - 1, -1, -1):
                if row[i] == "#":
                    row[i] = "."
                    while row[j] != ".":
                        j -= 1
                    row[j] = "#"
                elif row[i] == "*":
                    j = i
        return list(map(list, map(reversed, zip(*box))))

