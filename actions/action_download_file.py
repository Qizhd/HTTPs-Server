import json, copy
from common import readconfig, commonapi


class DownloadFileAction:
    def __init__(self, configFile):
        self.ActionConfig = readconfig.ReadConfigFile(configFile)
        self.head = self.ActionConfig.getHead()
        self.body = self.ActionConfig.getBody()

    def getBody(self, url, head, body):
        # return download file list, this function return empty list
        return json.dumps(copy.deepcopy(self.body))

    def getHead(self, url, head, body):
        res = commonapi.replaceArgs(copy.deepcopy(self.head), url, head, body)
        return res
