from flask import Flask, url_for, render_template
from riotwatcher import RiotWatcher
import json
import os
import match_extractors
m=match_extractors
w = RiotWatcher('88a2054a-5234-4303-880d-b5d7028f7ca0')
app = Flask(__name__)
#will need functions for:
#def build_champ_db that is indexable by  their id to avoid constantly querying the static db
#Constants
#team types
COMP_UNKNOWN = "unknown"
#standard team types 
#COMP_AP
#MID:AP carry or AP assassin
#BOT: ADC and support
COMP_AP = "ap"
#COMP_AD

#COMP_AP_SWAP
#COMP_AD_SWAP

#support variance
#COMP_SUP_NONE
#COMP_SUPDAMAGE --built 1+ dedicated damage items.
#COMP_
#champions = w.static_get_champion_list()


#player info
#lane position
# number shared with
# main/shared/no farm 
# damage type
# role [asssassin/bruiser/burst/carry/zerocs/tank/???]
# supporty [y/n]
# roamer [y/n]

@app.route('/hello/<name>')
def hello(name=None):
	if name != None:
		me = w.get_summoner(name)
		games = w.get_recent_games(me['id'])
		for game in games['games']:
			print w.static_get_champion(game['championId'])['name']
			print game['stats']['assists']
		print(me)
		return 'id '+ str(me['id']) +' level ' + str(me['summonerLevel'])
 
	else:
		return "no user input"
@app.route('/')
def index(): 
    with open('matches1.json') as json_file:
        matches = json.load(json_file, 'latin-1')
    process_seed_data(matches)



@app.route('/user/<username>')
def profile(username): pass
class champion_info:
    #needs to have:
    #Champion name
    #Champion role
    #Champion lane
    #Champion damage type
    #Other?
    champion = 'name'
    lane = 'mid/bot/top/jungle'
    damage = 'ap/ad/hybrid'
    role = 'damage/zero_cs/tank/bruiser(damage+tank)/dmg_zero_cs'#super reduced to start with



class game_info:
    #needs to have:
    #team that won
    #Per team:
    #"high level team comp"
    #type of each champion?
    #to start super high level
    win = -1
    blue_comp = COMP_UNKNOWN
    red_comnp = COMP_UNKNOWN
    rank = "unknown"#rank will be some average of players rank in the game
def process_team(match, team):
    do='stuff'
def proccess_game(match, t1, t2):
    do='stuff'

#Processes all seed data.
def process_seed_data(matches):
    for match in matches['matches']:
        #for each match print each champion in team and
        t1 = []
        t2 = []
       # for participant in match['participants']:
       #     if participant['teamId']== 100:
       #         t1.append(participant['championId'])
       #     else:
       #         t2.append(participant['championId'])
        teams= m.get_teams(match) 
        t1=teams[0]
        t2=teams[1]
        print 'red team!'
        for i in t1:
            print i
            print w.static_get_champion(i)['name']
        print 'blue team!'
        for i in t2:
            print i
            print w.static_get_champion(i)['name']




if __name__ == '__main__':
        #Figure out how to json
	app.run(debug=True)
