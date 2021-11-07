# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental, PriceCode
from customer import Customer
from movie_catalog_info import MovieCatalog


# from pricecode import PriceCode

def make_movies():
    movie_fetch = MovieCatalog()
    movies = [
        # Movie("The Irishman", PriceCode.new_release,2000),
        # Movie("CitizenFour", PriceCode.normal,1990),
        # Movie("Frozen", PriceCode.childrens,1990),
        # Movie("El Camino", PriceCode.new_release,1990),
        # Movie("Particle Fever", PriceCode.normal,1990)
        movie_fetch.get_movie("Deadpool")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
