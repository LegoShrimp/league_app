def get_teams(match):
        #for each match print each champion in team and
        t1 = []
        t2 = []
        for participant in match['participants']:
            if participant['teamId']== 100:
                t1.append(participant['championId'])
            else:
                t2.append(participant['championId'])


        return (t1,t2)
