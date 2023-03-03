import json


class DataJson:
    def __init__(self):
        self.input = None
        self.output = None

    def getInput(self):
        try:
            with open("conf.json") as load:
                fieldJson = json.load(load)
                self.input = fieldJson["input"]
                self.output = fieldJson["output"]

            return "OK"
        except:
            return "Error"

    def setInput(self, json_object):
        try:
            with open("conf.json", "w") as outfile:
                outfile.write(json_object)

            return "OK"
        except:
            return "Error"
