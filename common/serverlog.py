import os
from datetime import datetime
from threading import Timer

class ServerLog:
    def __init__(self, logPath="ESRSHttpServer.log"):
        self._path = os.getcwd() + "/log/" + logPath
        if not os.path.exists(os.getcwd() + "/log/"):
            os.mkdir("log")
        self._f = open(self._path, "a")

    def out(self, *args):
        for i in args:
            outStr = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + str(i) + "\n")
            self._f.write(outStr)
            self._f.flush()

    def logRotate(self):
        if os.path.exists(self._path) and os.path.getsize(self._path) >= 5 * 1024 * 1024:
            os.rename(self._path, os.getcwd() + "/log/" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ".log")
            os.mknod(self._path)

        Timer(5 * 24 * 60 * 60, self.logRotate, ()).start()

    def close(self):
        self._f.close()