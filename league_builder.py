import csv

TEAMS = ['Sharks', 'Dragons', 'Raptors']

# Constants for CSV File Headings
NAME = 'Name'
EXPERIENCE = 'Soccer Experience'
GUARDIANS = 'Guardian Name(s)'
HEIGHT = 'Height (inches)'
TEAM = 'Team'


#Determines if a player has soccer experienced_players
#RETURNS bool (True if experienced, False if not)
def has_experience(player):
    if player[EXPERIENCE] == 'YES': return True
    else: return False


#Prints a description of the player to console:
#Player name, experience level, and guardian names
def print_player(player):
    name = player[NAME]
    experience = player[EXPERIENCE]
    guardians = player[GUARDIANS]
    print("{}, {}, {}".format(name, experience, guardians))


#Main Function
if __name__ == "__main__":
    #Creates a dictionary for each of the three teams
    team_lists = dict()
    for team in TEAMS:
        team_lists[team] = list()

    #Creates two lists to divvy the players into two groups
    experienced_players = list()
    inexperienced_players = list()

    #Reads in the CSV file and divvies players into two groups:
    #experienced_players and inexperienced_players
    with open('soccer_players.csv') as csvfile:
        players_reader = csv.DictReader(csvfile)
        for player in players_reader:
            if has_experience(player):
                experienced_players.append(player)
            else:
                inexperienced_players.append(player)

    #Calculates the number of experienced_players and
    #inexperienced_players per team
    num_teams = len(TEAMS)
    num_experienced_per_team = len(experienced_players) // num_teams
    num_inexperienced_per_team = len(inexperienced_players) // num_teams

    #Distributed experienced_players and inexperienced_players
    #into equal and balanced teams according to experience
    team_num = 0
    for team_name, team_members in team_lists.items():
        #Adds slice of experienced_players to each team
        e_start = team_num * num_experienced_per_team
        e_end = (team_num + 1) * num_experienced_per_team
        team_members.extend(experienced_players[e_start:e_end])

        #Adds slice of inexperienced_players to each team
        i_start = team_num * num_inexperienced_per_team
        i_end = (team_num + 1) * num_inexperienced_per_team
        team_members.extend(inexperienced_players[i_start:i_end])
        team_num += 1

        #TODO: Remove this console print & replace with write_out
        print(team_name + ":")
        for player in team_members:
            print_player(player)
