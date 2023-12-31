import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas
import lxml

URL = "https://www.nba.com/stats"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept-Language": "en-US,en;q=0.5"
}

req = requests.get(URL, headers=HEADERS)
web_html_data = req.text

soup = BeautifulSoup(web_html_data, 'lxml')

# Yesterday's Leaders
players = soup.select(".LeaderBoardPlayerCard_lbpcTableRow___Lod5 .LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
data = [p.getText() for p in players]
# print(data)
players_list = [data[i] for i in range(0, len(data), 2)]
less_player_list = players_list
# print(players_list[:45])
# print(len(players_list) - 27)
# print(len(less_player_list))

stats = soup.select(".LeaderBoardWithButtons_lbwbCardValue__5LctQ .LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
stats_list = [float(st.text) for st in stats]
# print(stats_list)
# print(len(stats_list))

pts_leaders = {player : stat for (player,stat) in zip(less_player_list[0:5],stats_list[0:5])}
reb_leaders = {player : stat for (player,stat) in zip(less_player_list[5:10],stats_list[5:10])}
ast_leaders = {player : stat for (player,stat) in zip(less_player_list[10:15],stats_list[10:15])}
blk_leaders = {player : stat for (player,stat) in zip(less_player_list[15:20],stats_list[15:20])}
stl_leaders = {player : stat for (player,stat) in zip(less_player_list[20:25],stats_list[20:25])}
to_leaders = {player : stat for (player,stat) in zip(less_player_list[25:30],stats_list[25:30])}
# yesterdays_leaders = dict(zip(less_player_list,stats_list))
print(pts_leaders)
print(reb_leaders)
print(ast_leaders)
print(blk_leaders)
print(stl_leaders)
print(to_leaders)

yesterdays_leaders = {
    'Rebounds': reb_leaders
}

# print(yesterdays_leaders)

test = {
    "Players": less_player_list[:45],
    "Stats": stats_list[:45]
}

nba_data = pandas.DataFrame(yesterdays_leaders)
nba_data.to_csv("nba_yesterdays_data.csv")
