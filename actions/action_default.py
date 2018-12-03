import copy
from common import readconfig, commonapi


class DefaultAction:
    def __init__(self, configFile):
        self.ActionConfig = readconfig.ReadConfigFile(configFile)
        self.head = self.ActionConfig.getHead()
        self.body = self.ActionConfig.getBody()

    def getBody(self, url, head, body):
        return ""

    def getHead(self, url, head, body):
        res = commonapi.replaceArgs(copy.deepcopy(self.head), url, head, body)
        return res
