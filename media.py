import webbrowser


class Movie:
    """
    This class creates instance of movie that contains
    movie title.movie story line , poster image ,trailer of movie
    """
    def __init__(self,
                 movie_title,
                 movie_story_line,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
