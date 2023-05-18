# To calculate the distance and heading between two GPS coordinates, you can use the Haversine formula for distance and the Vincenty formula for heading. 
# Here's a Python script that demonstrates how to do this:

import math

# Define the two GPS coordinates
lat1, lon1 = 10.75955914912064, 78.8106141993423 # orion lecture hall complex
# lat2, lon2 = 10.758892948712363, 78.81064533807452 # 180 degrees
# lat2, lon2 = 10.759563679656337, 78.81184924154879  # 90 degrees
lat2, lon2 = 10.759568799734142, 78.81011374433265  # 270 degrees or -90 degrees

# Define some constants
R = 6371000  # radius of Earth in meters

# Convert latitudes and longitudes to radians
lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)

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

# Print the distance and heading
print("Distance: {:.2f} meters".format(distance))
print("Heading: {:.2f} degrees".format(heading))


# In this script, we first define the two GPS coordinates as lat1, lon1, lat2, and lon2. We also define the radius of the Earth in meters as R.

# We then convert the latitudes and longitudes from degrees to radians using the math.radians() function.

# Next, we calculate the distance between the two points using the Haversine formula, which takes into account the curvature of the Earth. 
# The formula involves calculating the difference in latitude and longitude between the two points, and then using these differences to calculate 
# the distance using trigonometric functions.

# Finally, we calculate the heading between the two points using the Vincenty formula, which also takes into account the curvature of the Earth. 
# The formula involves calculating the difference in longitude and latitude between the two points, and then using these differences to calculate 
# the heading using trigonometric functions.

# We print out the distance and heading using the print() function, formatting the output to two decimal places for readability.

