# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:22:59 2024

@author: citiz
"""
###convert json to geoson
import json
input_file=json.load(open("china_coord.json", "r", encoding="utf-8"))
geosontest={"type": "FeatureCollection","features":[]}
for i in range(len(input_file)):
	geosontest['features'].append({"properties":{"name":list(input_file.keys())[i].capitalize(),"cname":list(input_file.values())[i]['hanzi']}}|{"geometry":{"type":"Point","coordinates":list(input_file.values())[i]['coord']}})
geosontest=str(geosontest)
with open(r"china_coord_updated.geojson","w") as ff:
	ff.write(geosontest)

