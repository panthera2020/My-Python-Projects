from datetime import datetime

class MovieRating:
    def __init__(self):
        self.movies = []
        self.time = []
        self.ratings = []

    def addMovie(self, movie):
        self.movies.append(movie)
        self.ratings.append([0])
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time.append(time)

    def checkMovie(self):
        return self.movies

    def checkTime(self):
        return self.time

    def addRating(self, movie, rating):
        if(rating > 0 and rating <= 5):
            index = 0
            for _ in range(len(self.movies)):
                if self.movies[_] == movie: index = _
            self.ratings[index].append(rating)
        else:
            index = 0
            for _ in range(len(self.movies)):
                if self.movies[_] == movie: index = _
            self.ratings[index].append(0)


    def checkRating(self, movie):
        index = 0
        for _ in range(len(self.movies)):
            if self.movies[_] == movie: index = _

        rating = sum(self.ratings[index]) / len(self.ratings[index])
        return rating

    def checkRatings(self):
        ratings = []
        for _ in range(len(self.movies)): ratings.append(sum(self.ratings[_]) / len(self.ratings[_]))
        return ratings

    def isMovieAvailable(self, movie):
        isAvailable = False
        if movie in self.movies: isAvailable = True
        return isAvailable




