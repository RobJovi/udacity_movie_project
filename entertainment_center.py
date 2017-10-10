# import dependencies
import media
import fresh_tomatoes

# create instances of movies using the Movie class
toy_story = media.Movie(
    "Toy Story", "A story of a young boy and his toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"  # NOQA
    )

matrix = media.Movie(
    "Matrix",
    "Neo (Keanu Reeves) believes that Morpheus (Laurence Fishburne)"
    ", an elusive figure considered to be the most dangerous man alive,"
    "can answer his question -- What is the Matrix?",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY1200_CR84,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=m8e-FF8MsqU"  # NOQA
    )

titanic = media.Movie(
    "Titanic",
    "Titanic is a 1997 American epic romance-disaster film directed,"
    "written, co-produced and co-edited by James Cameron",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0"  # NOQA
    )

star_wars_new_hope = media.Movie(
    "Star Wars: Episode IV - A New Hope",
    "Luke Skywalker joins forces with a Jedi Knight,"
    "a cocky pilot, a Wookiee, and two droids to save "
    "the galaxy from the Empire",
    "https://images-na.ssl-images-amazon.com/images/I/81ZktNhAEkL._SY355_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1g3_CFmnU7k"  # NOQA
    )

whip_lash = media.Movie(
    "Whiplash",
    "Andrew Neiman (Miles Teller) is an ambitious young jazz drummer,"
    "in pursuit of rising to the top of his elite music conservatory."
    "Terence Fletcher (J.K. Simmons), an instructor known for his terrifying"
    "teaching methods, discovers Andrew and transfers the aspiring drummer "
    "into the top jazz ensemble",
    "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=7d_jQycdQGo"  # NOQA
    )

spider_man_3 = media.Movie(
    "Spider-Man 3",
    "Peter Parker (Tobey Maguire) and M.J. (Kirsten Dunst) seem to "
    "finally be on the right track in their complicated relationship,"
    "but trouble looms for the superhero and his lover. ",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Spider-Man_3%2C_International_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SZ1VNktVdqQ"  # NOQA
    )

# add all objects into a list
movies = [
    toy_story,
    matrix,
    titanic,
    star_wars_new_hope,
    whip_lash,
    spider_man_3
    ]

# pass list of movies in order to open up webpage
fresh_tomatoes.open_movies_page(movies)
