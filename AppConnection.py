import json
from Functions import set_script, ws_connect,open_app,get_script

def app_connection(appID):
    print("------------------------------------------------------------")
    print("- 1. Connecting to Qlik Sense Engine JSON")
    print("------------------------------------------------------------")
    ws = ws_connect()
    print(ws.recv())
    print(ws.recv())

    print("------------------------------------------------------------")
    print("- 2. Opening Qlik Sense App ")
    print("------------------------------------------------------------")
    app = open_app(ws,appID)
    result = ws.recv()
    app_json = json.loads(result)
    print(result)
    moving = {'websocket':ws,'json':app_json}
    return moving