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

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_point(self):
        # award renter points
        return self.movie.get_frequent_renter_point(self.days_rented)

    def get_charge(self):
        # compute self change
        return self.movie.price_code.price(self.days_rented)
