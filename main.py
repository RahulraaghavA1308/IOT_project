import math
import gspread
import time
import os
import webbrowser
from waypoints import waypoints_func


from distance_heading import dist_head_func

def sendData(sheetname,datacell,data):
	gc = gspread.service_account(filename='main\client_secret.json')
	wks = gc.open(sheetname).sheet1
	wks.update(datacell,[[data]])

def recieveData(sheetname,datacell):
	gc = gspread.service_account(filename='main\client_secret.json')
	wks = gc.open(sheetname).sheet1
	output = wks.get(datacell)
	return output[0][0]



def calc_bearing(lat1, long1, lat2, long2):
  # Convert latitude and longitude to radians
  lat1 = math.radians(lat1)
  long1 = math.radians(long1)
  lat2 = math.radians(lat2)
  long2 = math.radians(long2)
  
  # Calculate the bearing
  bearing = math.atan2(
      math.sin(long2 - long1) * math.cos(lat2),
      math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(long2 - long1)
  )
  
  # Convert the bearing to degrees
  bearing = math.degrees(bearing)
  
  # Make sure the bearing is positive
  bearing = (bearing + 360) % 360
  
  return bearing


distance_threshold = 100

# Starting coordinate will be ambulance coordinate
# Get starting coordinate from google sheet
# ending cordinate will be hardcoded to an hospital

start_lat, start_lon = 10.763379188669989, 78.81447607338754    # Diamond hostel
end_lat, end_lon = 10.757355527717523, 78.81823453408565        # NITT Library


print(" ")
print(" ")

print("-------------------------------------------------------------")
print("        GREEN CORRIDOR FOR AMBULANCE USING IOT               ")
print("-------------------------------------------------------------")   

print(" ")
print(" ")

i = 0

while True:
    i = i + 1
    flag = False
    print(f'*** Iteration : { i }')

    W = waypoints_func(start_lat, start_lon, end_lat, end_lon)

    file_path = "D:\Rahul\College\A_Semester_6\IOT_project\Code\main\maps\index.html"

    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'  # Path to Chrome executable
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(file_path)

    waypoints = []

    for w in W:
        waypoints.append([w["lat"],w["lon"]])

    ###############################################################################
    # Assumming that the traffic junction is hardcoded into this code 
    # we will now consider that the second waypoint returned is the junction
    # So we need to find the distance of ambulance from the second waypoint





    print(f'Ambulance coodinate : {start_lat,start_lon}')
    print(" ")
    print(f'Traffic Junction coodinate : {waypoints[1]}')
    print(" ")
    print(f'Next waypoint coodinate : {waypoints[2]}')
    print(" ")

    distance, ret = dist_head_func(start_lat, start_lon, waypoints[1][0], waypoints[1][1])

    if distance < distance_threshold:
        flag = True
        
    # We will now assume that the third waypoint returned is the waypoint
    # after the signal. This will be used to get the heading of the ambulance 
    # required.

    heading = calc_bearing(start_lat, start_lon, waypoints[2][0], waypoints[2][1])

    print(f'Distance of Ambulance from Traffic Junction : {distance} metres')
    print(" ")
    print(f'Heading of Ambulance after Traffic Junction : {heading} degrees')

    rel_orientation = ''

    if(heading > 130 and heading < 170):
        rel_orientation = 'West-South'
    elif(heading > 170 and heading < 190):
        rel_orientation = 'North-South'
    elif(heading > 190 and heading < 230):
        rel_orientation = 'East-South'
    elif(heading > 230 and heading < 260):
        rel_orientation = 'North-West'
    elif(heading > 260 and heading < 280):
        rel_orientation = 'East-West'
    elif(heading > 280 and heading < 310):
        rel_orientation = 'South-West'
    elif(heading > 10 and heading < 40):
        rel_orientation = 'West-North'
    elif(heading > 350 and heading < 10):
        rel_orientation = 'South-North'
    elif(heading > 310 and heading < 350):
        rel_orientation = 'East-North'
    elif(heading > 40 and heading < 80):
        rel_orientation = 'South-East'
    elif(heading > 80 and heading < 100):
        rel_orientation = 'West-East'
    elif(heading > 100 and heading < 130):
        rel_orientation = 'North-East'

    print(" ")
    print(f'Orientation of Ambulance after the signal : {rel_orientation}')
    print("Updating data in google sheet")
    time.sleep(5)
    print(" ")
    print(" ")