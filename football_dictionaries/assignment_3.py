from football_dictionaries.assignment_1 import players_as_dictionaries

def players_by_country_and_position(squads_list):

  SQUADS_DATA = {} 
  player_dict = players_as_dictionaries(squads_list)

  for player in player_dict:
    country = player['country']
    position = player['position']
    
    if country not in SQUADS_DATA:
      SQUADS_DATA[country] = {}

    if position not in SQUADS_DATA[country]:
      SQUADS_DATA[country][position] = []
        
    SQUADS_DATA[country][position].append(player)
    
  return SQUADS_DATA
