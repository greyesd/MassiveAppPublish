import json
import os
from AppConnection import app_connection
from Functions import do_save, set_script,get_script
from fileSecurity import decrypt, load_key, write_key

def UnhideAppScript(moving):
    filename = moving['json']["result"]["qReturn"]["qGenericId"]
    ws = moving['websocket']

    print("------------------------------------------------------------")
    print("- Getting App Script from " + filename + ".bin")
    print("------------------------------------------------------------")
    app_script = get_script(ws)
    result = ws.recv()
    #print(result)
    print("Done")
    script_json = json.loads(result)
    current_script = script_json["result"]["qScript"]
    #with open(filename + ".bin", "r") as file:
    #    script = file.read()
    #file.close()
    
    if os.path.exists("key.key"):
        key = load_key()
        script = decrypt(filename + ".bin",key).decode("utf-8")
    else:
        write_key()
        key = load_key()
        script = decrypt(filename + ".bin",key).decode("utf-8")
    if "Hidden Script" in current_script:
        print("------------------------------------------------------------")
        print("- Unhidding App Script")
        print("------------------------------------------------------------")
        print(script)
        hidden_app = set_script(ws,script)
        result = ws.recv()
        print(result)
        return ws
    else:
        print("------------------------------------------------------------")
        print("- Unhidding App Script")
        print("------------------------------------------------------------")
        print("Script already unhidden.")
        return ws