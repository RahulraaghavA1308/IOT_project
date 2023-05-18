
import math

def dist_head_func(start_lat, start_lon, end_lat, end_lon):
    R = 6371000 # radius of Earth in meters
    lat1_rad = math.radians(start_lat)
    lon1_rad = math.radians(start_lon)
    lat2_rad = math.radians(end_lat)
    lon2_rad = math.radians(end_lon)

    # Calculate the distance between the two points using the Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad)*math.cos(lat2_rad)*math.sin(dlon/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R*c

    # Calculate the heading between the two points using the Vincenty formula
    y = math.sin(lon2_rad-lon1_rad)*math.cos(lat2_rad)
    x = math.cos(lat1_rad)*math.sin(lat2_rad)-math.sin(lat1_rad)*math.cos(lat2_rad)*math.cos(lon2_rad-lon1_rad)
    heading = math.degrees(math.atan2(y, x))

    return distance, heading

