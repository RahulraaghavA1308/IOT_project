import folium
import requests

# Define the list of waypoints
waypoints = [
    {"lat": 37.7749, "lon": -122.4194},
    {"lat": 37.3382, "lon": -121.8863},
    {"lat": 37.7749, "lon": -122.4194},
]

# Define the OSRM server URL
osrm_url = "http://router.project-osrm.org/route/v1/driving/"

# Construct the OSRM request URL
request_url = osrm_url + ";".join([f"{wp['lon']},{wp['lat']}" for wp in waypoints]) + "?geometries=geojson"

# Send the request to OSRM and get the response
response = requests.get(request_url).json()

# Extract the route geometry from the response
geometry = response["routes"][0]["geometry"]

# Create a folium map object
map = folium.Map(location=[waypoints[0]["lat"], waypoints[0]["lon"]], zoom_start=10)

# Add the route to the map
folium.GeoJson(geometry).add_to(map)

# Add markers for the waypoints
for wp in waypoints:
    folium.Marker([wp["lat"], wp["lon"]]).add_to(map)

# Display the map
map.save("index.html")
