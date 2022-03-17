from collections import defaultdict, Counter

class DiscountSystem:

    def __init__(self):
        self.activities = {}
        self.users = defaultdict(Counter)  # {userId: {activity: count}}


    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        self.activities[actId] = {
            "actId": actId,
            "priceLimit": priceLimit,
            "discount": discount,
            "number": number,
            "userLimit": userLimit
        }

    def removeActivity(self, actId: int) -> None:
        self.activities.pop(actId, None)

    def consume(self, userId: int, cost: int) -> int:
        
        def search_activity():
            res = {
                "actId": float("inf"),
                "discount": 0,
                "number": float("inf"),
                "userLimit": float("inf")
            }
            for activity in self.activities.values():
                if cost < activity["priceLimit"] or activity["discount"] < res["discount"] or user[activity["actId"]] >= activity["userLimit"]:
                    continue
                if activity["discount"] > res["discount"]:
                    res = activity
                elif activity["actId"] < res["actId"]:
                    res = activity
            return res

        user = self.users[userId]
        activity = search_activity()
        user[activity["actId"]] += 1
        activity["number"] -= 1
        if activity["number"] == 0:
            self.removeActivity(activity["actId"])
        return cost - activity["discount"]

# Your DiscountSystem object will be instantiated and called as such:
# obj = DiscountSystem()
# obj.addActivity(actId,priceLimit,discount,number,userLimit)
# obj.removeActivity(actId)
# param_3 = obj.consume(userId,cost)

