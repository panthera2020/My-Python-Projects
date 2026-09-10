from unittest import TestCase

from movie_rating import *

class TestMovieRating (TestCase):
    def setUp(self):
        self.movie_rating = MovieRating()


    def test_thatICanAddOneMovie(self):
        self.movie_rating.addMovie("Avatar")
        self.assertEqual(["Avatar"], self.movie_rating.checkMovie())

    def test_thatICanAddThreeMovies(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addMovie("Bleach")
        self.movie_rating.addMovie("Naruto")
        self.assertEqual(["Avatar", "Bleach", "Naruto"], self.movie_rating.checkMovie())

    def test_thatWhenIAddMovieTimeIsSaved(self):
        self.movie_rating.addMovie("Avatar")
        self.assertEqual( 1,len(self.movie_rating.checkTime()))

    def test_thatWhenIAddThreeMovieTimeIsSaved(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addMovie("Bleach")
        self.movie_rating.addMovie("Naruto")
        self.assertEqual(3,len(self.movie_rating.checkTime()))

    def test_thatICanAddRatingToMovie(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addRating("Avatar",5)
        self.assertEqual(5,self.movie_rating.checkRating("Avatar"))

    def test_thatWhenIAddMovie_andIAddThreeRating_iGetTheAverageRating(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addRating("Avatar", 5)
        self.movie_rating.addRating("Avatar", 4)
        self.movie_rating.addRating("Avatar", 3)
        self.assertEqual(4, self.movie_rating.checkRating("Avatar"))

    def test_thatWhenIAddTwoMovies_andIAddVariousRating_IgetRatingsForTheTwoMovies(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addMovie("Bleach")
        self.movie_rating.addRating("Avatar", 5)
        self.movie_rating.addRating("Avatar", 4)
        self.movie_rating.addRating("Avatar", 3)
        self.movie_rating.addRating("Bleach", 2)
        self.movie_rating.addRating("Bleach", 4)
        self.assertEqual([4,3], self.movie_rating.checkRatings())

    def test_thatWhenIAddRatingOfLessThanOne_ZeroRatingIsAdded(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addRating("Avatar", -1)
        self.assertEqual(0, self.movie_rating.checkRating("Avatar"))

    def test_thatWhenIAddRatingOfGreaterThan5_ZeroRatingIsAdded(self):
        self.movie_rating.addMovie("Avatar")
        self.movie_rating.addRating("Avatar", 7)
        self.assertEqual(0, self.movie_rating.checkRating("Avatar"))

    def test_thatWhatMovieIsAdded_ifMovieIsAvailable_returnTrue(self):
        self.movie_rating.addMovie("Avatar")
        self.assertTrue(self.movie_rating.isMovieAvailable("Avatar"))