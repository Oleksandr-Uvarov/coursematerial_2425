# write your code here
def election_winner(votes):
    if len(votes) == 0:
        return None
    
    max_count = 0
    max_votes_name = ""
    
    for vote in votes:
        count = 0
        name = vote
        for vote_2 in votes:
            if vote == vote_2:
                count += 1
        if count > max_count:
            max_count = count
            max_votes_name = name
    return max_votes_name





print(election_winner(("Mark","Mark","Mark","John", "Elisabreh")))