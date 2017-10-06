# Udacity Movie Trailer project
Source code for a Movie Trailer website.

This project opens up a webpage with various movies and their trailers. Each movie will have their poster art and on click, the user will be able to see their youtube trailer.


Requirements
------------

In order to run this project you must have [Python](https://www.python.org/) installed on your system.

Run
---

In order to run the project, cd into project folder and run the command:


```python
python entertainment_center.py
```

Documentaion
------------

In order to add more movies to the webpage, open up the entertainment_center.py file and create or edit instance of the Movie class in the media.py and then add it to the movies list

For example to add new a movie, add the following to the entertainment_center.py file

```
movie_name = media.Movie('movie_name','movie_synopsis','movie_poster_url','movie_youtube_trailer_url')
```

and the then add the new movie instance to the movies list

```
movies = [movie_name]
```

Contributing
------------

The fresh_tomatoes.py file and code was provided [here](https://github.com/udacity/ud036_StarterCode)

