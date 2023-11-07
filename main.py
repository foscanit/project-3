import requests
import json
import pandas as pd
from getpass import getpass
import os
from dotenv import load_dotenv
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element
import time
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
from pymongo import MongoClient
from geopy.geocoders import Nominatim


import src.cleaning as clean
import src.visualizing as vis

if __name__ == '__main__':
    clean.mongo_city()
    clean.tech_startup()
    clean.import_dog()
    clean.import_guardes()
    clean.import_kara()
    clean.import_starbucks()
    clean.import_train()
    clean.import_veg()
    vis.circle_map0()
    vis.circle_map6