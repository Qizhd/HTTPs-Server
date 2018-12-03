from actions import action_add, action_status, action_delete, \
    action_keep_alive2, action_download_file, action_connect_home, action_mft_file, action_keep_alive, action_default
from common import readconfig

OBJECT_RE_FILE_NAME = "obj_re"

ADD_ACTION = "action_add"
KEEP_ALIVE_ACTION = "action_keep_alive"
KEEP_ALIVE2_ACTION = "action_keep_alive2"
CONNECT_HOME_ACTION = "action_connect_home"
STATUS_ACTION = "action_status"
DOWNLOAD_FILE_ACTION = "action_download_file"
DELETE_ACTION = "action_delete"
MFT_FILE_ACTION = "action_mft_file"
DEFAULT_ACTION = "action_default"

def initURL():
    objRePost = {}
    objRePut = {}
    objReGet = {}
    objReDelete = {}

    objReConfig = readconfig.ReadConfigFile(OBJECT_RE_FILE_NAME).getAllDate()
    objRePost[ADD_ACTION] = objReConfig["post"]["action_add"]
    objRePost[KEEP_ALIVE_ACTION] = objReConfig["post"]["action_keep_alive"]
    objRePost[KEEP_ALIVE2_ACTION] = objReConfig["post"]["action_keep_alive2"]
    objRePost[CONNECT_HOME_ACTION] = objReConfig["post"]["action_connect_home"]
    objReGet[STATUS_ACTION] = objReConfig["get"]["action_status"]
    objReGet[DOWNLOAD_FILE_ACTION] = objReConfig["get"]["action_download_file"]
    objReDelete[DELETE_ACTION] = objReConfig["delete"]["action_delete"]
    objRePut[MFT_FILE_ACTION] = objReConfig["put"]["action_mft_file"]
    return objRePost, objReGet, objReDelete, objRePut


def initObj():
    globalHandlerObjPost = {}
    globalHandlerObjPut = {}
    globalHandlerObjGet = {}
    globalHandlerObjDelete = {}

    globalHandlerObjPost[ADD_ACTION] = action_add.AddAction("action_add")
    globalHandlerObjPost[KEEP_ALIVE_ACTION] = action_keep_alive.KeepAliveAction("action_keep_alive")
    globalHandlerObjPost[KEEP_ALIVE2_ACTION] = action_keep_alive2.KeepAlive2Action("action_keep_alive2")
    globalHandlerObjPost[CONNECT_HOME_ACTION] = action_connect_home.ConnectHome("action_connect_home")
    globalHandlerObjPost[DEFAULT_ACTION] = action_default.DefaultAction("action_default")
    globalHandlerObjGet[STATUS_ACTION] = action_status.StatusAction("action_status")
    globalHandlerObjGet[DOWNLOAD_FILE_ACTION] = action_download_file.DownloadFileAction("action_download_file")
    globalHandlerObjGet[DEFAULT_ACTION] = action_default.DefaultAction("action_default")
    globalHandlerObjDelete[DELETE_ACTION] = action_delete.DeleteAction("action_delete")
    globalHandlerObjDelete[DEFAULT_ACTION] = action_default.DefaultAction("action_default")
    globalHandlerObjPut[MFT_FILE_ACTION] = action_mft_file.MFTFile("action_mft_file")
    globalHandlerObjPut[DEFAULT_ACTION] = action_default.DefaultAction("action_default")
    return globalHandlerObjPost, globalHandlerObjGet, globalHandlerObjDelete, globalHandlerObjPut
