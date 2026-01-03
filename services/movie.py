from db.models import Movie


def get_movies(genres_ids: list = None,
               actors_ids: list = None) -> None:
    # genres_id = Genre.objects.all().values_list("id", flat=True)
    # actors_id = Actor.objects.all().values_list("id", flat=True)

    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__in=genres_ids,
                                    actors__in=actors_ids)
    elif genres_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    elif actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)
    else:
        return Movie.objects.all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> None:
    if genres_ids is None:
        genres_ids = []
    if actors_ids is None:
        actors_ids = []

    movie__d = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    movie__d.genres.set(genres_ids)
    movie__d.actors.set(actors_ids)

    return movie__d
