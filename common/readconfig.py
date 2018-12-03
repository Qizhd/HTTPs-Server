import json, os

def readFile(path):
    with open(path, "r") as f:
        data = json.loads(f.read())
        return data

class ReadConfigFile:
    def __init__(self, fileName):
        self.path = os.getcwd() + "/config/" + fileName + ".json"
        self.data = readFile(self.path)

    def getHead(self):
        self.head = self.data["head"]
        return self.head

    def getBody(self):
        self.body = self.data["body"]
        return self.body

    def getAllDate(self):
        return self.data
