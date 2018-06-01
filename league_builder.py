import csv

TEAMS = ['Sharks', 'Dragons', 'Raptors']

# Constants for CSV File Headings
NAME = 'Name'
EXPERIENCE = 'Soccer Experience'
GUARDIANS = 'Guardian Name(s)'
HEIGHT = 'Height (inches)'
TEAM = 'Team'


def has_experience(player):
    if player[EXPERIENCE] == 'YES': return True
    else: return False


def assign_player_to_team(player, team):
    player[TEAM] = team


def split_players_from_list(players):
    team_num = 0
    for player in players:
        team = TEAMS[team_num]
        assign_player_to_team(player, team)
        if team_num == len(TEAMS): team_num == 0
        else: team_num += 1


def print_player(player):
    name = player[NAME]
    experience = player[EXPERIENCE]
    guardians = player[GUARDIANS]
    print("{}, {}, {}".format(name, experience, guardians))


if __name__ == "__main__":
    #Creates a dictionary for each of the three teams
    team_lists = dict()
    for team in TEAMS:
        team_lists[team] = list()

    #Creates two lists to divvy the players into two groups
    experienced_players = list()
    inexperienced_players = list()

    with open('soccer_players.csv') as csvfile:
        players_reader = csv.DictReader(csvfile)
        for player in players_reader:
            if has_experience(player):
                experienced_players.append(player)
            else:
                inexperienced_players.append(player)

    num_teams = len(TEAMS)
    num_experienced_per_team = len(experienced_players) // num_teams
    num_inexperienced_per_team = len(inexperienced_players) // num_teams

    team_num = 0
    for team_name, team_members in team_lists.items():
        e_start = team_num * num_experienced_per_team
        e_end = (team_num + 1) * num_experienced_per_team
        team_members.extend(experienced_players[e_start:e_end])

        i_start = team_num * num_inexperienced_per_team
        i_end = (team_num + 1) * num_inexperienced_per_team
        team_members.extend(inexperienced_players[i_start:i_end])
        team_num += 1

        print(team_name + ":")
        for player in team_members:
            print_player(player)
