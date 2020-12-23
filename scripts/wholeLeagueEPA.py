import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2020

data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                         'play_by_play_' + str(YEAR) + '.csv.gz?raw=True',
                         compression='gzip', low_memory=False)
                         
data = data.loc[data.season_type=='REG']

teamAbbreviations = pd.read_csv('https://gist.githubusercontent.com/cnizzardini/13d0a072adb35a0d5817/raw/dbda01dcd8c86101e68cbc9fbe05e0aa6ca0305b/nfl_teams.csv')
teamAbbreviations = teamAbbreviations.Abbreviation
teamAbbreviations[28] = 'LA'

COLORS = {'ARI':'#97233F','ATL':'#A71930','BAL':'#241773','BUF':'#00338D','CAR':'#0085CA','CHI':'#00143F',
          'CIN':'#FB4F14','CLE':'#FB4F14','DAL':'#B0B7BC','DEN':'#002244','DET':'#046EB4','GB':'#24423C',
          'HOU':'#C9243F','IND':'#003D79','JAX':'#136677','KC':'#CA2430','LA':'#002147','LAC':'#2072BA',
          'LV':'#C4C9CC','MIA':'#0091A0','MIN':'#4F2E84','NE':'#0A2342','NO':'#A08A58','NYG':'#192E6C',
          'NYJ':'#203731','PHI':'#014A53','PIT':'#FFC20E','SEA':'#7AC142','SF':'#C9243F','TB':'#D40909',
          'TEN':'#4095D1','WAS':'#FFC20F'}

for i in range(0, len(teamAbbreviations)):
    
    team_data = data.loc[(data.posteam==teamAbbreviations[i])]
    team_data = team_data.loc[team_data.play_type.isin(['no_play','pass','run'])]
    team_data = team_data.groupby('week', as_index=False)[['epa']].mean()

    plt.figure(figsize=(10,10))

    plt.plot(team_data.week, team_data.epa, color=COLORS[teamAbbreviations[i]], marker='.', label=teamAbbreviations[i])

    plt.grid(zorder=0, alpha=0.4)
    plt.xlabel('Week')
    plt.ylabel('Offensive EPA per play')
    plt.title(teamAbbreviations[i] + ' Offensive EPA By Week')

    plt.axhline(y=0,linestyle='--', color='grey')
    plt.legend()

    plt.savefig('scripts/figures/wholeLeagueEPA/' + teamAbbreviations[i] + 'EPA.png', dpi=400)
