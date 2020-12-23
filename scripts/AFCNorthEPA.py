import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2020

data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                         'play_by_play_' + str(YEAR) + '.csv.gz?raw=True',
                         compression='gzip', low_memory=False)
                         
data = data.loc[data.season_type=='REG']

pit_data = data.loc[(data.posteam=='PIT')]
bal_data = data.loc[(data.posteam=='BAL')]
cle_data = data.loc[(data.posteam=='CLE')]
cin_data = data.loc[(data.posteam=='CIN')]

pit_data = pit_data.loc[pit_data.play_type.isin(['no_play','pass','run'])]
bal_data = bal_data.loc[bal_data.play_type.isin(['no_play','pass','run'])]
cle_data = cle_data.loc[cle_data.play_type.isin(['no_play','pass','run'])]
cin_data = cin_data.loc[cin_data.play_type.isin(['no_play','pass','run'])]


pit_data = pit_data.groupby('week', as_index=False)[['epa']].mean()
bal_data = bal_data.groupby('week', as_index=False)[['epa']].mean()
cle_data = cle_data.groupby('week', as_index=False)[['epa']].mean()
cin_data = cin_data.groupby('week', as_index=False)[['epa']].mean()

plt.figure(figsize=(10,10))

plt.plot(pit_data.week, pit_data.epa, color='#FFB612', marker='.', label='PIT')
plt.plot(bal_data.week, bal_data.epa, color='#241773', marker='.', label='BAL')
plt.plot(cle_data.week, cle_data.epa, color='#311D00', marker='.', label='CLE')
plt.plot(cin_data.week, cin_data.epa, color='#FB4F14', marker='.', label='CIN')

plt.grid(zorder=0, alpha=0.4)
plt.xlabel('Week')
plt.ylabel('Offensive EPA per play')
plt.title('AFC North Offensive EPA By Week')

plt.axhline(y=0,linestyle='--', color='grey')
plt.legend()

plt.savefig('scripts/figures/AFCNorthEPA.png', dpi=800)

