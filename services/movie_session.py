from typing import Optional
from datetime import datetime

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:

    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )
    return movie_session


def get_movies_sessions(session_date: str = None) -> list:
    if session_date:
        try:
            date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
            sessions = MovieSession.objects.filter(show_time__date=date_obj)
        except ValueError:
            raise ValueError("session_date must be in 'YYYY-MM-DD' format")
    else:
        sessions = MovieSession.objects.all()

    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    try:
        return MovieSession.objects.get(id=movie_session_id)
    except MovieSession.DoesNotExist:
        return None


def update_movie_session(session_id: int,
                         show_time: Optional[datetime] = None,
                         movie_id: Optional[int] = None,
                         cinema_hall_id: Optional[int] = None)\
        -> Optional[MovieSession]:
    try:
        session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        return None

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> bool:
    try:
        session = MovieSession.objects.get(id=session_id)
        session.delete()
        return True
    except MovieSession.DoesNotExist:
        return False
