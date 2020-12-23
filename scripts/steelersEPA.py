import pandas as pd
import matplotlib.pyplot as plt

YEAR = 2020

data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                         'play_by_play_' + str(YEAR) + '.csv.gz?raw=True',
                         compression='gzip', low_memory=False)
                         
data = data.loc[data.season_type=='REG']

pit_data = data.loc[(data.posteam=='PIT')]

pit_data = pit_data.loc[pit_data.play_type.isin(['no_play','pass','run'])]

pit_data = pit_data.groupby('week', as_index=False)[['epa']].mean()

print(data)

plt.figure(figsize=(10,10))

plt.plot(pit_data.week, pit_data.epa, color='#FFB612', marker='.')

plt.grid(zorder=0, alpha=0.4)
plt.xlabel('Week')
plt.ylabel('Offensive EPA per play')
plt.title('Steelers\' Offensive EPA Timeline')

plt.axhline(y=0,linestyle='--', color='grey')

plt.savefig('scripts/figures/steelersEPA.png', dpi=800)

