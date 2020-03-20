#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Ybrayym Abamov"

import cProfile
import pstats
# import functools >>>> # didn't what to do with it
# nor was it needed for this asignment
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).strip_dirs().sort_stats('cumulative')
        ps.print_stats()  # defaults to top 10
        return retval
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


# def is_duplicate(title, movies):
#     """returns True if title is within movies list"""
#     for movie in movies:
#         if movie.lower() == title.lower():
#             return True
#     return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [m_one for m_one, m_two in zip(
        movies[:-1], movies[1:]) if m_one == m_two]
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    num_rep1 = 7
    num_rep2 = 3
    result = t.repeat(repeat=num_rep1, number=num_rep2)
    best_time = min(result) / float(num_rep2)
    print('Best time across {} repeats of {} runs per repeat in {} sec'.format(
        num_rep1, num_rep2, best_time))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
