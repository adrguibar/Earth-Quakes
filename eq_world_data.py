import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#exploring the data structure from the data
file_name = 'data\eq_data_30_day_m1.json'
with open(file_name) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dict = all_eq_data['features']

#extracting the information about the earthquakes
mags,lons,lats,hover_texts = [],[],[],[]
for eq_dict in all_eq_dict:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

#ploting the data
title = all_eq_data["metadata"]["title"]
data = [{'type':'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_texts,
         'marker':{
            'size': [5*mag for mag in mags],
             'color': mags,
             'colorscale': 'Viridis',
             'reversescale': True,
             'colorbar': {'title': 'Magnitude'}

            },
         }]
my_layout = Layout(title=f'{title}')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
