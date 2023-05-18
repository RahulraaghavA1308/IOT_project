import gspread #for communication with google sheets
import time
from distance_heading import dist_head_func
from waypoints import waypoints_func

distance_threshold = 150

# lat = ["10.767239457109996",
# "10.766775729253428",
# "10.766433222745475",
# "10.765969340347745",
# "10.765117400630272",
# "10.764604451465264",
# "10.764176249748061",
# "10.763703442990051",
# "10.763404593051687"]

# lon = ["78.81308824774013",
# "78.81306742253017",
# "78.81306395166239",
# "78.81305425908833",
# "78.81303155744583",
# "78.81308604138432",
# "78.81310420269602",
# "78.8131178236815",
# "78.81312690433884",
# "78.81314506565136"]

lat = ["10.767750920825579",
"10.767239457109996",
"10.766775729253428",
"10.766433222745475",
"10.765969340347745",
"10.765108537902124",
"10.765100954355793",
"10.765222291073236",
"10.765239986007785",
"10.765237458161357"]

lon = ["78.81308824774013",
"78.81306742253017",
"78.81306395166239",
"78.81305425908833",
"78.81375634986914",
"78.81426325703913",
"78.8150223312253",
"78.81602585303285",
"78.8172738224584",
"78.81802517724873"]





def sendData(sheetname,datacell,data):
	gc = gspread.service_account(filename='main\client_secret.json')
	wks = gc.open(sheetname).sheet1
	wks.update(datacell,[[data]])

def recieveData(sheetname,datacell):
	gc = gspread.service_account(filename='main\client_secret.json')
	wks = gc.open(sheetname).sheet1
	output = wks.get(datacell)
	return output[0][0]
	
#Sending the value 11 to the google sheet at data cell "A1"
hospital = [10.762875348744194, 78.81845890476383]


sendData('IoT_NITT_Project','E2',str(lat[0]))
sendData('IoT_NITT_Project','F2',str(lon[0]))
sendData('IoT_NITT_Project','E3',str(hospital[0]))
sendData('IoT_NITT_Project','F3',str(hospital[1]))
sendData('IoT_NITT_Project','E6',"150 metres")


# signal = [10.76300318896086, 78.81316143827202]

signal = [10.765099361230686, 78.81308721616251]


sendData('IoT_NITT_Project','E9',str(signal[0]))
sendData('IoT_NITT_Project','F9',str(signal[1]))


# print('B'+str)
prev = 10000

for i in range(10):
    print("***",end=" ")
    wp = waypoints_func(lat[i],lon[i],hospital[0],hospital[1])
    sendData('IoT_NITT_Project','A'+str(i+2),lat[i])
    sendData('IoT_NITT_Project','B'+str(i+2),lon[i])
    sendData('IoT_NITT_Project','E5',lat[i])
    sendData('IoT_NITT_Project','F5',lon[i])

    distance, ret = dist_head_func(float(lat[i]),float(lon[i]),float(signal[0]),float(signal[1]))
    
    sendData('IoT_NITT_Project','E7',str(round(distance,2))+" metres")
    
    if(distance < distance_threshold and prev > distance):
        sendData('IoT_NITT_Project','H'+str(i+2),"YES")
        prev = distance
    else:
        sendData('IoT_NITT_Project','H'+str(i+2),"NO")

    # time.sleep(0.1)


#Receiving whatever data is present at data cell "A1"
# print(recieveData('IoT_NITT_Project','A2'))