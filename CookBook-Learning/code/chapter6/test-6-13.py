import pandas as pd
import numpy as np
import os

dir_path = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                        '../../../'))
csv_file = os.path.join(dir_path, 'tmp\\rats.csv')

rats = pd.read_csv(csv_file)
print(rats['Current Activity'].unique)

crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print('crew_dispatched', crew_dispatched, len(crew_dispatched))


dates = crew_dispatched.groupby('Completion Date')
print('dates:', len(dates))

date_counts = dates.size()
print(date_counts[1:10])
date_counts.sort()
print(date_counts[1:10])
