from pricecode import PriceCode
import logging


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    movie_type = {
        REGULAR: PriceCode.normal,
        NEW_RELEASE: PriceCode.new_release,
        CHILDRENS: PriceCode.childrens
    }

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        if not price_code in Movie.movie_type:
            log = logging.getLogger()
            log.error(f"Movie {self.title} has unrecognized priceCode {price_code}")
            raise ValueError(f"Movie {self.title} has unrecognized priceCode {price_code}")
        self.price_code = Movie.movie_type[price_code]

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def get_frequent_renter_point(self, days):
        return self.price_code.point(days)

    def __str__(self):
        return self.title
