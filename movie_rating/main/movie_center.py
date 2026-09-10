from movie_rating import MovieRating

movie = MovieRating()

welcomeMessage = """
================================
    Welcome to Raters
================================
TO ADD MOVIE         -> PRESS 1
TO ADD RATING        -> PRESS 2
TO VIEW RATING       -> PRESS 3
================================
TO EXIT              -> PRESS 0
================================
"""
userMenuChoice = -1
while userMenuChoice != 0:
    print(welcomeMessage)
    userChoice = input()
    if userChoice == "1":
        userMovie = input("Enter Movie Name: ")
        movie.addMovie(userMovie)
    elif userChoice == "2":
        userMovieToRate = input("Enter Movie you want to rate: ")
        userMovieRating = input("Enter Rating for Movie: ")
        if movie.isMovieAvailable(userMovieToRate):
            movie.addRating(userMovieToRate, int(userMovieRating))
        else:
            print("Movie not available")
    elif userChoice == "3":
        moviesAvailable = movie.checkMovie()
        movieRated = movie.checkRatings()
        timeMovieWasAddded = movie.checkTime()
        if len(moviesAvailable) == 0:
            print("No Movies Available")
        else:
            print("Average Rating")
            print("S/N", "  average rating  ", "   time movie was  added   ")
            for _ in range(len(moviesAvailable)):
                print( _ + 1, " ", moviesAvailable[_], " ", movieRated[_], timeMovieWasAddded[_] )
    elif userChoice == "0":
        userMenuChoice = 0
    else:
        print("Invalid Choice")