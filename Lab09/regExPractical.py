import re

def getFloatData(sensorID):
    with open("sensors.xml") as sensorFile:
        all_lines = sensorFile.readlines()
        sensor_line = "".join(all_lines)
    allSensors = re.findall(r"\s*<{0}>\s*(.*)\s*</{0}>\s*".format(sensorID), sensor_line)
    allSensString = "".join(allSensors)
    allFloat = re.findall(r"[+-]?\d{1,2}\.\d+\b", allSensString, re.IGNORECASE)
    return allFloat

def getScientificData(sensorID):
    with open("sensors.xml") as sensorFile:
        all_lines = sensorFile.readlines()
        sensor_line = "".join(all_lines)
    allSensors = re.findall(r"\s*<{0}>\s*(.*)\s*</{0}>\s*".format(sensorID), sensor_line)
    allSensString = "".join(allSensors)
    allScience = re.findall(r"[+-]?\d\.\d+e[+-]?\d+", allSensString, re.IGNORECASE)
    return allScience

def getOptions(commandline):
    allOptions = re.findall(r"\s*-(\w)\s*([\S]*)", commandline)
    allOptions.sort()
    return allOptions

if __name__ == "__main__":
    print(getFloatData("4IP"))
    print(getScientificData("4IP"))
    print(getOptions("myScript.bash -v    -i 2    -p  /local/bin/somefolder"))
