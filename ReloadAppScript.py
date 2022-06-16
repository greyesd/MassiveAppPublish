import json
from Functions import do_reload,get_progress,do_save
from HideAppScript import HideAppScript
from UnhideAppScript import UnhideAppScript

def ReloadAppScript(moving):
    #filename = moving['json']["result"]["qReturn"]["qGenericId"]
    #ws = moving['websocket']
    ws = UnhideAppScript(moving)
    print("------------------------------------------------------------")
    print("- Reloading App Data")
    print("------------------------------------------------------------")
    reload = do_reload(ws)
    result = ws.recv()
    print(result)

    inprogress = get_progress(ws)
    result = ws.recv()
    print(result)

    progress_json = json.loads(result)
    print(progress_json)
    progress = progress_json["result"]["qProgressData"]["qFinished"]
    print(progress)
    while progress is False:
        inprogress = get_progress(ws)
        result = ws.recv()
        print(result)
        progress_json = json.loads(result)
        print(progress_json)
        progress = progress_json["result"]["qProgressData"]["qFinished"]
        total = progress_json["result"]["qProgressData"]["qTotal"]
        print(progress)
        print(total)

    print("------------------------------------------------------------")
    print("- App Saved")
    print("------------------------------------------------------------")
    save = do_save(ws)
    result = ws.recv()
    print(result)

    ws = HideAppScript(moving)
    #result = ws.recv()
    #print(result)
    return ws