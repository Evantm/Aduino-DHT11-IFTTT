import serial #serial communication
import time #for waiting
from ISStreamer.Streamer import Streamer #Initial state streaming

try:
    port = serial.Serial('COM5',115200)
except:
    port = serial.Serial('COM5',115200)

time.sleep(3) #gives the arduino time to wake up

streamer = Streamer(bucket_name="IS name here", access_key="IS access key here")

while True:
    read= port.readline()
    try:
        trigger='IFTTT action name'
        IFTTTkey='Enter your ifttt id here'
        read = str(read)
        print(read)
        nums = read.split(',')


        print ('sent')
        payload = { 'value1' : nums[0][2:], 'value2' : nums[1][:-5], 'value3' : 'null'} #value3 is not used. 

        streamer.log("Humid", nums[0][2:])
        streamer.log("Temp", nums[1][:-5])
        
        time.sleep(3) #Time delay so it updates every 3 seconds, could change to update based on temp or humid logic.

    except Exception as e:
        print (e) #for 

