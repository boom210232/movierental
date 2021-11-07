from enum import Enum
from datetime import date


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic rental would have fields for the dates
    that the movie was rented and returned, from which the
    self period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = PriceCode.for_movie(self.movie)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_point(self):
        # award renter points
        return self.price_code.point(self.days_rented)
        # return self.get_frequent_renter_point(self.days_rented)

    def get_charge(self):
        # compute self change
        return self.price_code.price(self.days_rented)


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2.0 if days <= 2 else (1.5 * (days - 2)) + 2,
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 if days <= 3 else (1.5 * (days - 3)) + 1.5,
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def point(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        compute_point = self.value["frp"]  # the enum member's price formula
        return compute_point(days)

    @classmethod
    def for_movie(cls, movie):
        if movie.get_year() == date.today().year:
            return cls.new_release
        elif "Children" in movie.get_genre():

            return cls.childrens
        return cls.normal
