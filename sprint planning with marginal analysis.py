import pandas as pd
from tabulate import tabulate

df = pd.read_excel('backlog task data.xlsx',
        index_col=0,            # the first column contains the index labels (numbers assigned otherwise)
        # skipfooter=2,           # ignore the last two lines of the sheet
        #header=0,               # take the column names from the second row
        #usecols='A:S',          # use these Excel columns
        #sheet_name='Sheet1'  # take data from this sheet
        )
    
df['Value'] = [10 if df['Priority'][task] == "High" else 5 if df['Priority'][task] == "Medium" else 2 if df['Priority'][task] == "Low" else 0 for task in df.index]
df['value_per_storypoint'] = [df['Value'][task] / df['Story_Points'][task] for task in df.index]
df = df.sort_values(by=['value_per_storypoint'], ascending=False)
print(df)


story_points_available = 16.5
output = [['Task', 'Story_Points', 'story_points_left']]

# choose highest marginal value tasks until constraint reached
for task in df.index:
    if df['Story_Points'][task] <= story_points_available:
        story_points_available -= df['Story_Points'][task]
        output.append([task, df['Story_Points'][task], story_points_available])
        
print('\nResults\n', tabulate(output, tablefmt="simple"))
