from flask import Flask, url_for, render_template
from riotwatcher import RiotWatcher
import json
import os
w = RiotWatcher('88a2054a-5234-4303-880d-b5d7028f7ca0')
app = Flask(__name__)
#champions = w.static_get_champion_list()
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
    process_seed_data()



@app.route('/user/<username>')
def profile(username): pass

#Processes all seed data.
def process_seed_data():
    with open('matches1.json') as json_file:
        matches = json.load(json_file, 'latin-1')
    for match in matches['matches']:
        #for each match print each champion in team and
        t1 = []
        t2 = []
        for participant in match['participants']:
            if participant['teamId']== 100:
                t1.append(participant['championId'])
            else:
                t2.append(participant['championId'])
        print 'red team!'
        for i in t1:
            print i
            print w.static_get_champion(i)['name']
        for i in t2:
            print i
            print w.static_get_champion(i)['name']




if __name__ == '__main__':
        #Figure out how to json
	app.run(debug=True)
