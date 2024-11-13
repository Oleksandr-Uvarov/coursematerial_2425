from collections import namedtuple
Movie = namedtuple("Movie", ["title", "runtime", "director", "actors"])


def actor_count(movie):
    return len(movie.actors)