
from Functions import do_replace, ws_connect
from HideAppScript import HideAppScript
from UnhideAppScript import UnhideAppScript


def ReplaceApp(moving,option,sourceAppID,targetAppID):
    ws = moving['websocket']
    if option=="6":
        moving['json']["result"]["qReturn"]["qGenericId"]=targetAppID
        ws = HideAppScript(moving)
    print("------------------------------------------------------------")
    print("- Replacing App " + targetAppID + " with App " + sourceAppID)
    print("------------------------------------------------------------")
    app_publish = do_replace(ws,sourceAppID,targetAppID)
    result = ws.recv()
    print(result)
    if option=="6":
        ws = UnhideAppScript(moving)
    return ws