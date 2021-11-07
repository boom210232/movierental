import csv
from movie import Movie
from rental import *


class MovieCatalog:
    def __init__(self):
        self.file = open("movies.csv", "r")
        self.movies_list = []
        for line in csv.reader(self.file):
            if line[0].startswith("#"):
                continue
            movie = Movie(line[1], int(line[2]), line[3].split("|"))
            self.movies_list.append(movie)

    def get_movie(self, title: str) -> Movie:
        wanted = filter(lambda movie: movie.get_title() == title, self.movies_list)
        return list(wanted)[0]


if __name__ == "__main__":
    catalog = MovieCatalog()
    # hacksaw = movie_catalog.get_movie("Hacksaw Ridge")
    # print(hacksaw, hacksaw.get_year(), hacksaw.get_genre())
    # print(catalog.movies_list)
    movie = catalog.get_movie("Frozen")
    rental = Rental(movie, 100)
    assert rental.price_code == PriceCode.childrens, f"Yae leaw! Wrong price code. Mun kee {rental.price_code.name}"
