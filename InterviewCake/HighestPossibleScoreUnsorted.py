def sort_scores(unsorted_scores, highest_possible_score):
    # list of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score + 1)

    # populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # populate the final sorted list
    sorted_scores = []

    # for each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # for the number of times the item occurs
        for time in range(count):
            # add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores


print sort_scores([4, 2, 4, 5, 7, 3, 5, 7], 10)
