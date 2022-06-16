
from Functions import do_publish


def PublishApp(moving,streamID,appName):
    filename = moving['json']["result"]["qReturn"]["qGenericId"]
    ws = moving['websocket']
    print("------------------------------------------------------------")
    print("- Publishing App " + filename + " into Stream " + streamID + " with name " + appName)
    print("------------------------------------------------------------")
    app_publish = do_publish(ws,streamID,appName)
    result = ws.recv()
    print(result)
    return ws