from unittest import TestCase

from movie_rating import *

class TestMovieRating (TestCase):

    def test_thatICanAddOneMovie(self):
        self.movie_rating = MovieRating()
        self.movie_rating.addMovie("Avatar")
        self.assertEqual(["Avatar"], self.movie_rating.checkMovie())

    def test_thatICanAddManyMovies(self):
        self.movie_rating = MovieRating()
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addMovie("Bleach")
        self.movie_rating.addMovie("Naruto")
        self.assertEqual(["Avatar", "Bleach", "Naruto"], self.movie_rating.checkMovie())

