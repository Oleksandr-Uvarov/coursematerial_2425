from math import ceil

def make_teams(participants, team_size):
    list_of_teams = []

    if team_size > len(participants):
        return participants
    elif len(participants) % team_size == 0:
        team = []
        for i in range (0, len(participants)):
            if len(team) < team_size:
                team.append(participants[i])
            else:
                list_of_teams.append(team)
                team = []
                team.append(participants[i])

        list_of_teams.append(team)

        return list_of_teams
    else:
        number_of_players_left = len(participants) % team_size
        list_of_players_left = participants[-number_of_players_left:]

        participants_to_add_first = participants[:len(participants)-number_of_players_left]
        team = []
        for i in range (0, len(participants_to_add_first)):
            if len(team) < team_size:
                team.append(participants_to_add_first[i])
            else:
                list_of_teams.append(team)
                team = []
                team.append(participants_to_add_first[i])

        list_of_teams.append(team)


        while len(list_of_players_left) != 0:
            # although this loop iterates over teams rather than players,
            # the while loop above makes sure that all players are added
            # even if there are more players left than teams
            for team in list_of_teams:
                if(len(list_of_players_left) != 0):
                    player = list_of_players_left.pop()
                    team.append(player)

        return list_of_teams





print(make_teams(['Annie', 'Ashley', 'Butcher', 'Frenchie', 'Hughie', 'John', 'Kimiko', 'Maeve'], 4))
print(make_teams(['Annie', 'Ashley', 'Butcher', 'Frenchie', 'Hughie', 'John', 'Kimiko', 'Maeve'], 3))
print(make_teams(['Annie', 'Ashley', 'Butcher', 'Frenchie', 'Hughie', 'John', 'Kimiko', 'Maeve', 'Marvin'], 4))

print(make_teams(["a","a","a","a","a","b","b","b","b","b","c","c","c","c","c","d","d","d","d","d","e","e","e","e",], 5))












lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[-3:])









        # # For example, there are 8 players, and team size is 6
        # # 2 are left; spread those players across the teams

        # # For example, there are 9 players, and team size is 6
        # # 3 are left; spread those players across the teams
        # # Team 1 gets two additional players; team 2 gets one additional player.


        # players_left = len(participants) % team_size

        # players_to_add = participants[:len(participants)-players_left]

        # list_of_players_left = participants[len(players_to_add)+1:]

        # team = []
        # for i in range (0, len(players_to_add)):
        #     if len(team) < team_size:
        #         team.append(players_to_add[i])
        #     else:
        #         list_of_teams.append(team)
        #         team = []
        #         team.append(players_to_add[i])

        # list_of_teams.append(team)


        # for i in range(0, len(list_of_players_left)):
        #     list_of_teams[i].append(list_of_teams[i])