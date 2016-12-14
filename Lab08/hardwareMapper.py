from moduleTasks import *

def mapHardwareLine(line):
    try:
        parsedLine = parseLine(line)
        VHDList = []
        for tup in parsedLine[2]:
            VHDList.append("{}=>{}".format(tup[0], tup[1]))
        VHDStr = ", ".join(VHDList)
        return "{}: {} PORT MAP({});".format(parsedLine[1], parsedLine[0], VHDStr)
    except:
        return "Error: Bad Line."

def mapFile(sourceFile, targetFile):
    with open(sourceFile) as readFile:
        indiLine = readFile.readlines()
    with open(targetFile, "w") as saveFile:
        for line in indiLine:
             saveFile.write(mapHardwareLine(line)+"\n")

if __name__ == "__main__":
    #print(mapHardwareLine(" OAI22X1 ( .A(n32), .B(n5), .C(n3), .D(n6), .Y(n25) )"))
    mapFile("verilog_test.v", "something2.vhdl")
    #print("yeah man")