
import plotly.graph_objects as go
import pandas as pd
import sys, time

#where is the data source file. Contains 'name' and 'data'
data_source=sys.argv[1]
#Getting the start date like 2020-03-28
if len(sys.argv) > 2:
    start_date = sys.argv[2]

df = pd.read_csv('./us_state_lonlat.csv')
df_data = pd.read_csv(data_source)
df.head()

df['text'] = df['name'] # + df['data'].astype(str) #+ '<br>Population ' + (df['pop']/1e6).astype(str)+' million'

frame_data={}
#Mask the entry based on the date that we want to see
df_data['date'] = pd.to_datetime(df_data['date']) 
mask=(df_data['date'] == start_date)
df_data = df_data.loc[mask]
frame_data[0]=df_data

'''
df_data = pd.read_csv(data_source)
mask=(df_data['date'] == pd.to_datetime(start_date+1))
df_data = df_data.loc[mask]
frame_data[1]=df_data
print frame_data
'''

# Let's combine the data source into the  geolocation source
# https://github.com/nytimes/covid-19-data/blob/master/us-states.csv
df = df.set_index('name')
df_data =df_data.set_index('state')
df['data']=df_data['cases']
df=df.fillna(axis=1, value='0')

#limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
limits = [(0,3000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 10


df['text']=df['text']+'\n'+df['data'].astype(str)

#fig = go.Figure()


# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

for i in range(len(limits)):
    lim = limits[i]
    # Breaking the list which is based in the order by population. 
    df_sub = df[lim[0]:lim[1]]
fig_dict = dict(
    layout = dict(
        title_text = 'US States Blah Blah<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        ),
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),

    data = [
        {'type': 'scattergeo', 
        'locationmode' : 'USA-states',
        'lon' : df_sub['lon'],
        'lat' : df_sub['lat'],
        'text' : df_sub['text'],
        'marker' : {
            'size' : df_sub['data'].astype(int)/scale, #10,  #df_sub['pop']/scale,
            'color' : colors[i],
            'line_color' : 'rgb(40,40,40)',
            'line_width': 0.5,
            'sizemode' : 'area'
            }
        
        
		},
#    'name' : '{0} - {1}'.format(lim[0],lim[1])

    ],

    frames = [
        {'name' : '0', 'layout' : {},
         'data': [
             {'type': 'scattergeo', 
              'locationmode' : 'USA-states',
              'lon' : df_sub['lon'],
              'lat' : df_sub['lat'],
              'text' : df_sub['text'],
              'marker' : {
                'size' : df_sub['data'].astype(int)/scale, #10,  #df_sub['pop']/scale,
                'color' : colors[i],
                'line_color' : 'rgb(40,40,40)',
                'line_width': 0.5,
                'sizemode' : 'area'
            }
            }
          ],
        },
        {'name' : '1', 'layout' : {},
         'data': [
             {'type': 'scattergeo', 
              'locationmode' : 'USA-states',
              'lon' : df_sub['lon'],
              'lat' : df_sub['lat'],
              'text' : df_sub['text'],
              'marker' : {
                'size' : df_sub['data'].astype(int)/scale, #10,  #df_sub['pop']/scale,
                'color' : colors[i],
                'line_color' : 'rgb(40,40,40)',
                'line_width': 1.5,
                'sizemode' : 'area'
            }
            }
            ]
        }
    ]
)

fig = go.Figure(fig_dict)

fig.show()


