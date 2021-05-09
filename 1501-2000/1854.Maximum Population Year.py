class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for birth, death in logs:
            events.append((birth, True))
            events.append((death, False))
        events.sort()
        res = None
        max_pop = population = 0
        for year, is_birth in events:
            if is_birth:
                population += 1
                if population > max_pop:
                    max_pop = population
                    res = year
            else:
                population -= 1
        return res

