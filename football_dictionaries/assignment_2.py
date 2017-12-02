from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_position(squads_list):

    SQUADS_DATA = {}
    player_dict = players_as_dictionaries(squads_list)

    for player in player_dict:
        # create list of position if not exist
        if player['position'] not in SQUADS_DATA:
            SQUADS_DATA[player['position']] = []
            
        SQUADS_DATA[player['position']].append(player)
    return SQUADS_DATA
