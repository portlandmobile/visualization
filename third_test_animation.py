
import plotly.graph_objects as go
import pandas as pd
import sys, time


# make figure
fig_dict = {
    "data": [],
    "layout": {},
    "frames": []
}

fig_dict = dict(
    layout = dict(
        xaxis1 = {'domain': [0.0, 0.44], 'anchor': 'y1', 'title': '1', 'range': [-2.25, 3.25]},
        yaxis1 = {'domain': [0.0, 1.0], 'anchor': 'x1', 'title': 'y', 'range': [-20.0, 24.0]},
        xaxis2 = {'domain': [0.56, 1.0], 'anchor': 'y2', 'title': '2', 'range': [-2.25, 3.25]},
        yaxis2 = {'domain': [0.0, 1.0], 'anchor': 'x2', 'title': 'y', 'range': [-518.64200000000005, 10500.982]},
        title  = '',
        margin = {'t': 50, 'b': 50, 'l': 50, 'r': 50},
        updatemenus = [{'buttons': [{'args': [['0', '1', '2', '3'], {'frame': {'duration': 500.0, 'redraw': False}, 'fromcurrent': True, 'transition': {'duration': 0, 'easing': 'linear'}}], 'label': 'Play', 'method': 'animate'}, {'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}], 'label': 'Pause', 'method': 'animate'}], 'direction': 'left', 'pad': {'r': 10, 't': 85}, 'showactive': True, 'type': 'buttons', 'x': 0.1, 'y': 0, 'xanchor': 'right', 'yanchor': 'top'}],
        sliders = [{'yanchor': 'top', 'xanchor': 'left', 'currentvalue': {'font': {'size': 16}, 'prefix': 'Frame: ', 'visible': True, 'xanchor': 'right'}, 'transition': {'duration': 500.0, 'easing': 'linear'}, 'pad': {'b': 10, 't': 50}, 'len': 0.9, 'x': 0.1, 'y': 0, 
                    'steps': [{'args': [['0'], {'frame': {'duration': 500.0, 'easing': 'linear', 'redraw': False}, 'transition': {'duration': 0, 'easing': 'linear'}}], 'label': '0', 'method': 'animate'}, 
                              {'args': [['1'], {'frame': {'duration': 500.0, 'easing': 'linear', 'redraw': False}, 'transition': {'duration': 0, 'easing': 'linear'}}], 'label': '1', 'method': 'animate'}, 
                              {'args': [['2'], {'frame': {'duration': 500.0, 'easing': 'linear', 'redraw': False}, 'transition': {'duration': 0, 'easing': 'linear'}}], 'label': '2', 'method': 'animate'},
                              {'args': [['3'], {'frame': {'duration': 500.0, 'easing': 'linear', 'redraw': False}, 'transition': {'duration': 0, 'easing': 'linear'}}], 'label': '3', 'method': 'animate'}, 
                    ]}]
    ),

    data = [
        {'type': 'scatter', 'name': 'f1', 'x': [-2.  , -1.  ,  0.01,  1.  ,  2.  ,  3.  ], 'y': [  4.00000000e+00,   1.00000000e+00,   1.00000000e-04, 1.00000000e+00,   4.00000000e+00,   9.00000000e+00], 'hoverinfo': 'name+text', 'marker': {'opacity': 1.0, 'symbol': 'circle', 'line': {'width': 0, 'color': 'rgba(50,50,50,0.8)'}}, 'line': {'color': 'rgba(255,79,38,1.000000)'}, 'mode': 'markers+lines', 'fillcolor': 'rgba(255,79,38,0.600000)', 'legendgroup': 'f1', 'showlegend': True, 'xaxis': 'x1', 'yaxis': 'y1'}
    ],

    frames = [
        {'name' : '0', 'layout' : {},
         'data': [
             {'type': 'scatter', 
              'name': 'f1', 
               'x': [-2.  , -1.  ,  0.01,  1.  ,  2.  ,  3.  ], 
               'y': [  4.00,   1.00,   1.00000000e-04, 1.00,   4.00,   9.00], 
               'hoverinfo': 'name+text', 
               'marker': {
                          'opacity': 1.0, 
               			  'symbol': 'circle',
               			  'size' : 10
               			  }, 
               	'line': {'color': 'rgba(255,79,38,1.000000)'}, 
               	'mode': 'markers+lines', 
               	'fillcolor': 'rgba(255,79,38,0.600000)', 
               	'legendgroup': 'f1', 
               	'showlegend': True, 
               	'xaxis': 'x1', 
               	'yaxis': 'y1'
              }
             ],
        },

        {'name' : '1', 'layout' : {},
         'data': [
             {'type': 'scatter', 'name': 'f1', 'x': [-2.  , -1.  ,  0.01,  1.  ,  2.  ,  3.  ], 'y': [ 6.    ,  2.    , -0.0099,  0.    ,  2.    ,  6.    ], 'hoverinfo': 'name+text', 'marker': {'opacity': 1.0, 'symbol': 'circle', 'size' : 5, 'line': {'width': 0, 'color': 'rgba(50,50,50,0.8)'}}, 'line': {'color': 'rgba(255,79,38,1.000000)'}, 'mode': 'markers+lines', 'fillcolor': 'rgba(255,79,38,0.600000)', 'legendgroup': 'f1', 'showlegend': True, 'xaxis': 'x1', 'yaxis': 'y1'} 
             ],
        },

        {'name' : '2', 'layout' : {},
         'data': [
             {'type': 'scatter', 'name': 'f1', 'x': [-2.  , -1.  ,  0.01,  1.  ,  2.  ,  3.  ], 'y': [ 8.    ,  3.    , -0.0199, -1.    ,  0.    ,  3.    ], 'hoverinfo': 'name+text', 'marker': {'opacity': 1.0, 'symbol': 'circle', 'line': {'width': 0, 'color': 'rgba(50,50,50,0.8)'}}, 'line': {'color': 'rgba(255,79,38,1.000000)'}, 'mode': 'markers+lines', 'fillcolor': 'rgba(255,79,38,0.600000)', 'legendgroup': 'f1', 'showlegend': True, 'xaxis': 'x1', 'yaxis': 'y1'}
             
             ],
        },

        {'name' : '3', 'layout' : {},
         'data': [
             {'type': 'scatter', 'name': 'f1', 'x': [-2.  , -1.  ,  0.01,  1.  ,  2.  ,  3.  ], 'y': [ 10.    ,   4.    ,  -0.0299,  -2.    ,  -2.    ,   0.    ], 'hoverinfo': 'name+text', 'marker': {'opacity': 1.0, 'symbol': 'circle', 'line': {'width': 0, 'color': 'rgba(50,50,50,0.8)'}}, 'line': {'color': 'rgba(255,79,38,1.000000)'}, 'mode': 'markers+lines', 'fillcolor': 'rgba(255,79,38,0.600000)', 'legendgroup': 'f1', 'showlegend': True, 'xaxis': 'x1', 'yaxis': 'y1'}
             
             ],
        }
    ]
)

fig = go.Figure(fig_dict)

fig.show()


