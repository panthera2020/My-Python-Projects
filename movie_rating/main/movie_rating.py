class MovieRating:
    def __init__(self):
        self.movies = []

    def addMovie(self, movie):
        self.movies.append(movie)

    def checkMovie(self):
        return self.movies