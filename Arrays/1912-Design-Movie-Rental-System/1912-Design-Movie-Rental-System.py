from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = SortedList()
        self.rented = SortedList()
        self.price_map = {} 
        self.movie_map = defaultdict(SortedList)

        for shop, movie, price in entries:
            self.available.add((price, shop, movie))
            self.movie_map[movie].add((price, shop))
            self.price_map[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        return [shop for price, shop in self.movie_map[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.available.remove((price, shop, movie))
        self.movie_map[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available.add((price, shop, movie))
        self.movie_map[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
