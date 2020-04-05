#Reference from: https://plotly.com/python/bubble-maps/
#Command to run this:
# python test_plotly.py https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv 2020-03-29
# Reference:  More Plotly docs is here  https://plotly.com/~notebook_demo/254/interact-here-is-a-simple-example-of-usi/#/


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

#Mask the entry based on the date that we want to see
df_data['date'] = pd.to_datetime(df_data['date']) 
mask=(df_data['date'] == start_date)
df_data = df_data.loc[mask]

# Let's combine the data source into the  geolocation source
# https://github.com/nytimes/covid-19-data/blob/master/us-states.csv
df = df.set_index('name')
df_data =df_data.set_index('state')
df['data']=df_data['cases']
df=df.fillna(axis=1, value='0')

#limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
limits = [(0,50)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 10


df['text']=df['text']+'\n'+df['data'].astype(str)

# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}


# fill in most of layout
fig_dict["layout"]["title_text"] = "US States Blah Blah<br>(Click legend to toggle traces)"
fig_dict["layout"]["showlegend"] = True
fig_dict["layout"]["geo"] = dict(scope = 'usa',landcolor = 'rgb(217, 217, 217)')
fig_dict["layout"]["updatemenus"] = [
{
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": False},
                                "fromcurrent": True, "transition": {"duration": 300,
                                                                    "easing": "quadratic-in-out"}}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }
]



figAnim = go.Figure(fig_dict)
# figAnim.show()

#######
# # https://medium.com/swlh/interactive-animated-travel-data-visualizations-mapping-nba-travel-a154a2e7c18d
#######
#Seems like I can just add more frames to existing figures
frame = {"data": [], "name": 'testFrame1'}
data_dict= {
    
          'data': [
             {'type': 'Scattergeo', 
              'name': 'f1', 
               'marker': {
                          'size' : 10
                          }
              }
             ],
        }
frame["data"].append(data_dict)
fig_dict["frames"].append(frame)

######
# End
######
fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    # Breaking the list which is based in the order by population. 
    df_sub = df[lim[0]:lim[1]]
    orig_trace= fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['data'].astype(int)/scale, #10,  #df_sub['pop']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))


fig.update_layout(
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
    )


fig.show()

# Test to see how to add another trace and potentially use batch_animate()
# Just copy from the same as above and make a small change

#update_trace does not seem to auto refresh. Can't figure how to refresh without calling another show()
#time.sleep(3)
#fig.update_traces(
#          marker = dict (size=df_sub['data'].astype(int)/100)
#     )
