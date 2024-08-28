# Sample Dataset
movies = [
    {"name": "The Shawshank Redemption", "year": 1994, "genre": "Drama", "rating": 9.3, "director": "Frank Darabont"},
    {"name": "The Godfather", "year": 1972, "genre": "Crime", "rating": 9.2, "director": "Francis Ford Coppola"},
    {"name": "The Dark Knight", "year": 2008, "genre": "Action", "rating": 9.0, "director": "Christopher Nolan"},
    {"name": "12 Angry Men", "year": 1957, "genre": "Drama", "rating": 8.9, "director": "Sidney Lumet"},
    {"name": "Schindler's List", "year": 1993, "genre": "Biography", "rating": 8.9, "director": "Steven Spielberg"},
    {"name": "Pulp Fiction", "year": 1994, "genre": "Crime", "rating": 8.9, "director": "Quentin Tarantino"},
    {"name": "Inception", "year": 2010, "genre": "Sci-Fi", "rating": 8.8, "director": "Christopher Nolan"},
    {"name": "Fight Club", "year": 1999, "genre": "Drama", "rating": 8.8, "director": "David Fincher"},
    {"name": "Forrest Gump", "year": 1994, "genre": "Drama", "rating": 8.8, "director": "Robert Zemeckis"},
    {"name": "The Matrix", "year": 1999, "genre": "Sci-Fi", "rating": 8.7, "director": "The Wachowskis"},
    {"name": "Goodfellas", "year": 1990, "genre": "Crime", "rating": 8.7, "director": "Martin Scorsese"},
    {"name": "The Empire Strikes Back", "year": 1980, "genre": "Sci-Fi", "rating": 8.7, "director": "Irvin Kershner"},
    {"name": "One Flew Over the Cuckoo's Nest", "year": 1975, "genre": "Drama", "rating": 8.7, "director": "Miloš Forman"},
    {"name": "Parasite", "year": 2019, "genre": "Thriller", "rating": 8.6, "director": "Bong Joon Ho"},
    {"name": "Interstellar", "year": 2014, "genre": "Sci-Fi", "rating": 8.6, "director": "Christopher Nolan"},
    {"name": "City of God", "year": 2002, "genre": "Crime", "rating": 8.6, "director": "Fernando Meirelles"},
    {"name": "Spirited Away", "year": 2001, "genre": "Animation", "rating": 8.6, "director": "Hayao Miyazaki"},
    {"name": "Saving Private Ryan", "year": 1998, "genre": "War", "rating": 8.6, "director": "Steven Spielberg"},
    {"name": "The Green Mile", "year": 1999, "genre": "Drama", "rating": 8.6, "director": "Frank Darabont"},
    {"name": "The Usual Suspects", "year": 1995, "genre": "Mystery", "rating": 8.5, "director": "Bryan Singer"},
    {"name": "The Silence of the Lambs", "year": 1991, "genre": "Thriller", "rating": 8.6, "director": "Jonathan Demme"},
    {"name": "Se7en", "year": 1995, "genre": "Thriller", "rating": 8.6, "director": "David Fincher"},
    {"name": "It's a Wonderful Life", "year": 1946, "genre": "Drama", "rating": 8.6, "director": "Frank Capra"},
    {"name": "Life Is Beautiful", "year": 1997, "genre": "Comedy", "rating": 8.6, "director": "Roberto Benigni"},
    {"name": "The Departed", "year": 2006, "genre": "Crime", "rating": 8.5, "director": "Martin Scorsese"},
    {"name": "Gladiator", "year": 2000, "genre": "Action", "rating": 8.5, "director": "Ridley Scott"},
    {"name": "The Prestige", "year": 2006, "genre": "Drama", "rating": 8.5, "director": "Christopher Nolan"},
    {"name": "The Lion King", "year": 1994, "genre": "Animation", "rating": 8.5, "director": "Roger Allers"},
    {"name": "Apocalypse Now", "year": 1979, "genre": "War", "rating": 8.4, "director": "Francis Ford Coppola"},
    {"name": "The Shining", "year": 1980, "genre": "Horror", "rating": 8.4, "director": "Stanley Kubrick"},
    {"name": "Whiplash", "year": 2014, "genre": "Drama", "rating": 8.5, "director": "Damien Chazelle"},
    {"name": "The Great Dictator", "year": 1940, "genre": "Comedy", "rating": 8.4, "director": "Charlie Chaplin"},
    {"name": "The Wolf of Wall Street", "year": 2013, "genre": "Biography", "rating": 8.2, "director": "Martin Scorsese"},
    {"name": "Django Unchained", "year": 2012, "genre": "Western", "rating": 8.4, "director": "Quentin Tarantino"},
    {"name": "Mad Max: Fury Road", "year": 2015, "genre": "Action", "rating": 8.1, "director": "George Miller"},
    {"name": "Braveheart", "year": 1995, "genre": "Biography", "rating": 8.3, "director": "Mel Gibson"},
    {"name": "Alien", "year": 1979, "genre": "Sci-Fi", "rating": 8.4, "director": "Ridley Scott"},
    {"name": "Toy Story", "year": 1995, "genre": "Animation", "rating": 8.3, "director": "John Lasseter"},
    {"name": "Memento", "year": 2000, "genre": "Mystery", "rating": 8.4, "director": "Christopher Nolan"},
    {"name": "The Truman Show", "year": 1998, "genre": "Comedy", "rating": 8.1, "director": "Peter Weir"},
    {"name": "Jaws", "year": 1975, "genre": "Thriller", "rating": 8.0, "director": "Steven Spielberg"},
    {"name": "Raging Bull", "year": 1980, "genre": "Biography", "rating": 8.2, "director": "Martin Scorsese"},
    {"name": "Casablanca", "year": 1942, "genre": "Romance", "rating": 8.5, "director": "Michael Curtiz"},
    {"name": "Raiders of the Lost Ark", "year": 1981, "genre": "Adventure", "rating": 8.4, "director": "Steven Spielberg"},
    {"name": "Amélie", "year": 2001, "genre": "Comedy", "rating": 8.3, "director": "Jean-Pierre Jeunet"},
    {"name": "A Beautiful Mind", "year": 2001, "genre": "Biography", "rating": 8.2, "director": "Ron Howard"},
    {"name": "The Sixth Sense", "year": 1999, "genre": "Mystery", "rating": 8.1, "director": "M. Night Shyamalan"},
    {"name": "WALL·E", "year": 2008, "genre": "Animation", "rating": 8.4, "director": "Andrew Stanton"},
]
# Functions
def print_first_n_movies(movies, n):
    print(movies[:n])

