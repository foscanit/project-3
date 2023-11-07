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

def circle_map0():
    
    # Narita airport's coordinates:

    lati = 35.770178
    longi = 140.3817412
    
    # Haneda airport's coordinates:

    latu = 35.5493932
    longu = 139.7772583
    
    # Create a base map centered around Tokyo, Japan
    m = folium.Map(location=[35.652832, 139.839478], zoom_start=13)

    # Add the narita marker
    icon = folium.Icon(color='pink', icon_color='white', icon='plane', prefix='fa')
    narita = folium.Marker(location=[lati, longi], tooltip="Narita Airport", icon=icon)
    narita.add_to(m)

    # Add the haneda marker
    icon = folium.Icon(color='pink', icon_color='white', icon='plane', prefix='fa')
    haneda = folium.Marker(location=[latu, longu], tooltip="Haneda Airport", icon=icon)
    haneda.add_to(m)


    # Add other markers from tok_df to the map
    tok_df = mongo_city()
    for index, row in tok_df.iterrows():
        tooltip = row['name']
        icon = folium.Icon(color='purple', icon_color='white', icon='gamepad', prefix='fa')
        folium.Marker(location=[row['lat'], row['lon']], tooltip=tooltip, icon=icon).add_to(m)
    

    # Add the successful tech startups that have coordinates  
    start = tech_startup()
    for index, row in start.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='red', icon_color='white', icon='cloud-upload', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lon']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
          
    # pet places
    dog_d = import_dog()
    for index, row in dog_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='blue', icon_color='white', icon='paw', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
     # elementary school
    guardes_d = import_guardes()
    for index, row in guardes_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='blue', icon_color='black', icon='child', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
     # karaokes
    kara_d = import_kara()
    for index, row in kara_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='black', icon_color='white', icon='microphone', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
    # starbucks
    starbucks_d = import_starbucks()
    for index, row in starbucks_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='red', icon_color='black', icon='coffee', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
            
    # metro stations
    train_d = import_train()
    for index, row in train_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='orange', icon_color='black', icon='train', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
            
    # vegan places
    veg_d = import_veg()
    for index, row in veg_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='green', icon_color='white', icon='leaf', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
        
    # Add circles with a ratio of the closest things
    
    circles = [
        {"center": [35.669185, 139.734548], "radius": 1500, "color": "red",},
        {"center": [35.657591, 139.699055], "radius": 1500, "color": "blue"},
        {"center": [35.627796, 139.740745], "radius": 1500, "color": "green"},
        {"center": [35.661512, 139.728418], "radius": 1500, "color": "orange"},
        {"center": [35.673578, 139.764248], "radius": 1500, "color": "purple"},
        {"center": [35.673165, 139.738309], "radius": 1500, "color": "yellow"},
        {"center": [35.693763, 139.703632], "radius": 1500, "color": "gray"}
        
    ]

    for circle_info in circles:
        circle_center = circle_info["center"]
        circle_radius = circle_info["radius"]
        circle_color = circle_info["color"]

        folium.Circle(
            location=circle_center,
            radius=circle_radius,
            color=circle_color,
            fill=True,
            fill_color=circle_color,
            fill_opacity=0.2
        ).add_to(m)

    return m

def circle_map6():
    
    # Create a base map centered around Tokyo, Japan
    m = folium.Map(location=[35.656467,139.7318437], zoom_start=15)
    
    # Narita airport's coordinates:

    lati = 35.770178
    longi = 140.3817412
    
    # Haneda airport's coordinates:

    latu = 35.5493932
    longu = 139.7772583

    # Add the narita marker
    icon = folium.Icon(color='pink', icon_color='white', icon='plane', prefix='fa')
    narita = folium.Marker(location=[lati, longi], tooltip="Narita Airport", icon=icon)
    narita.add_to(m)

    # Add the haneda marker
    icon = folium.Icon(color='pink', icon_color='white', icon='plane', prefix='fa')
    haneda = folium.Marker(location=[latu, longu], tooltip="Haneda Airport", icon=icon)
    haneda.add_to(m)

   
    # Add other markers from tok_df to the map
    tok_df = mongo_city()
    for index, row in tok_df.iterrows():
        tooltip = row['name']
        icon = folium.Icon(color='purple', icon_color='white', icon='gamepad', prefix='fa')
        folium.Marker(location=[row['lat'], row['lon']], tooltip=tooltip, icon=icon).add_to(m)
    

    # Add the successful tech startups that have coordinates  
    start = tech_startup()
    for index, row in start.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='red', icon_color='white', icon='cloud-upload', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lon']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
          
    # pet places
    dog_d = import_dog()
    for index, row in dog_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='blue', icon_color='white', icon='paw', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
    # elementary school
    guardes_d = import_guardes()
    for index, row in guardes_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='blue', icon_color='black', icon='child', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
    # karaokes
    kara_d = import_kara()
    for index, row in kara_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='black', icon_color='white', icon='microphone', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
    # starbucks
    starbucks_d = import_starbucks()
    for index, row in starbucks_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='red', icon_color='black', icon='coffee', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
            
    # metro stations
    train_d = import_train()
    for index, row in train_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='orange', icon_color='black', icon='train', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
            
            
    # vegan places
    veg_d = import_veg()
    for index, row in veg_d.iterrows():
            tooltip = row['name']
            icon = folium.Icon(color='green', icon_color='white', icon='leaf', prefix='fa')
            folium.Marker(
                location=[row['lat'], row['lng']],
                tooltip=tooltip,
                icon=icon
                ).add_to(m)
        
    # Add circles with a ratio of the closest things
    circle_center = [35.6555691, 139.7343113] # I have chosen this center because it's a dog grooming place that it's nearby to all the things required.
    circle_radius = 900 
    circle_radius_2 = 1500

    # Create a circle with the specified center and radius
    folium.Circle(location=circle_center, radius=circle_radius, color='red', fill=True, fill_color='red', fill_opacity=0.2).add_to(m)
    folium.Circle(location=circle_center, radius=circle_radius_2, color='blue', fill=True, fill_color='red', fill_opacity=0.2).add_to(m)
    
     # Create a legend
    legend_html = """
    <div style="position: fixed; top: 10px; left: 10px; z-index: 1000; background-color: white; padding: 10px; border: 2px solid black;">
        <div><i class="fa fa-plane" style="color: pink;"></i> Narita Airport</div>
        <div><i class="fa fa-plane" style="color: pink;"></i> Haneda Airport</div>
        <div><i class="fa fa-gamepad" style="color: purple;"></i> Videogame company</div>
        <div><i class="fa fa-cloud-upload" style="color: red;"></i> Tech Startup</div>
        <div><i class="fa fa-paw" style="color: blue;"></i> Dog Place</div>
        <div><i class="fa fa-child" style="color: blue;"></i> Elementary School</div>
        <div><i class="fa fa-microphone" style="color: black;"></i> Karaoke</div>
        <div><i class="fa fa-coffee" style="color: red;"></i> Starbucks</div>
        <div><i class="fa fa-train" style="color: orange;"></i> Metro Station</div>
        <div><i class="fa fa-leaf" style="color: green;"></i> Vegan Place</div>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    

    return m