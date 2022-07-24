import heapq, collections

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = {}
        self.food_cuisine = {}
        self.cuisine_to_rating_food = collections.defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_cuisine[food] = cuisine
            self.changeRating(food, rating)
            


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.food_rating[food] = newRating
        heapq.heappush(self.cuisine_to_rating_food[cuisine], [-newRating, food])


    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_rating_food[cuisine]
        while self.food_rating[heap[0][1]] != -heap[0][0]:
            heapq.heappop(heap)
        return heap[0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