def get_total_movies(movies):
    print(f"Total: {len(movies)}")
    return len(movies)

def get_highest_rated_movie(movies):
    hr_movie = max(movies, key=lambda m: m["rating"])
    print(f"Highest: {hr_movie['name']} ({hr_movie['rating']})")
    return hr_movie

def calculate_average_rating(movies):
    avg_rating = sum(m["rating"] for m in movies) / len(movies)
    print(f"Average Rating: {avg_rating:.2f}")
    return avg_rating

def get_pre_2000_movies(movies):
    pre_2000 = [m["name"] for m in movies if m["year"] < 2000]
    print("Before 2000:", ", ".join(pre_2000))
    return pre_2000

def get_high_rated_movies(movies, threshold=8.0):
    high_rated = [m["name"] for m in movies if m["rating"] > threshold]
    print(f"Above {threshold}:", ", ".join(high_rated))
    return high_rated

def get_genre_count(movies):
    genre_count = {}
    for m in movies:
        genre_count[m["genre"]] = genre_count.get(m["genre"], 0) + 1
    print("Genre Counts:", genre_count)
    return genre_count

def get_newest_and_oldest_movies(movies):
    newest = max(movies, key=lambda m: m["year"])
    oldest = min(movies, key=lambda m: m["year"])
    print(f"Newest: {newest['name']} ({newest['year']}), Oldest: {oldest['name']} ({oldest['year']})")
    return newest, oldest

# New Modules

def filter_movies_by_genre(movies, genre):
    filtered_movies = [m["name"] for m in movies if m["genre"].lower() == genre.lower()]
    print(f"Movies in genre '{genre}':", ", ".join(filtered_movies) if filtered_movies else "None found")
    return filtered_movies

def filter_movies_by_year(movies, year):
    filtered_movies = [m["name"] for m in movies if m["year"] == year]
    print(f"Movies released in {year}:", ", ".join(filtered_movies) if filtered_movies else "None found")
    return filtered_movies

def count_movies_by_director(movies):
    director_count = {}
    for m in movies:
        director_count[m["director"]] = director_count.get(m["director"], 0) + 1
    print("Movies by Director:", director_count)
    return director_count

# Main Program
def main():
    functions = {
        "1": ("Print first n movies", print_first_n_movies),
        "2": ("Get total number of movies", get_total_movies),
        "3": ("Get highest-rated movie", get_highest_rated_movie),
        "4": ("Calculate average rating", calculate_average_rating),
        "5": ("Get movies before 2000", get_pre_2000_movies),
        "6": ("Get movies above rating 8.0", get_high_rated_movies),
        "7": ("Get genre count", get_genre_count),
        "8": ("Get newest and oldest movies", get_newest_and_oldest_movies),
        "9": ("Filter movies by genre", filter_movies_by_genre),
        "10": ("Filter movies by year", filter_movies_by_year),
        "11": ("Count movies by director", count_movies_by_director),
    }
    
    while True:
        print("\nAvailable functions:")
        for k, v in functions.items():
            print(f"{k}: {v[0]}")
        choice = input("Choose a function or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        if choice in functions:
            if choice == "1":
                functions[choice][1](movies, int(input("Enter number: ")))
            elif choice == "6":
                functions[choice][1](movies, float(input("Enter threshold (default 8.0): ") or 8.0))
            elif choice == "9":
                functions[choice][1](movies, input("Enter genre: "))
            elif choice == "10":
                functions[choice][1](movies, int(input("Enter year: ")))
            else:
                functions[choice][1](movies)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
