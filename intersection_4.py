import requests
import json
import folium

'''------------------------------------------------------------------'''

'''
Function: returns a route in the form of a list of list
Each list in "route" is a [long,lat] and is a waypoint between source and destination
'''

def get_shortest_path(lat1, lon1, lat2, lon2):
    # Use OSRM to find the shortest path
    url = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"
    response = requests.get(url)
    try:
        response.raise_for_status()
        route = json.loads(response.content)["routes"][0]["geometry"]["coordinates"]
        return route
    #handling eceptions
    except (requests.exceptions.HTTPError, IndexError, KeyError) as e:
        print(f"Error getting shortest path: {e}")
        print(response.content)
        return None

'''------------------------------------------------------------------'''

'''
returns True if the coordinate is a 3 lane intersection
'''
def is_intersection(cordinates):
    # Define the query to retrieve the roads in the vicinity of the point
    query = f"""
    [out:json];
    way
    ["highway"]
    (around: 7, {cordinates[0]}, {cordinates[1]});
    (._;>;);
    out;
    """
    # query = f"""
    # [out:json][timeout:25];
    # // gather results
    # (
    # // query part for: “"traffic signals"”
    # node["highway"="traffic_signals"]({{bbox}});
    # );
    # // print results
    # out body;
    # >;
    # out skel qt;
    # """

    # Send the query to the Overpass API and retrieve the response
    url = "https://overpass-api.de/api/interpreter"
    response = requests.post(url, data=query)

    # Parse the response as JSON and count the number of roads
    data = response.json()
    # num_roads = sum(1 for element in data["elements"] if element["type"] == "way")
    # Return True if the point corresponds to an intersection of at least 4 roads, False otherwise
    return data

'''------------------------------------------------------------------'''

lat1, lon1 = 10.759278170362593, 78.81326494926076
lat2, lon2 = 10.777865835062338, 78.79859918760036
route = get_shortest_path(lat1, lon1, lat2, lon2)

#reversing each elmental list in the list since the request gives the waypoint of the form [long,lat]
for lists in route:
    lists.reverse()

m = folium.Map(location=route[0], zoom_start=15)

for coord in route:
    folium.Marker(location=coord).add_to(m)
m.save('map2.html')


'''Another map for plotting just the 4 lane intesections along the shortest path'''
m2 = folium.Map(location=route[0], zoom_start=15)


#finding if the points in the waypoint contains any 4 lane intersections
for cords in route:
    if(is_intersection(cords)):
        folium.Marker(location=cords).add_to(m2)

m2.save('map3.html')