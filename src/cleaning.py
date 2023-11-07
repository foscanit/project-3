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

def mongo_city():
    client = MongoClient("localhost:27017")
    db = client["Ironhack"]
    c = db.get_collection("companies")
    
    
    filters4 = {"category_code": "games_video", "offices.city": "Tokyo"}
    projection4 = {'name': 1, '_id': 0, 'offices': 1, 'category_code': 1}
    Tok = list(c.find(filters4, projection4).sort('number_of_employees', -1))
    
    # Extract the relevant information from the nested structure
    tok_df = []
    for entry in Tok:
        name = entry['name']
        category_code = entry['category_code']
        for office in entry['offices']:
            description = office.get('description', '')
            address1 = office.get('address1', '')
            address2 = office.get('address2', '')
            zip_code = office.get('zip_code', '')
            city = office.get('city', '')
            country_code = office.get('country_code', '')
            tok_df.append([name, category_code, description, address1, address2, zip_code, city, country_code])

    # Create the DataFrame
    columns = ['name', 'category_code', 'description', 'address1', 'address2', 'zip_code', 'city', 'country_code']
    tok_df = pd.DataFrame(tok_df, columns=columns)
    
    tok_df = tok_df.drop_duplicates() 
    
    tok_df['lat'] = None  
    tok_df['lon'] = None  
    
    desired_value = 'Tokyo'
    tok_df = tok_df[tok_df['city'] == desired_value]
    
    tok_df.at[0, 'lat'] = 35.6948056
    tok_df.at[0, 'lon'] = 139.6393433
    tok_df.at[2, 'lat'] = 35.6587603
    tok_df.at[2, 'lon'] = 139.72941112
    tok_df.at[3, 'lat'] = 35.7122007
    tok_df.at[3, 'lon'] = 139.7021159
    tok_df.at[7, 'lat'] = 35.6871672
    tok_df.at[7, 'lon'] = 139.7867856
    tok_df.at[8, 'lat'] = 35.6633886
    tok_df.at[8, 'lon'] = 139.6655874
    tok_df.at[9, 'lat'] = 35.6898602
    tok_df.at[9, 'lon'] = 139.6899144
    tok_df.at[10, 'lat'] = 35.664797
    tok_df.at[10, 'lon'] = 139.7086912
    
    return tok_df


def tech_startup():
    start_ups = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/startups.csv")
    start = start_ups.dropna(subset=["lat"])
    start = start.drop(20)
    
    return start

def import_dog():
    
    dog = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/dog.csv")
    
    return dog   

def import_guardes():
    
    guardes = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/guardes.csv")
    
    return guardes

def import_kara():
    
    kara = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/kara.csv")
    
    return kara

def import_starbucks():
    
    starbucks = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/starbucks.csv")
    
    return starbucks

def import_train():
    
    train = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/train.csv")
    
    return train

def import_veg():
    
    veg = pd.read_csv("/Users/usuari/Desktop/Ironhack/BOOTCAMP/projects/project-3/data/veg.csv")
    
    return veg
    




        
