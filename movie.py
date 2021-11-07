# from pricecode import PriceCode
import logging
from rental import PriceCode


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).

    def __init__(self, title, price_code, year, genre=list):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = genre
        if price_code not in PriceCode:
            log = logging.getLogger()
            log.error(f"Movie {self.__title} has unrecognized priceCode {price_code}")
            raise ValueError(f"Movie {self.__title} has unrecognized priceCode {price_code}")
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.__title

    def get_frequent_renter_point(self, days):
        return self.price_code.point(days)

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def __str__(self):
        return self.__title
