from flask import Flask, request, render_template, redirect
from teams import team_list
import json

app= Flask(__name__)

@app.before_first_request
def make_db():
    #initialising DB
    teamfile= {'teams': []}
    for team in team_list:
        teamdict= {
            'id'        : team.id,
            'name'      : team.name,
            'boss'      : team.boss,
            'drivers'   : team.drivers,
            'car'       : team.car,
            'score'     : 0
        }
        teamfile['teams'].append(teamdict)

    with open('team_info.json','w') as outfile:
        json.dump(teamfile,outfile)


@app.route('/', methods= ['POST','GET'])
def index():
    if request.method=='POST':
        #loading json db
        json_file= open('team_info.json','r')
        data= json.load(json_file)
        
        #loading user submitted ranking ---- !!!! NEEDS TO BE VERIFIED !!!!
        rank= request.form['rank'].split(",")
        
        #defining scoring system
        scoring= [25,18,15,12,10,8,6,4,2,1]

        #calculating points accumulated
        for team in data['teams']:
            points= scoring[rank.index(str(team['id']))]
            team['score']+= points
        
        #sorting data
        data['teams']= sorted(data['teams'], key= lambda d: d['score'], reverse=True)

        #confirming points into database
        with open('team_info.json','w') as outfile:
            json.dump(data,outfile)

        return redirect('/rankings')
    else:
        #homepage
        return render_template('index.html',team_list= team_list)

@app.route('/rankings')
def ranks():
    json_file= open('team_info.json','r')
    data= json.load(json_file)
    return render_template('ranks.html', team_list= data['teams'])
    

if __name__ == '__main__':
    app.run(debug=True)