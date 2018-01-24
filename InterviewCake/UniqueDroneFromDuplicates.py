def find_unique_delivery_id(delivery_ids):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id


print find_unique_delivery_id(
    [1, 2, 3, 4, 2, 3, 4, 1, 2, 4, 5, 5, 2, 4, 3, 2, 1, 6, 3, 2, 1, 4, 3, 4, 5, 5, 3, 2, 3, 4, 2, 3, 4, 2, 3, 4, 4, 3,
     2])
