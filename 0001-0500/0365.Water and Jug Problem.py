import math

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return jug1Capacity + jug2Capacity >= targetCapacity and \
            (jug1Capacity * jug2Capacity != 0 or targetCapacity == 0 or jug1Capacity * jug2Capacity == targetCapacity) and \
            targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0


