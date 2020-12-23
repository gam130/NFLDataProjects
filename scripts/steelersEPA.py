import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2020

data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                         'play_by_play_' + str(YEAR) + '.csv.gz?raw=True',
                         compression='gzip', low_memory=False)
                         
data = data.loc[data.season_type=='REG']

data = data.loc[(data.posteam=='PIT')]

data = data.loc[data.play_type.isin(['no_play','pass','run'])]

data = data.groupby('week', as_index=False)[['epa']].mean()

print(data)

plt.figure(figsize=(10,10))

plt.plot(data.week, data.epa, color='#FFB612', marker='.')

plt.grid(zorder=0, alpha=0.4)

plt.xlabel('Week')
plt.ylabel('Offensive EPA per play')
plt.title('Steelers\' Offensive EPA Timeline')

plt.axhline(y=0,linestyle='--', color='grey')

plt.savefig('scripts/figures/steelersEPA.png', dpi=800)

