from functools import lru_cache
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        @lru_cache(None)
        def dp(box_id):
            if box_id == len(boxes):
                return 0
            count = 0
            weight = 0
            this_batch_port = None
            trip = 1
            res = float("inf")
            for i in range(box_id, len(boxes)):
                box = boxes[i]
                count += 1
                weight += box[1]
                if this_batch_port != box[0]:
                    this_batch_port = box[0]
                    this_batch_start_id = i
                    trip += 1
                if count > maxBoxes or weight > maxWeight:
                    break
            else:
                i += 1
                this_batch_start_id = i
                trip += 1
            assert(box_id != i)
            if this_batch_start_id != box_id:
                res = trip - 1 + dp(this_batch_start_id)
            if this_batch_start_id != i:
                res = min(res, trip + dp(i))
            return res

        return dp(0)

