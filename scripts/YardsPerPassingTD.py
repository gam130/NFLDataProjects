import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

YEAR = 2019

data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                         'play_by_play_' + str(YEAR) + '.csv.gz?raw=True',
                         compression='gzip', low_memory=False)

data = data.loc[data.season_type=='REG']

yards = data.yards_gained.loc[(data.play_type=='pass') & (data.complete_pass==1)]
air_yards = data.air_yards.loc[(data.play_type=='pass') & (data.complete_pass==1)]
print(air_yards.count())
plt.figure(figsize=(12, 8))

plt.hist(yards, bins=100, color='blue', label='Total yards per complete pass')
plt.hist(air_yards, bins=50, color='red', label='Air Yards per complete pass', alpha=.7)

plt.xlabel('Yards per complete pass', fontsize=12)
plt.ylabel('Number of passes', fontsize=12)

plt.title('Distribution of how long passes were in 2019')

plt.xticks(np.arange(-10, 100, step=10))
plt.legend()

plt.savefig('scripts/figures/ydsTDdist.png', dpi=400)