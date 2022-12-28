from bs4 import BeautifulSoup
from IPython.display import HTML
import numpy as np
import re

def get_data(html):
    soup = BeautifulSoup(html)
    def team_names(name):
        namer = {"mumbai":'Mumbai Indians',
                 "mumbai indians":'Mumbai Indians',
                 "chennai":'Chennai Super Kings',
                 "chennai super kings":'Chennai Super Kings',
                 "hyderabad":'Sunrisers Hyderabad',
                 "sunrisers hyderabad":'Sunrisers Hyderabad',
                 "sunrisers":'Sunrisers Hyderabad',
                 "kolkata":'Kolkata Knight Riders',
                 "kolkata knight riders":'Kolkata Knight Riders',
                 "bangalore":'Royal Challengers Bangalore',
                 "royal challengers bangalore":'Royal Challengers Bangalore',
                 "royal":'Royal Challengers Bangalore',
                 "delhi":'Delhi Capitals',
                 "delhi capitals":'Delhi Capitals',
                 "kings":'Punjab Kings',
                 "punjab kings":'Punjab Kings',
                 "punjab":'Punjab Kings',
                 "gujarat":'Gujarat Titans',
                 "gujarat titans":'Gujarat Titans',
                 "rajasthan":'Rajasthan Royals',
                 "rajasthan royals":'Rajasthan Royals',
                 "lucknow":'Lucknow Super Giants',
                 "lucknow super giants":'Lucknow Super Giants',
                 "gt":'Gujarat Titans',
                 "lsg":'Lucknow Super Giants'
                 
                }

        return namer.get(name,"anon_team")
    
    def stadium_names(city):
        namer = {                 
                 "abu":'Sheikh Zayed Stadium',
                 "dubai":'Dubai International Cricket Stadium',
                 "sharjah":'Sharjah Cricket Stadium',
                 "chennai":'MA Chidambaram Stadium',
                 "kolkata":'Eden Gardens',
                 "mumbai":'Wankhede Stadium',
                 "jaipur":'Sawai Mansingh Stadium',
                 "delhi":'Arun Jaitley Stadium',
                 "bengaluru": 'M Chinnaswamy Stadium',
                 "hyderabad":'Rajiv Gandhi International Stadium',
                 "mohali":'Punjab Cricket Association IS Bindra Stadium',
                 "visakhapatnam":'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
                 "pune":'Maharashtra Cricket Association Stadium',
                 "ahmedabad":'Narendra Modi Stadium',
                 "raipur":'Shaheed Veer Narayan Singh International Stadium',
                 "ranchi":'JSCA International Stadium Complex',
                 "rajkot":'Saurashtra Cricket Association Stadium',
                 "kanpur":'Green Park',
                 "indore":'Holkar Cricket Stadium',
                 "dharamsala":'Himachal Pradesh Cricket Association Stadium',
                 "cuttack":'Barabati Stadium',
                 "nagpur":'Vidarbha Cricket Association Stadium',
                 "uppal":'Rajiv Gandhi International Stadium',
                 "jamtha":'Vidarbha Cricket Association Stadium'
        }
        
        return namer.get(city,'anon_stadium');
        

    def won_toss(team):
        if team_names(team)==team2:
            return 1
        else: 
            return 0

    def fours_count():
        fours_list = []
        for i in range(5,100,4):
            if soup.findAll('div',class_="cb-col cb-col-8 text-right")[i].get_text() == 'M':
                break
            fours_list.append(int(soup.findAll('div',class_="cb-col cb-col-8 text-right")[i].get_text()))
        return fours_list

    def sixes_count():
        sixes_list = []
        for i in range(6,100,4):
            if soup.findAll('div',class_="cb-col cb-col-8 text-right")[i].get_text() == 'NB':
                break
            sixes_list.append(int(soup.findAll('div',class_="cb-col cb-col-8 text-right")[i].get_text()))
        return sixes_list

    team_who_won_toss = soup.findAll('div',class_ = "cb-col cb-col-73")[2].get_text().strip().split(' ')[0].lower()
    team_who_won_toss = team_names(team_who_won_toss)
    toss_dec = soup.findAll('div',class_ = "cb-col cb-col-73")[2].get_text().strip().split(' ')[-1].lower()
    team1 = team_names(soup.findAll('h1',class_ ="cb-nav-hdr cb-font-18 line-ht24" )[0].get_text().split(',')[0].split(' vs ')[0].lower())
    team2 = team_names(soup.findAll('h1',class_ ="cb-nav-hdr cb-font-18 line-ht24" )[0].get_text().split(',')[0].split(' vs ')[1].lower())
    
    
    team_1 = team1 if ((team_who_won_toss == team1) & (toss_dec == 'bat')) or ((team_who_won_toss == team2) & (toss_dec == 'bowl')) else team2
    team_2 = team2 if team_1 != team2 else team1
    bleh = soup.findAll('div',"cb-col cb-col-100 cb-scrd-hdr-rw")[0].get_text().strip().split(' ')[0].lower()
    inning = 1 if team_names(bleh)==team_1 else 2

    x = soup.findAll('div',class_ ="cb-col-32 cb-col" )[1].get_text()
    wickets_over_balls = re.findall(r"\b\d+\b",x)
    city = soup.findAll('div',class_ ="cb-col cb-col-73" )[4].get_text().strip().split(',')[1].strip().lower()
    
    

    current_score = int(soup.findAll('div',class_ ="cb-col cb-col-8 text-bold text-black text-right" )[0].get_text())
    venue = stadium_names(city)
    
    team1 = team_1
    team2 = team_2      
    team1_sixes = sum(sixes_count())
    team1_fours = sum(fours_count())
    try:
        current_over = 19 if int(wickets_over_balls[1]) == 20 else int(wickets_over_balls[1])
        current_ball_of_over = 6 if int(wickets_over_balls[1]) == 20 else int(wickets_over_balls[2])
    except IndexError:
        current_over = int(wickets_over_balls[1])-1
        current_ball_of_over = 6
    total_extra_runs = int(soup.findAll('div',class_ ="cb-col cb-col-8 text-bold cb-text-black text-right" )[0].get_text())
    wicket_loss = int(wickets_over_balls[0])
    balls_left = 120 - (current_over*6 + current_ball_of_over)
    over_left = 0 if (current_over == 19 and current_ball_of_over == 6) else 19 - current_over
    current_run_rate = current_score/current_over
    projected_score = int(current_score + (current_run_rate*(20-(current_over+1))))
    team2_won_toss = won_toss(team_who_won_toss)
    
    if inning == 2:
        team1_score = int(soup.findAll('div',class_ ="cb-col cb-col-8 text-bold text-black text-right" )[1].get_text()) + 1
        team1_extra_runs = int(soup.findAll('div',class_ ="cb-col cb-col-8 text-bold cb-text-black text-right" )[1].get_text())
        y = soup.findAll('div',class_ ="cb-col-32 cb-col" )[3].get_text()
        wickets_over_balls_2 = re.findall(r"\b\d+\b",y) 
        team1_wickets = int(wickets_over_balls_2[0])
        over_playedBy_team1 = int(wickets_over_balls_2[1])
        required_runs = team1_score - current_score
        required_run_rate = abs((required_runs/balls_left)*6)
        
    if inning ==1:
        dictionary = {
            'inning':inning,
            'current_score':current_score,
            'venue':venue,
            'team1':team1,
            'team2':team2,
            'fours_team1':team1_fours,
            'sixes_team1':team1_sixes,
            'current_score':current_score,
            'current_over':current_over,
            'current_ball_of_over':current_ball_of_over,
            'current_run_rate':current_run_rate,
            'wicket_loss':wicket_loss,
            'balls_left':balls_left,
            'over_left':over_left,
            'total_extra_runs':total_extra_runs,
            'projected_score':projected_score,
            'team2_won_toss':team2_won_toss
            
        }
    else:
        dictionary = {
            'inning':inning,
            'current_score':current_score,
            'venue':venue,
            'team1':team1,
            'team2':team2,
            'fours_team2':team1_fours,
            'sixes_team2':team1_sixes,
            'current_over':current_over,
            'current_ball_of_over':current_ball_of_over,
            'current_run_rate':current_run_rate,
            'wicket_loss':wicket_loss,
            'balls_left':balls_left,
            'over_left':over_left,
            'total_extra_runs':total_extra_runs,
            'team2_won_toss':team2_won_toss,
            'team1_score':team1_score,
            'team1_wickets': team1_wickets,
            'team1_extra_runs':team1_extra_runs,
            'over_playedBy_team1':over_playedBy_team1,
            'required_run_rate':required_run_rate,
            'required_runs':required_runs
            
        }

    
    return dictionary