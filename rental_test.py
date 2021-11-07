import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie
from movie_catalog_info import MovieCatalog


class RentalTest(unittest.TestCase):
    catalog = MovieCatalog()

    def setUp(self):
        self.new_movie = self.catalog.get_movie("James vs Kotlin")
        self.regular_movie = self.catalog.get_movie("The Martian")
        self.childrens_movie = self.catalog.get_movie("Mulan")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Amagami", 2010, ["Romantic-comedy"])
        self.assertEqual("Amagami", m.get_title())
        rental = Rental(m, 100)
        self.assertEqual(PriceCode.normal, rental.price_code)

    def test_rental_price_for_new_movie(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_charge(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_charge(), 15.0)

    def test_rental_price_for_regular_movie(self):
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_charge(), 2)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_charge(), 6.5)

    def test_rental_price_for_children_movie(self):
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_charge(), 4.5)

    def test_rental_points(self):
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_point(), 1)
        rental = Rental(self.regular_movie, 999)
        self.assertEqual(rental.get_point(), 1)
        rental = Rental(self.new_movie, 36525)
        self.assertEqual(rental.get_point(), 36525)
