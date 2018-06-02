import csv

#Constant that supplies the names of the teams
TEAMS = ['Sharks', 'Dragons', 'Raptors']
FILENAME = 'teams.txt'


#Constants for CSV File Headings
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


#Create output file (truncating any previous versions)
#and output each team's data to file
def output_team_lists(team_lists):
    with open(FILENAME, 'w') as file:
        for team, team_list in team_lists.items():
            file.write(team + ":\n")
            for player in team_list:
                file.write(player_description(player) + "\n")
            file.write("\n")


def create_welcome_letter_for(player, team):
    name = player[NAME]
    guardians = player[GUARDIANS]
    letter_filename = name.lower().replace(' ', '_') + '.txt'
    print(letter_filename)



#Main Function
if __name__ == "__main__":
    #Creates a dictionary<string: team name, list: player_dictionaries>
    #for each of the teams.
    team_lists = dict()
    for team in TEAMS:
        team_lists[team] = list()

    #Create two opposing indexes (exp and inexp) to assist
    #the following csv reader code to divvy the players into equally
    #experienced teams WHILE importing the data from the csv file.
    exp_index = 0
    inexp_index = len(team_lists) - 1

    #Reads in the CSV file and divvies players into teams.
    #Players with experienced are placed on teams in a 'positive'
    #direction (from Team 0 to Team x, where x is the number of teams - 1),
    #and inexperienced players are placed on teams in a 'negative'
    #direction (from Team x, where x is the number of teams - 1, to Team 0.)
    max_team_index = len(team_lists) - 1
    with open('soccer_players.csv') as csvfile:
        players_reader = csv.DictReader(csvfile)
        for player in players_reader:
            if has_experience(player):
                team_name = TEAMS[exp_index]
                team_lists[team_name].append(player)
                if exp_index == max_team_index : exp_index = 0
                else: exp_index += 1
            else:
                team_name = TEAMS[inexp_index]
                team_lists[team_name].append(player)
                if inexp_index == 0 : inexp_index = max_team_index
                else: inexp_index -= 1
            create_welcome_letter_for(player, team_name)

    #Prints the team_lists to the console in a readable manner
    output_team_lists(team_lists)
