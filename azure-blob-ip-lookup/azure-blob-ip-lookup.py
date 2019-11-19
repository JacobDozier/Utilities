import json

def correctJson(invalidJson):
    """Takes a stringified JSON and adds a parent node and array.
    Also commas in between objects"""

    invalidJson = "{ \"logs\": [ \n" + invalidJson
    invalidJson = invalidJson.replace("}}", "}},")
    invalidJson = invalidJson + "]}\n"
    invalidJson = invalidJson.replace("}},\n]", "}}\n]")
    return invalidJson

# TODO Refactor to search through all files in the various directories under y-2019.
with open("/Users/jdozier/Documents/y=2019/m=10/d=13/h=00/m=00/PT1H.json", "r") as logs:
    stringLogs = logs.read()
    newPT1H = open("/Users/jdozier/Dev/Utilities/PT1H.json", "w")
    newPT1H.write(correctJson(stringLogs))
    newPT1H.close()

# TODO Refactor so that it searches from a list of IP's rather than a hard coded value.
with open("/Users/jdozier/Dev/Utilities/PT1H.json", "r") as validJson:
    jsonString = json.load(validJson)
    for pyObj in jsonString["logs"]:
        if pyObj.get("properties").get("clientIp") == "108.28.120.26":
            print(pyObj)
