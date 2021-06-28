from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie2priceshops = defaultdict(SortedList)
        self.shopmovie2price = {}
        self.rented_BST = SortedList()  # [(price, shop, movie)]
        for shop, movie, price in entries:
            self.movie2priceshops[movie].add((price, shop))
            self.shopmovie2price[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        return [item[1] for item in self.movie2priceshops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shopmovie2price[(shop, movie)]
        self.movie2priceshops[movie].remove((price, shop))
        self.rented_BST.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shopmovie2price[(shop, movie)]
        self.movie2priceshops[movie].add((price, shop))
        self.rented_BST.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [item[1:] for item in self.rented_BST[:5]]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

