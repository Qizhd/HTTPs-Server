#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import init
from common import serverlog
import ssl, json, re, sys

DEFAULT_IP = "localhost"
DEFAULT_PORT = 9443
SERVER_KEYFILE_PATH = "certification/server.pem"
HTTP_VERSION = "HTTP/1.1"

log = serverlog.ServerLog()
globalHandlerObjPost, globalHandlerObjGet, globalHandlerObjDelete, globalHandlerObjPut = init.initObj()
objRePost, objReGet, objReDelete, objRePut = init.initURL()


class ESRSHTTPRequestHandler(BaseHTTPRequestHandler):
    def set_headers(self, head, contentLen):
        for key in head:
            if "errorCode" == str(key):
                self.send_response(int(head["errorCode"]))
            else:
                self.send_header(key, head[key])
        self.send_header("Content-Length", contentLen)
        self.end_headers()

    def do_POST(self):
        head = self._parseHead(self.headers.headers)
        body = self._parseBody()
        try:
            insName, url = self._matchUrl(objRePost, self.path)
            ins = globalHandlerObjPost[insName]

            log.out("do_POST:receive:URL " + self.path + "\n" + "do_POST:receive:URL_RE " + json.dumps(url) + "\n" + "do_POST:receive:ins " + str(ins) + "\n" + "do_POST:receive:head " + str(head) + "\n" + "do_POST:receive:body " + body)

            sendHead = ins.getHead(url, head, body)
            sendBody = ins.getBody(url, head, body)

            log.out("do_POST:send:head " + json.dumps(sendHead) + "\n" + "do_POST:send:Body " + sendBody + "\n")

            self.set_headers(sendHead, len(sendBody))
            self.wfile.write(sendBody)
        except Exception as e:
            log.out("Error Request." + str(e) + "\n")

    def do_GET(self):
        head = self._parseHead(self.headers.headers)
        body = self._parseBody()
        try:
            insName, url = self._matchUrl(objReGet, self.path)
            ins = globalHandlerObjGet[insName]

            log.out("do_GET:receive:URL " + self.path + "\n" + "do_GET:receive:URL_RE " + json.dumps(url) + "\n" + "do_GET:receive:ins " + str(ins) + "\n" + "do_GET:receive:head " + str(head) + "\n" + "do_GET:receive:body " + body)

            sendHead = ins.getHead(url, head, body)
            sendBody = ins.getBody(url, head, body)

            log.out("do_GET:send:head " + json.dumps(sendHead) + "\n" + "do_GET:send:Body " + sendBody + "\n")

            self.set_headers(sendHead, len(sendBody))
            self.wfile.write(sendBody)
        except Exception as e:
            log.out("Error Request." + str(e) + "\n")

    def do_DELETE(self):
        head = self._parseHead(self.headers.headers)
        body = self._parseBody()
        try:
            insName, url = self._matchUrl(objReDelete, self.path)
            ins = globalHandlerObjDelete[insName]

            log.out("do_DELETE:receive:URL " + self.path + "\n" + "do_DELETE:receive:URL_RE " + json.dumps(url) + "\n" + "do_DELETE:receive:ins " + str(ins) + "\n" + "do_DELETE:receive:head " + str(head) + "\n" + "do_DELETE:receive:body " + body)

            sendHead = ins.getHead(url, head, body)
            sendBody = ins.getBody(url, head, body)

            log.out("do_DELETE:send:head " + json.dumps(sendHead) + "do_DELETE:send:Body " + sendBody + "\n")

            self.set_headers(sendHead,len(sendBody))
            self.wfile.write(sendBody)
        except Exception as e:
            log.out("Error Request." + str(e) + "\n")

    def do_PUT(self):
        head = self._parseHead(self.headers.headers)
        try:
            insName, url = self._matchUrl(objRePut, self.path)
            ins = globalHandlerObjPut[insName]

            log.out("do_PUT:receive:URL " + self.path + "\n" + "do_PUT:receive:URL_RE " + json.dumps(url) + "\n" + "do_PUT:receive:ins " + str(ins) + "\n" + "do_PUT:receive:head " + str(head))

            sendHead = ins.getHead(url, head, "")

            log.out("do_PUT:send:head " + json.dumps(sendHead) + "\n")

            self.set_headers(sendHead, 0)
        except Exception as e:
            log.out("Error Request." + str(e) + "\n")

    def _parseHead(self, head):
        headTmp = {}
        for item in head:
            key = item.split(":")[0].strip()
            value = item.split(":")[1].strip()
            headTmp[key] = value
        return headTmp

    def _parseBody(self):
        if "Content-Length" in self.headers:
            return self.rfile.read(int(self.headers.getheader('Content-Length')))
        else:
            return ""

    def _matchUrl(self, objRe, recvUrlStr):
        url = {}
        isMatch = False
        actionIns = "action_default"
        for action in objRe:
            if isMatch:
                break
            for actionRe in objRe[action]:
                if re.search(actionRe, recvUrlStr):
                    actionIns = action
                    url = re.search(actionRe, recvUrlStr).groupdict()
                    isMatch = True
                    break
        if not isMatch:
            url["serialNumber"] = str.strip(recvUrlStr[2:], "/")[4]
        return actionIns, url


def run(serverClass=HTTPServer, handlerClass=ESRSHTTPRequestHandler, serverIP=DEFAULT_IP, serverPort=DEFAULT_PORT):
    handlerClass.protocol_version = HTTP_VERSION
    httpd = serverClass((serverIP, serverPort), handlerClass)
    try:
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile=SERVER_KEYFILE_PATH, server_side=True)
        print 'ESRS Server Started, Listening IP:Port %s:%d' % (serverIP, serverPort)
        log.logRotate()
        httpd.serve_forever()
    finally:
        log.close()
        httpd.server_close()


helpMsg = """ Usage: python main.py [IP:Port], the default IP:Port is localhost:9443. The support python version is 2.7."""

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if "-h" == sys.argv[1]:
            print helpMsg
        else:
            IPAndPortList = sys.argv[1].split(":")
            if len(IPAndPortList) == 2:
                ip = IPAndPortList[0]
                port = int(IPAndPortList[1])
            else:
                ip = IPAndPortList[0]
                port = DEFAULT_PORT
            run(serverIP=ip, serverPort=port)
    else:
        run()
