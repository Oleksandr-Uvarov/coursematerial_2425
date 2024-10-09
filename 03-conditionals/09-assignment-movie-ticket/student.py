# write your code here
def movie_ticket(duration, imax, student, ticket_count):
    cost = 0

    if duration < 90:
        cost = 10
    elif 90 <= duration < 120:
        cost = 11
    elif 120 <= duration < 150:
        cost = 12
    else:
        cost = 15

    if imax:
        cost *= 1.2

    if student:
        cost -= 3

    return cost * ticket_count