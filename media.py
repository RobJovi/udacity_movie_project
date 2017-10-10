# import webbrowser module in order to play movie trailer
import webbrowser


# Class for movies
class Movie():
    # class constructor
    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url):
        self.title = title
        self.synopsis = synopsis
        # self.box_art = box_art
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # method that plays movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
