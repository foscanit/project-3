# project-III-geospatial-data

# Overview

In this case scenario I have created a new company in the gaming industry. The aim of the project is to choose a city and coordinates to locate this company through MongoDB, the database of companies and geoqueries. In order to pick the best location I have taken into account several conditions and requirements from my employees. 
<br>

# Requirements/Libraries Used:
This code was written in Python/Jupyter Notebook, using the following libraries:
<br>
- Pandas
- Requests
- json
- os
- dotenv
- Geopandas
- Cartoframes
- Time
- Folium
- Pymongo
- Geopy
<br>

# Goals:

I considered all the demands from my staff and the ones I prioritized were the following:

1) 30% of the company staff are parents, so I need to choose a secure and fun city for the kids, and also place the office close to an elementary school.

2) There should be video game companies near the office, at least one, so that my designers can share knowledge with other video games designers.

3) The company should be close to at least one tech startup that has raised 1 Million dollars or more, as requested by the developers. 

4) The office has to be close to one or more Starbucks for executives to drown in coffee.

5) Also, the office has to be well connected with metro and train stations.

6) There must be some karaokes nearby so that the employees can have fun together after work. 

7) Close to the office, there should also be a pet grooming place for our dog, Dobby.

8) And finally, if possible, find nearby the office one or more vegan places so that the CEO can eat without having to go too far away. 
<br>


# Workflow/ Methodology:

## 1. MongoDB filters and queries

First of all, after connecting in my Jupyter Notebook file with MongoDB and the collection of companies, I checked in which cities there were tech startups that have raised at least one Million dollars. For this query, I used regex to check if in the "tag_list" category of companies there was the tag of "startup" and also I checked if in the string value of "total_money_raised" there was an "m" equivalent to "million". The cities that met these conditions were Irvine, New York, San Francisco, Seattle, London and Minneapolis. But then, I realized that these weren't the best cities to live with children according to my research, so I changed my project's approach and decided to filter the companies differently. 

So after that I checked in which cities there were more video games companies. From the result of the query, I created a set of the cities, and then I made a dictionary in which the keys were the cities, and the values were the number of video games companies that each city had. I compared the results of this dictionary with the best ten cities in the world to live with children (see the source at the end). The criteria taken into account when drawing up the list of best cities were as follows: 

1. Quality of life
2. Crime rate
3. Attractions
4. Outdoor activities
5. Pollution Index
6. The cost of renting a three bedroom apartment
7. Child care costs
8. Total monthly bills

Among these ten cities, I picked Tokyo because it was the one that had more video games companies according to the dictionary. 

Then I filtered through MongoDB the video games companies located in Tokyo, and created a dataframe out of it. I dropped the duplicated data, I created the columns for the latitude and longitude coordinates (as in the results of the Mongo query these categories had "None" values), and afterwards, I added the coordinates values for each company (since I had the addresses).
<br>


## 2. Foursquare

At this point of the project I decided to use Tokyo's coordinates to create a function with Foursquare's API. Through this function I wanted to find 50 locations for each place required by the staff. So I looked up Starbucks, pet grooming places, metro stations, karaokes, vegan places and I placed them into a folium map. For each Foursquare query I saved a csv file, just in case I didn't have to use the API again if I restarted the code. I also used the dataframe of the video games companies, created before, to locate each of them in the same map.

Later on, I made another query through MongoDB to check which companies in Tokyo had raised at least one Million dollars and from this I made another dataframe. After that, I created a function with geocode to extract the coordinates of each company, as most of them had empty values in the latitude and longitude columns. Then I applied the function and cleaned the dataframe, keeping only the companies whose coordinates had been extracted. I saved the cleaned dataset into a csv file.  
<br>


## 3. Visualizations

Finally, I also located the successful tech companies from the cleaned dataframe into the same map and I added circles (7) using these companies' coordinates to check which one had more places inside its ratio. These are the images for each area:

![image1](https://github.com/foscanit/project-3/blob/main/images/grey.png)

![image2](https://github.com/foscanit/project-3/blob/main/images/blue.png)

![image3](https://github.com/foscanit/project-3/blob/main/images/green.png)

![image4](https://github.com/foscanit/project-3/blob/main/images/purple.png)


As you can see, the last image shows three circles where most of the sites are located. 

![image5](https://github.com/foscanit/project-3/blob/main/images/three%20circles.png)


# In Conclusion

After analyzing the seven areas, I realized that the best coordinates would be 35.656467, 139.734424: when merging the three circles above (yellow, red and orange) and using the Pet House Hara as a central point from which all the important sites are close within a radius of 900 metres: a videgame company, a tech startup, two vegan places, two starbucks, two metro stations, three karaokes and two elementary schools.

See the image with the legend:

![image6](https://github.com/foscanit/project-3/blob/main/images/legend.png)


# Next steps

In order to uphold my decision in an even more accurate way, the ideal following steps would be to insert my data (all the csv files created) into MongoDB making a collection for each dataset and also creating 2dsphere indexes. After that, make more geoqueries to calculate the distances between all the sites and the tech companies. With the results of these geoqueries, we could sort the distances and analyze again which is the best spot in Tokyo for our company and check if it coincides with the previous choice. 


# Sources

https://immigrantinvest.com/insider/best-cities-to-raise-a-family-2021-en/
https://location.foursquare.com/developer/reference/place-search
https://fontawesome.com/v4/icons/
