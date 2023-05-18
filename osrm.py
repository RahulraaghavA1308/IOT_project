import requests
import json
import overpy
import folium

osrm_url = "http://router.project-osrm.org/route/v1/driving/"




def get_shortest_path(lat1, lon1, lat2, lon2):
    # Use OSRM to find the shortest path
    url = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"
    response = requests.get(url)
    try:
        response.raise_for_status()
        route = json.loads(response.content)["routes"][0]["geometry"]["coordinates"]
        for i in route:
            print(i[1],end=',')
            print(i[0])
        return route
    except (requests.exceptions.HTTPError, IndexError, KeyError) as e:
        print(f"Error getting shortest path: {e}")
        print(response.content)
        return None

def get_intersections(route):
    # Use Overpass API to get all intersections with at least 4 lanes along the route
    api = overpy.Overpass()
    nodes = api.query(f"""
        way["highway"~"^(primary|secondary|tertiary|unclassified|residential|service)$"]
        (around:0.001,{route[0][1]},{route[0][0]});
        (
            node["highway"~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|service)$"]
            ["lanes"~"^[4-9]|10$"]
            (around:0.001,{route[0][1]},{route[0][0]});
            node["highway"~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|service)$"]
            ["lanes"~"^[4-9]|10$"]
            (around:0.001,{route[-1][1]},{route[-1][0]});
        );
        out;
    """).nodes
    return [(node.lat, node.lon) for node in nodes]

def create_map(route):
    request_url = osrm_url + ";".join([f"{wp[1]},{wp[0]}" for wp in route]) + "?geometries=geojson"
    response = requests.get(request_url).json()
    # Extract the route geometry from the response
    geometry = response["routes"][0]["geometry"]
    # Create a folium map object
    map = folium.Map(location=[route[0][1], route[0][0]], zoom_start=10)
    # Add the route to the map
    folium.GeoJson(geometry).add_to(map)

    # Add markers for the waypoints
    for wp in route:
        folium.Marker([wp[1], wp[0]]).add_to(map)
    
    print("Map saved as index.html")
    # Display the map
    map.save('index.html')



# Example usage
lat1, lon1 = 10.763379188669989, 78.81447607338754    # Diamond hostel
# lat2, lon2 = 10.757355527717523, 78.81823453408565    # NITT Library

lat2, lon2 = 10.805527507535956, 78.73786568470108     # hospital

route = get_shortest_path(lat1, lon1, lat2, lon2)

create_map(route=route)




if route is not None:
    print("These are the intersections")
    intersections = get_intersections(route)
    print(intersections)
