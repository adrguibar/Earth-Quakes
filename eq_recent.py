#Earthquakes for february 2022
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#get eq data
file_name = 'data/all_month.geojson.json'
with open(file_name,'r',encoding='utf-8') as f:
        all_eq_data = json.load(f)

#Format data
file_name = 'data/readable_file_eq.json'
with open(file_name, 'w') as f:
    readable_file = json.dump(all_eq_data, f, indent=4)

#get data dict
all_eq_dict = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dict:
    if (eq_dict['properties']['mag'] < 0):
        continue
    else:
        mags.append(eq_dict['properties']['mag'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])


#plot
title = all_eq_data['metadata']['title']
data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_texts,
         'marker':{
             'size': [5*mag for mag in mags],
             'color': mags,
             'colorscale': 'inferno',
             'reversescale': True,
             'colorbar':{'title': 'Magnitude'}
             }

         }]
my_layout = Layout(title=f'{title}')

#configuer plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_2022.html')