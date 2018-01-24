def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False


print can_two_movies_fill_flight([2, 1, 2, 1, 12, 4, 5, 8, 76, 5, 9, 7, 54, 2, 1], 9)
