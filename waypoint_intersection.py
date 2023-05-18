import requests
import json

# Define the start and end coordinates
start_lat, start_lon = 10.763379188669989, 78.81447607338754    # Diamond hostel
end_lat, end_lon = 10.805527507535956, 78.73786568470108     # hospital

# Define the OSRM API endpoint and parameters
osrm_url = "http://router.project-osrm.org/route/v1/driving/{},{};{},{}".format(start_lon, start_lat, end_lon, end_lat)
params = {
    "steps": "true",
    "geometries": "geojson",
    "annotations": "nodes,segments"
}

# Make the API request and get the response
response = requests.get(osrm_url, params=params)
response_data = response.json()

if response_data is None:
    print("No response")
# Extract the coordinates of each waypoint from the response
waypoints = []
four_lane_intersections = []
for annotation in response_data['routes'][0]['legs'][0]['annotation']:
    if annotation['nodes'] != None:
        for node in annotation['nodes']:
            if node not in waypoints:
                waypoints.append(node)
                if annotation['datasources'][node]['classes'][0] == 'motorway_link':
                    prev_node = annotation['datasources'][node]['in'][0]['node']
                    next_node = annotation['datasources'][node]['out'][0]['node']
                    prev_class = annotation['datasources'][prev_node]['classes'][0]
                    next_class = annotation['datasources'][next_node]['classes'][0]
                    if prev_class == 'motorway' and next_class == 'motorway':
                        four_lane_intersections.append(node)

# Print the list of waypoints and four lane intersections
print("Waypoints:")
print(json.dumps(waypoints, indent=4))
print("\nFour-lane Intersections:")
print(json.dumps(four_lane_intersections, indent=4))


# In this script, we first define the start and end coordinates as start_lat, start_lon, end_lat, and end_lon. Then we construct the OSRM API endpoint by substituting 
# these coordinates into the URL template. We also specify three query parameters: steps, geometries, and annotations. The steps parameter tells OSRM to return a list
# of all the waypoints along the route, the geometries parameter specifies the format of the geometry data returned by the API, and the annotations parameter tells OSRM 
# to return additional data about the route, including the nodes and segments along the route.

# We then make the API request using the requests.get() method, passing in the API endpoint URL and the query parameters. We convert the response from JSON format to a 
# Python dictionary using the response.json() method.

# Next, we extract the coordinates of each waypoint from the response by iterating over the annotation array of the leg object in the response. We check if the nodes 
# field of the annotation is not None, and if it's not, we iterate over the nodes array and append each node to the waypoints list.

# We also check if the node is a four-lane intersection by looking at the classes of the adjacent nodes. If the node is a motorway_link and its adjacent nodes are both 
# motorway classes, we append the node to the four_lane_intersections list.

# Finally, we print out the lists of waypoints and four-lane intersections using the json.dumps() method to format the output as JSON with indentation for readability