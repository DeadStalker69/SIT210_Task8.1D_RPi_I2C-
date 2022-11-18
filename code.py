
import smbus  #library used for I2C communication
import time

sensor = 0x23 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 1lx resolution. Time typically 120ms 
data_register = 0x10

bus = smbus.SMBus(1)  # creating an object of smbus library

def convertToNumber(data):  # converts the hex data recieved from sensor to decimal
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readValue(addr=sensor): # read the output from the BH1750 sensor
  data = bus.read_i2c_block_data(addr,data_register)
  return convertToNumber(data)

def main():

  while True:
    lightLevel=readLight()
    if (lightLevel < 50):
        print("Too dark")
    
    if (lightLevel > 50 and lightLevel < 150):
        print("Dark")
    
    if (lightLevel > 150 and lightLevel < 300):
        print("Medium Brightness")
    
    if (lightLevel > 300 and lightLevel < 700):
        print("Bright")
    
    if (lightLevel > 700):
        print("Too bright")
        
    time.sleep(0.5)

main()
