from PIL import Image, ImageColor, ImageOps, ImageFilter
from skimage import color
import os
import imageio
import numpy as np
import pandas as pd
from geopy.distance import geodesic, pi, EARTH_RADIUS, cos, sin

# get map images and np arrays
maps = {}
for name in os.listdir('Slum Maps/original'):
    image = Image.open(f'Slum Maps/original/{name}')
    maps[f"{name.split('_')[0]}_original"] = image

for name in os.listdir('Slum Maps/grayscale'):
    image = Image.open(f'Slum Maps/grayscale/{name}')
    maps[f"{name.split('_')[0]}_grayscale"] = image

# defining a distance function
def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**.5

# ——————————————————————
# RIO DE JENEIRO
# ——————————————————————

# lattitude and Longitude reference points
rio_origin_lat_long = (-22.73094444, -43.83611111)
rio_edge_lat_long = (-23.17808056, -43.03277778)

# Pixel coordinate refrence points
rio_origin_coords = (0, 0)
rio_edge_coords = (536, 960)

# getting real world component and total distances between refrence points
rio_total_dist_lat_long = geodesic(rio_origin_lat_long, rio_edge_lat_long).kilometers
rio_y_dist_lat_long = geodesic(rio_origin_lat_long, (rio_edge_lat_long[0], rio_origin_lat_long[1])).kilometers
rio_x_dist_lat_long = geodesic(rio_origin_lat_long, (rio_origin_lat_long[0], rio_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
rio_total_dist_coords = distance(rio_origin_coords,rio_edge_coords)
rio_y_dist_coords = distance(rio_origin_coords, (rio_edge_coords[0], rio_origin_coords[1]))
rio_x_dist_coords = distance(rio_origin_coords, (rio_origin_coords[0], rio_edge_coords[1]))

# getting conversion between x distance in pixels to km
rio_x_factor = rio_x_dist_lat_long / rio_x_dist_coords
# getting conversion between y distance in pixels to km
rio_y_factor = -rio_y_dist_lat_long / rio_y_dist_coords


# defining a function to get lattitude and longitude prom pixel coordinates
def rio_get_lat_long(coord):
    y = coord[1] * rio_y_factor
    x = coord[0] * rio_x_factor
    lat  = rio_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = rio_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(rio_origin_lat_long[0] * pi/180)
    return (lat, long)

# ——————————————————————
# MUMBAI
# ——————————————————————

# lattitude and Longitude reference points
mumbai_origin_lat_long = (19.28103056, 72.77083333)
mumbai_edge_lat_long = (18.88450000, 72.98388889)
# Pixel coordinate refrence points
mumbai_origin_coords = (0, 0)
mumbai_edge_coords = (8000, 4000)

# getting real world component and total distances between refrence points
mumbai_total_dist_lat_long = geodesic(mumbai_origin_lat_long, mumbai_edge_lat_long).kilometers
mumbai_y_dist_lat_long = geodesic(mumbai_origin_lat_long, (mumbai_edge_lat_long[0], mumbai_origin_lat_long[1])).kilometers
mumbai_x_dist_lat_long = geodesic(mumbai_origin_lat_long, (mumbai_origin_lat_long[0], mumbai_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
mumbai_total_dist_coords = distance(mumbai_origin_coords,mumbai_edge_coords)
mumbai_y_dist_coords = distance(mumbai_origin_coords, (mumbai_edge_coords[0], mumbai_origin_coords[1]))
mumbai_x_dist_coords = distance(mumbai_origin_coords, (mumbai_origin_coords[0], mumbai_edge_coords[1]))

# getting conversion between x distance in pixels to km
mumbai_x_factor = mumbai_x_dist_lat_long / mumbai_x_dist_coords
# getting conversion between y distance in pixels to km
mumbai_y_factor = -mumbai_y_dist_lat_long / mumbai_y_dist_coords

def mumbai_get_lat_long(coord):  
    y = coord[1] * mumbai_y_factor
    x = coord[0] * mumbai_x_factor
    lat  = mumbai_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = mumbai_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(mumbai_origin_lat_long[0] * pi/180)
    return (lat, long)


# ——————————————————————
# HYDERABAD
# ——————————————————————

# lattitude and Longitude reference points
hyderabad_origin_lat_long = (17.57938611, 78.21666667)
hyderabad_edge_lat_long = (17.26456111, 78.65083333)
# Pixel coordinate refrence points
hyderabad_origin_coords = (0, 0)
hyderabad_edge_coords = (1283, 1800)

# getting real world component and total distances between refrence points
hyderabad_total_dist_lat_long = geodesic(hyderabad_origin_lat_long, hyderabad_edge_lat_long).kilometers
hyderabad_y_dist_lat_long = geodesic(hyderabad_origin_lat_long, (hyderabad_edge_lat_long[0],hyderabad_origin_lat_long[1])).kilometers
hyderabad_x_dist_lat_long = geodesic(hyderabad_origin_lat_long, (hyderabad_origin_lat_long[0], hyderabad_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
hyderabad_total_dist_coords = distance(hyderabad_origin_coords,hyderabad_edge_coords)
hyderabad_y_dist_coords = distance(hyderabad_origin_coords, (hyderabad_edge_coords[0], hyderabad_origin_coords[1]))
hyderabad_x_dist_coords = distance(hyderabad_origin_coords, (hyderabad_origin_coords[0], hyderabad_edge_coords[1]))

# getting conversion between x distance in pixels to km
hyderabad_x_factor = hyderabad_x_dist_lat_long / hyderabad_x_dist_coords
# getting conversion between y distance in pixels to km
hyderabad_y_factor = -hyderabad_y_dist_lat_long / hyderabad_y_dist_coords

def hyderabad_get_lat_long(coord):
    y = coord[1] * hyperbad_y_factor
    x = coord[0] * hyperbad_x_factor
    lat  = hyderabad_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = hyderabad_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(hyderabad_origin_lat_long[0] * pi/180)
    return (lat, long)

def get_pixel_coords(city, coord):
    
    if city == 'rio':
        y = (coord[0] - rio_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  rio_origin_lat_long[1]) * cos(rio_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        x = int(np.round(x / rio_x_factor))
        y = int(np.round(y / rio_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
            
        if x > rio_edge_coords[1]-1:
            x =  rio_edge_coords[1]-1
        if y >  rio_edge_coords[0]-1:
            y =  rio_edge_coords[0]-1
        
        return (x,y)
    
    
    elif city == 'mumbai':
        y = (coord[0] - mumbai_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  mumbai_origin_lat_long[1]) * cos(mumbai_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        x = int(np.round(x / mumbai_x_factor))
        y = int(np.round(y / mumbai_y_factor))

        if x < 0:
            x = 0
        if y < 0:
            y = 0
            
        if x > mumbai_edge_coords[1]-1:
            x = mumbai_edge_coords[1]-1
        if y > mumbai_edge_coords[0]-1:
            y = mumbai_edge_coords[0]-1
        
        return (x,y)
    
    
    elif city == 'hyderabad':
        
        y = (coord[0] - hyderabad_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  hyderabad_origin_lat_long[1]) * cos(hyderabad_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        
        x = int(np.round(x / hyderabad_x_factor))
        y = int(np.round(y / hyderabad_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        
        
        if x > hyderabad_edge_coords[1]-1:
            x = hyderabad_edge_coords[1]-1
        if y > hyderabad_edge_coords[0]-1:
            y = hyderabad_edge_coords[0]-1
        
        return (x,y)
        
    
    else:
        print("Error Invalid City, Valid Cities are rio, mumbai")


def get_slum_val(city, coord):
    
    pixel_coords = get_pixel_coords(city=city, coord=coord)
    
    if city == 'rio':
        if np.array(maps['rio_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1
        
    elif city == 'mumbai':
        if np.array(maps['mumbai_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1
    elif city == 'hyderabad':
        if np.array(maps['hyderabad_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1