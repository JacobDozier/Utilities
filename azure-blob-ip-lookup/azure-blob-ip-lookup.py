import json
import os

# File paths
blobPath = "/Users/jdozier/Documents/y=2019/m={}/d={}/h={}/m=00/PT1H.json"
correctedJsonPath = "/Users/jdozier/Dev/Utilities/azure-blob-ip-lookup/PT1H-corrected.json"
errorLogsPath = "/Users/jdozier/Dev/Utilities/azure-blob-ip-lookup/errorLogs.txt"
outputPath = "/Users/jdozier/Dev/Utilities/azure-blob-ip-lookup/PT1H.json"

# Working vars
output = []
totalLogs = ""

def correctJson(invalidJson):
    """Takes a stringified JSON and adds a parent node and array.
    Also adds commas in between objects."""
    invalidJson = "{ \"logs\": [ \n" + invalidJson
    invalidJson = invalidJson.replace("}}", "}},")
    invalidJson = invalidJson + "]}\n"
    invalidJson = invalidJson.replace("}},\n]", "}}\n]")
    return invalidJson

def deleteFile(pathToFile):
    """Deletes the file from the passed absolute pathway."""
    try:
        os.remove(pathToFile)
    except:
        pass

def appendToFile(appendFilePath, toAppend):
    """Takes a file path and variable to append. Converts passed variable to a string."""
    try:
        appendFile = open(appendFilePath, "a")
        appendFile.write(str(toAppend))
        appendFile.write("\n")
        appendFile.close()
    except Exception as appendError:
        print(appendError)

def writeToFile(writeFilePath, toWrite):
    """Takes a file path and variable to write. Converts passed variable to a string."""
    try:
        writeFile = open(writeFilePath, "w")
        writeFile.write(str(toWrite))
        writeFile.close()
    except Exception as writeError:
        appendToFile(writeFilePath, writeError)

# TODO Refactor so that it searches from a list of IP's rather than a hard coded value.
if __name__ == '__main__':
    deleteFile(errorLogsPath)
    deleteFile(outputPath)

    for month in range(1, 13):
        for day in range(1, 32):
            for hour in range(24):
                try:
                    with open(blobPath.format(str(month).zfill(2), str(day).zfill(2), str(hour).zfill(2)), "r") as logs:
                        stringLogs = logs.read()
                        totalLogs += stringLogs
                except OSError as jsonCorrectionErr:
                    appendToFile(errorLogsPath, jsonCorrectionErr)
                except Exception as e:
                    appendToFile(errorLogsPath, e)

    jsonDict = json.loads(correctJson(totalLogs))
    for pyObj in jsonDict["logs"]:
        if pyObj.get("properties").get("clientIp") == "221.235.236.196":
            output.append(pyObj)
            print(pyObj)

    writeToFile(outputPath, json.dumps(output))
