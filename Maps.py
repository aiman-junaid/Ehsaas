# # # import folium
# # # from IPython.display import HTML
import json
import requests
from googleplaces import GooglePlaces, types, lang
import functools
import xlrd
import webbrowser
import googlemaps
import geocoder
import folium
import numpy as np


my_map1 = folium.Map(location=[24.8607, 67.0011],
                     zoom_start=12)

# save method of Map object will create a map
# webbrowser.open_new_tab('my_map.html')
gmaps = googlemaps.Client(key='AIzaSyDtXUOF8QiIB608KLzmSlPZJhHjh81Wrvw')
lat = gmaps.geolocate()["location"]["lat"]
lng = gmaps.geolocate()["location"]["lng"]


folium.Marker([round(lat, 2), round(lng, 2)],
              popup='Source').add_to(my_map1)
loc = ("Stores.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
longi = sheet.cell_value(1, 8)
latt = sheet.cell_value(1, 9)
folium.Marker([latt, longi],
              popup=sheet.cell_value(1, 1)).add_to(my_map1)

#API_KEY = 'AIzaSyDtXUOF8QiIB608KLzmSlPZJhHjh81Wrvw'


# def haversine_distance(lat1, lon1, lat2, lon2):
#     r = 6371
#     phi1 = np.radians(lat1)
#     phi2 = np.radians(lat2)
#     delta_phi = np.radians(lat2 - lat1)
#     delta_lambda = np.radians(lon2 - lon1)
#     a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * \
#         np.cos(phi2) * np.sin(delta_lambda / 2)**2
#     res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
#     print(np.round(res, 2))
#     return np.round(res, 2)


# google_places = GooglePlaces(API_KEY)
# query_result = google_places.nearby_search(
#     # lat_lng ={'lat': 46.1667, 'lng': -1.15},
#     lat_lng={'lat': latt, 'lng': longi},
#     radius=haversine_distance(lat, lng, latt, longi))
# query_result1 = google_places.nearby_search(
#     # lat_lng ={'lat': 46.1667, 'lng': -1.15},
#     lat_lng={'lat': lat, 'lng': lng},
#     radius=haversine_distance(lat, lng, latt, longi))

# if query_result.has_attributions:
#     print(query_result.html_attributions)


# coordinates = []
# coordinates.append([latt, longi])
# coordinates.append([round(lat, 2), round(lng, 2)])
# # Iterate over the search results
# for place in query_result.places:
#     # print(type(place))
#     # place.get_details()
#     coordinates.append([str(place.geo_location['lat']),
#                         str(place.geo_location['lng'])])
# for place in query_result1.places:
#     # print(type(place))
#     # place.get_details()
#     if [str(place.geo_location['lat']),
#             str(place.geo_location['lng'])] not in coordinates:
#         coordinates.append([str(place.geo_location['lat']),
#                             str(place.geo_location['lng'])])
#     else:
#         continue

coordinates = []
coordinates.append([latt, longi])
coordinates.append([round(lat, 2), round(lng, 2)])
my_PolyLine = folium.PolyLine(locations=coordinates, weight=5)
my_map1.add_child(my_PolyLine)
my_map1.save(" my_map.html ")
