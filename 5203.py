class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        def translate(artifact):
            r1, c1, r2, c2 = artifact
            return [(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]
        mapping = {}
        for artifact in artifacts:
            cells = translate(artifact)
            for cell in cells:
                mapping[cell] = cells
        res = 0
        for cell in map(tuple, dig):
            if cell in mapping:
                mapping[cell].pop()
                if not mapping[cell]:
                    res += 1
        return res

