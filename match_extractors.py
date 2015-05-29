def get_teams(match):
        #for each match print each champion in team and
        t1 = []
        t2 = []
        for participant in match['participants']:
            if participant['teamId']== 100:
                t1.append(participant['participantId'])
            else:
                t2.append(participant['participantId'])


        return (t1,t2)
