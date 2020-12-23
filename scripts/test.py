import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2019

data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                         'play_by_play_' + str(YEAR) + '.csv.gz?raw=True',
                         compression='gzip', low_memory=False)
                         
data = data.loc[data.season_type=='REG']

passing_tds = data.loc[(data.play_type=='pass') & (data.touchdown==1) & (data.qb_scramble==0) & (data.posteam==data.td_team)] 
passing_tds = passing_tds.groupby(['passer']).agg({'yards_gained' : 'mean', 'play_id' : 'count'})

passing_tds = passing_tds.loc[passing_tds.play_id > 4]

passing_tds.sort_values('play_id', ascending=False, inplace=True)
passing_tds.columns = ['Avg. TD yardage', 'TDs']

passing_tds = passing_tds.round(2)

print(passing_tds)

plt.figure(figsize=(10,10))

plt.scatter(passing_tds['Avg. TD yardage'], passing_tds['TDs'], alpha=0.7, color='red')

plt.xlabel('Avg. TD Yardage')
plt.ylabel('Number of TDs')
plt.title('Length and Number of Touchdown passes in the NFL by QB')

plt.grid(zorder=0,alpha=0.4)

plt.savefig('scripts/figures/avgAndNum.png', dpi=800)


