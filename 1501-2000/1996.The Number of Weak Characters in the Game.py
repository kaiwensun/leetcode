class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_defense = float("-inf")
        res = 0
        for _, defense in sorted(properties, key=lambda prop: (-prop[0], prop[1])):
            res += defense < max_defense
            max_defense = max(max_defense, defense)
        return res

