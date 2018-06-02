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


#Returns a description of the player formatted as:
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

    #Create two opposing indexes (exp and inexp) to assist
    #the following csv reader code to divvy the players into equally
    #experienced teams WHILE importing the data from the csv file.
    exp_index = 0
    inexp_index = len(team_lists) - 1

    #Reads in the CSV file and divvies players onto two teamsself.
    #Players with experienced are placed on teams in a 'positive'
    #direction (from Team 0 to Team x, where x is the number of teams - 1),
    #and inexperienced players are placed on teams in a 'negative'
    #direction (from Team x, where x is the number of teams - 1, to Team 0.)
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

    #Prints the team_lists to the console in a readable manner
    for team, team_list in team_lists.items():
        print("\n\n\n")
        print(team)
        for player in team_list:
            print(player_description(player))
