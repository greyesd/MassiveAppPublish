import json
import os
from AppConnection import app_connection
from Functions import set_script,get_script
from fileSecurity import encrypt, load_key, write_key

def HideAppScript(moving):
    filename = moving['json']["result"]["qReturn"]["qGenericId"]
    ws = moving['websocket']
    print("------------------------------------------------------------")
    print("- Getting App Script and saving into " + filename + ".bin")
    print("------------------------------------------------------------")
    app_script = get_script(ws)
    result = ws.recv()
    #print(result)
    print("Done")
    script_json = json.loads(result)
    script = script_json["result"]["qScript"]

    if "Hidden Script" in script:
        print("------------------------------------------------------------")
        print("- Hidding App Script")
        print("------------------------------------------------------------")
        print("Script already hidden. Process aborted. Check script file integrity.")
        return ws
    else:
        file = open(filename + ".bin", "w")
        file.write(script)
        file.close()

        if os.path.exists("key.key"):
            key = load_key()
            encrypt(filename + ".bin",key)
        else:
            write_key()
            key = load_key()
            encrypt(filename + ".bin",key)
        
        print("------------------------------------------------------------")
        print("- Hidding App Script")
        print("------------------------------------------------------------")
        hidden_app = set_script(ws,"Hidden Script")
        result = ws.recv()
        print(result)
        return ws