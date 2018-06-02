import csv

TEAMS = ['Sharks', 'Dragons', 'Raptors']

# Constants for CSV File Headings
NAME = 'Name'
EXPERIENCE = 'Soccer Experience'
GUARDIANS = 'Guardian Name(s)'
HEIGHT = 'Height (inches)'


#Determines if a player has soccer experienced_players
#RETURNS bool (True if experienced, False if not)
def has_experience(player):
    if player[EXPERIENCE] == 'YES': return True
    else: return False


#Prints a description of the player to console:
#Player name, experience level, and guardian names
def player_description(player):
    name = player[NAME]
    experience = player[EXPERIENCE]
    guardians = player[GUARDIANS]
    return "{}, {}, {}".format(name, experience, guardians)


#Main Function
if __name__ == "__main__":
    #Creates a dictionary for each of the three teams
    team_lists = dict()
    for team in TEAMS:
        team_lists[team] = list()

    exp_index = 0
    inexp_index = len(team_lists) - 1

    #Reads in the CSV file and divvies players into two groups:
    #experienced_players and inexperienced_players
    with open('soccer_players.csv') as csvfile:
        players_reader = csv.DictReader(csvfile)
        for player in players_reader:
            if has_experience(player):
                team_lists[TEAMS[exp_index]].append(player)
                if exp_index == len(team_lists) - 1 : exp_index = 0
                else: exp_index += 1
            else:
                team_lists[TEAMS[inexp_index]].append(player)
                if inexp_index == 0 : inexp_index = len(team_lists) - 1
                else: inexp_index -= 1

    for team, team_list in team_lists.items():
        print(team)
        for player in team_list:
            print(player_description(player))
        print("\n\n\n")
