import csv

TEAMS = ['Sharks', 'Dragons', 'Raptors']

# Constants for CSV File Headings
NAME = 'Name'
EXPERIENCE = 'Soccer Experience'
GUARDIANS = 'Guardian Name(s)'
HEIGHT = 'Height (inches)'

def has_experience(player):
    if player[EXPERIENCE] == 'YES': return True
    else: return False

def print_player(player):
    name = player[NAME]
    experience = player[EXPERIENCE]
    guardians = player[GUARDIANS]
    print("{}, {}, {}".format(name, experience, guardians))


if __name__ == "__main__":
    experienced_players = list()
    inexperienced_players = list()

    with open('soccer_players.csv') as csvfile:
        players_reader = csv.DictReader(csvfile)
        for player in players_reader:
            if has_experience(player):
                experienced_players.append(player)
            else:
                inexperienced_players.append(player)

    print("\n** EXPERIENCED PLAYERS **")
    for player in experienced_players:
        print_player(player)
    print("\n\n**INEXPERIENCED PLAYERS **")
    for player in inexperienced_players:
        print_player(player)
