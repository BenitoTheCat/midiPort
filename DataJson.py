import json


class DataJson:
    def __init__(self):
        self.input = None
        self.output = None
        self.setting = {"input": self.input, "output": self.output}
        self.loadSetting()

    def loadSetting(self):
        try:
            with open("conf.json") as load:
                fieldJson = json.load(load)
                self.input = fieldJson["input"]
                self.output = fieldJson["output"]
                self.setting = {"input": self.input, "output": self.output}

            return "OK"
        except:
            self.input = None
            self.output = None
            self.setting = {"input": self.input, "output": self.output}
            return "Error"

    def setSetting(self, json_object):
        try:
            with open("conf.json", "w") as outfile:
                outfile.write(json_object)

            return "OK"
        except:
            return "Error"

    def getSetting(self):
        return self.setting

    def getInput(self):
        return self.input

    def getOutput(self):
        return self.output
