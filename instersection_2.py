import requests

# Define the two coordinates
start_coord = {"lat": 10.759278170362593, "lon": 78.81326494926076}
 
end_coord = {"lat": 10.777865835062338, "lon": 78.79859918760036}

# Define the OSRM server URL
osrm_url = "http://router.project-osrm.org/"

# Find the nearest intersection to the starting coordinate
start_response = requests.get(osrm_url + "nearest/v1/driving/" + f"{start_coord['lon']},{start_coord['lat']}").json()
start_waypoint = start_response["waypoints"][0]["location"]

# Find the nearest intersection to the ending coordinate
end_response = requests.get(osrm_url + "nearest/v1/driving/" + f"{end_coord['lon']},{end_coord['lat']}").json()
end_waypoint = end_response["waypoints"][0]["location"]

# Get the route between the two intersections
route_response = requests.get(osrm_url + "route/v1/driving/" + f"{start_waypoint[0]},{start_waypoint[1]};{end_waypoint[0]},{end_waypoint[1]}").json()

# Extract the coordinates of all four-lane intersections from the route
intersections = []
for step in route_response["routes"][0]["legs"][0]["steps"]:
    if step["intersections"][0]["lanes"] and step["intersections"][0]["lanes"][0]["valid"]:
        # Check if the intersection has at least four lanes
        if len(step["intersections"][0]["lanes"][0]["valid"]) >= 4:
            intersections.append(step["intersections"][0]["location"])

# Print the coordinates of all four-lane intersections

print("These are the intersections")
print(len(intersections))
for intersection in intersections:
    print(intersection)
