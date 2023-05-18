import requests
import folium
import json



# Function which takes starting longitude, latitude and 
# ending longitude, latitude and returns the waypoints
def waypoints_func(start_lat, start_lon, end_lat, end_lon):
    # Define the OSRM API endpoint and parameters
    osrm_url = "http://router.project-osrm.org/route/v1/driving/{},{};{},{}".format(start_lon, start_lat, end_lon, end_lat)
    params = {
        "steps": "true",
        "geometries": "geojson"
    }

    response = requests.get(osrm_url, params=params)
    response_data = response.json()
    geometry = response_data["routes"][0]["geometry"]

    waypoints = []
    for feature in response_data['routes'][0]['geometry']['coordinates']:
        waypoint = {
            "lat": feature[1],
            "lon": feature[0]
        }
        waypoints.append(waypoint)

    #Create a map
    map = folium.Map(location=[waypoints[0]["lat"], waypoints[0]["lon"]], zoom_start=17)

    # Add the route to the map
    folium.GeoJson(geometry).add_to(map)

    # Add markers for the waypoints
    for wp in waypoints:
        folium.Marker([wp["lat"], wp["lon"]]).add_to(map)

    # Save the map
    map.save("D:\Rahul\College\A_Semester_6\IOT_project\Code\main\maps\index.html")
    
    return waypoints

