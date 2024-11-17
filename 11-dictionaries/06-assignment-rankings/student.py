def rankings(participants):
    ranks = {}
    for i in range(1, len(participants) + 1):
        ranks[participants[i-1]] = i

    return ranks