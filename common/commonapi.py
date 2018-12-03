import uuid, json


def getDeviceKey():
    return str(uuid.uuid1().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex) + str(uuid.uuid4().hex)


def replaceArgs(des, url, head, body):
    if body != "" and body is not None:
        body = json.loads(body)
    for key in des:
        if str(des[key]) == "#":
            if url.has_key(key):
                des[key] = url[key]
            elif head.has_key(key):
                des[key] = head[key]
            elif body.has_key(key):
                des[key] = body[key]
            else:
                des[key] = ""
    return des
