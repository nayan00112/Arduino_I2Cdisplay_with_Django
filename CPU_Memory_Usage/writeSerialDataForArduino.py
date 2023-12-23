import serial
import time
from get_cpu_ram_percentage import getCPUPercent, getMemoryPercent

# print(getMemoryPercent())
# print(getCPUPercent())

ser = serial.Serial("COM7", 9600)
try:
    while True:
        # m = str("Memory: "+getMemoryPercent()+"%").encode()
        # ser.write(m)
        # print(m)
        # time.sleep(3)

        # c = str("Processor: "+getCPUPercent()+"%").encode()
        # ser.write(c)
        # print(c)
        # time.sleep(3)

        c = str("CPU: "+getCPUPercent()+"%") 
        m = str("Memory: "+getMemoryPercent()+"%")
        datatosend = f"{c}\n{m}"

        time.sleep(3)
        ser.write(datatosend.encode())
except:
    ser.close()

