
import os

GLB_name = "test.txt"

def CheckError(name):
    try:
        open (name, "r")
        return 0
    except FileNotFoundError:
        print ("Error: file does not found")
        return 1

def RPubFile():
    if CheckError(GLB_name) == 0:
        file = open(GLB_name, "r")
        while True:
            line = file.readline()
            if not line:
                break
            command = "mosquitto_pub -t test -m " + '"' + line + '"'
            res = os.system(command)
            print ("Returned Value: ", res)
        file.close()

if __name__ == "__main__":
    RPubFile()