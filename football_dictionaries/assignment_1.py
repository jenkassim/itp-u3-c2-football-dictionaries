def players_as_dictionaries(squads_list):

    SQUADS_DATA = []

    for sList in squads_list:
        players = {}
        players['number'] = sList[0]
        players['position'] = sList[1]
        players['name'] = sList[2]
        players['date_of_birth'] = sList[3]
        players['caps'] = sList[4]
        players['club'] = sList[5]
        players['country'] = sList[6]
        players['club_country'] = sList[7]
        players['year'] = sList[8]

        SQUADS_DATA.append(players)

    return SQUADS_DATA
