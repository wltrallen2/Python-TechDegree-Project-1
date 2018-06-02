import csv

################# CONSTANTS #################

# Create constant that supply the names of the teams and files.
TEAMS = ['Sharks', 'Dragons', 'Raptors']
FILENAME = 'teams.txt'
WELCOME_LTR_MASTER = 'welcome_letter_master.txt'

# Create constants to represent CSV File Headings.
NAME = 'Name'
EXPERIENCE = 'Soccer Experience'
GUARDIANS = 'Guardian Name(s)'
HEIGHT = 'Height (inches)'

# Create constants to represent placeholders in the welcome_letter_master.
STUDENT_NAME = 'STUDENT_NAME'
GUARDIAN_NAMES = 'GUARDIAN_NAMES'
TEAM_NAME = 'TEAM_NAME'

################# FUNCTIONS #################

# has_experience determines if a player has soccer experience
# and returns True if he is experienced and False if not.
def has_experience(player):
    return player[EXPERIENCE] == 'YES'


# player_description returns a description of the player formatted as
# "Player_Name, Experience_Level, and Guardian_Names."
def player_description(player):
    name = player[NAME]
    experience = player[EXPERIENCE]
    guardians = player[GUARDIANS]
    return "{}, {}, {}".format(name, experience, guardians)


# output_team_lists creates the output file (truncating
# any previous versions) and outputs each team's data to file.
    with open(FILENAME, 'w') as file:
        for team, team_list in team_lists.items():
            file.write(team + ":\n")
            for player in team_list:
                file.write(player_description(player) + "\n")
            file.write("\n")


# create_welcome_letter_for creates and outputs personalized
# welcome letter for player when given the team and the
# letter_text.  The letter_text must use the correct placeholders:
# STUDENT_NAME, GUARDIAN_NAMES, TEAM_NAME.
def create_welcome_letter_for(player, team, letter_text):
    name = player[NAME]
    guardians = player[GUARDIANS]
    letter_filename = name.lower().replace(' ', '_') + '.txt'

    letter_text = letter_text.replace(STUDENT_NAME, name)
    letter_text = letter_text.replace(GUARDIAN_NAMES, guardians)
    letter_text = letter_text.replace(TEAM_NAME, team)

    with open(letter_filename, 'w') as file:
        file.write(letter_text)


# import_welcome_letter_text imports and returns the text
# from welcome_letter_master to be used to create welcome
# letters for each student.
def import_welcome_letter_text():
    letter_text = ''
    with open(WELCOME_LTR_MASTER) as file:
        for line in file:
            letter_text += line
    return(letter_text)


################# __MAIN__ #################
if __name__ == "__main__":
    # Create a dictionary with string keys (the team name) and
    # dictionary values (player data) for each of the teams.
    team_lists = dict()
    for team in TEAMS:
        team_lists[team] = list()

    # Create two opposing indices (exp and inexp) to assist
    # in divvying the players into equally experienced teams
    # WHILE importing the data from the csv file.
    exp_index = 0
    inexp_index = len(team_lists) - 1

    # Import template for welcome letter.
    letter_text = import_welcome_letter_text()

    # Read in the CSV file and divvy players into teams.
    # Players with experience are placed on teams in a 'positive'
    # direction (from Team 0 to Team x, where x is the number of teams - 1),
    # and inexperienced players are placed on teams in a 'negative'
    # direction (from Team x, where x is the number of teams - 1, to Team 0.)
    #
    # Also, call function to create customized welcome letter for each student.
    max_team_index = len(team_lists) - 1
    with open('soccer_players.csv') as csvfile:
        players_reader = csv.DictReader(csvfile)
        for player in players_reader:
            if has_experience(player):
                team_name = TEAMS[exp_index]
                team_lists[team_name].append(player)
                if exp_index == max_team_index:
                    exp_index = 0
                else:
                    exp_index += 1
            else:
                team_name = TEAMS[inexp_index]
                team_lists[team_name].append(player)
                if inexp_index == 0:
                    inexp_index = max_team_index
                else:
                    inexp_index -= 1
            create_welcome_letter_for(player, team_name, letter_text)

    # Output list of teams and players to file.
    output_team_lists(team_lists)
