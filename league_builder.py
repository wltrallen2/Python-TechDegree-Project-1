import csv

################# CONSTANTS #################

#Constants that supplies the names of the teams and file names
TEAMS = ['Sharks', 'Dragons', 'Raptors']
FILENAME = 'teams.txt'
WELCOME_LTR_MASTER = 'welcome_letter_master.txt'

#Constants for CSV File Headings
NAME = 'Name'
EXPERIENCE = 'Soccer Experience'
GUARDIANS = 'Guardian Name(s)'
HEIGHT = 'Height (inches)'

#Constants from welcome_letter_master
STUDENT_NAME = 'STUDENT_NAME'
GUARDIAN_NAMES = 'GUARDIAN_NAMES'
TEAM_NAME = 'TEAM_NAME'

################# FUNCTIONS #################

#Determines if a player has soccer experience
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


#Creates and outputs personalized welcome letter for player
#when given the team and the letter_text using the constants:
#STUDENT_NAME, GUARDIAN_NAMES, TEAM_NAME
def create_welcome_letter_for(player, team, letter_text):
    name = player[NAME]
    guardians = player[GUARDIANS]
    letter_filename = name.lower().replace(' ', '_') + '.txt'

    letter_text = letter_text.replace(STUDENT_NAME, name)
    letter_text = letter_text.replace(GUARDIAN_NAMES, guardians)
    letter_text = letter_text.replace(TEAM_NAME, team)

    with open(letter_filename, 'w') as file:
        file.write(letter_text)


#Imports and returns the text from welcome_letter_master
#to be used to create welcome letters for each student
def import_welcome_letter_text():
    letter_text = ''
    with open(WELCOME_LTR_MASTER) as file:
        for line in file:
            letter_text += line
    return(letter_text)


################# __MAIN__ #################
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

    #Import template for welcome letter
    letter_text = import_welcome_letter_text()

    #Reads in the CSV file and divvies players into teams.
    #Players with experience are placed on teams in a 'positive'
    #direction (from Team 0 to Team x, where x is the number of teams - 1),
    #and inexperienced players are placed on teams in a 'negative'
    #direction (from Team x, where x is the number of teams - 1, to Team 0.)
    #
    #Also calls function to create customized welcome letter for each student.
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
            create_welcome_letter_for(player, team_name, letter_text)

    #Outputs team list to file (FILENAME from constants)
    output_team_lists(team_lists)
