def election_winner(votes):
    if len(votes) == 0:
        return None
    
    candidates = set(votes)

    votes_calculated = {}
    count = 0

    for candidate in candidates:
        for vote in votes:
            if candidate == vote:
                count += 1
        votes_calculated[candidate] = count
        count = 0

    
    winner = ""
    max_votes = 0

    for candidate in votes_calculated.keys():
        if votes_calculated.get(candidate) > max_votes:
            max_votes = votes_calculated.get(candidate)
            winner = candidate

    print(votes_calculated)
    return winner



