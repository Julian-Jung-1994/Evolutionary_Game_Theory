def hawk_dove(matches):

    replication_dove = 0
    replication_hawk = 0

    for match in matches:
        if match == (0, 0):
            replication_dove += 8
            replication_dove += 8
        elif match == (0, 1) or match == (1, 0):
            replication_dove += 5
            replication_hawk += 10
        elif match == (1, 1):
            replication_hawk += 1
            replication_hawk += 1

    rate_dove = replication_dove / (replication_dove + replication_hawk)
    rate_hawk = 1 - rate_dove
    replications = [rate_dove, rate_hawk]

    return replications
