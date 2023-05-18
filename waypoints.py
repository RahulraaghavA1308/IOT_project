import requests
import folium
import json

# Define the start and end coordinates
start_lat, start_lon = 10.768326787577756, 78.813116724416   # Diamond hostel
end_lat, end_lon = 10.762364823965529, 78.81867565936166       # NITT Library

# start_lat, start_lon = 10.759278170362593, 78.81326494926076
# end_lat, end_lon = 10.777865835062338, 78.79859918760036



# Define the OSRM API endpoint and parameters
osrm_url = "http://router.project-osrm.org/route/v1/driving/{},{};{},{}".format(start_lon, start_lat, end_lon, end_lat)
params = {
    "steps": "true",
    "geometries": "geojson",
    "overview":"full"
}

# Make the API request and get the response
response = requests.get(osrm_url, params=params)
response_data = response.json()


# Extract the route geometry from the response
geometry = response_data["routes"][0]["geometry"]

# Extract the coordinates of each waypoint from the response
waypoints = []
for feature in response_data['routes'][0]['geometry']['coordinates']:
    waypoint = {
        "lat": feature[1],
        "lon": feature[0]
    }
    waypoints.append(waypoint)

# Print the list of waypoints
print("Way points generated : ")

#Create a map
map = folium.Map(location=[waypoints[0]["lat"], waypoints[0]["lon"]], zoom_start=10)

# Add the route to the map
folium.GeoJson(geometry).add_to(map)

# Add markers for the waypoints
for wp in waypoints:
    print(wp)
    folium.Marker([wp["lat"], wp["lon"]]).add_to(map)

# Save the map
map.save("index.html")


