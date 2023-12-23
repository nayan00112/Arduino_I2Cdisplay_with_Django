import psutil as pu

def getCPUPercent():
    return str(pu.cpu_percent(interval=1))

def getMemoryPercent():
    return str(pu.virtual_memory()).split(",")[2].split("=")[1]