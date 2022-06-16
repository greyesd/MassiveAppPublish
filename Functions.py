import websocket
import ssl
import json

#Websocket Connection
#ws = websocket.create_connection("ws://localhost:4848/app/", header=header_user)
#ws = websocket.create_connection("wss://OPCLOUD-SRV-DEV.solmelia.corp/winauth/app/",header = header_user)
#ws1 = websocket.create_connection("wss://OPCLOUD-SRV-DEV.solmelia.corp/hdr/app/",header_user = {'hdr-usr': 'OPCLOUD-SRV-DEV\qlikservices'})
#print(ws.status)

def ws_connect():
    with open("settings.conf","r") as settings:
        i=0
        for linea in settings:
            if i==0:
                split_line=linea.split("=")
                value_hdr=split_line[1].rstrip('\n')
                i=i+1
            elif i==1:
                split_line=linea.split("=")
                value_usr=split_line[1].rstrip('\n')
                i=i+1
            else:
                split_line=linea.split("=")
                value_host=split_line[1].rstrip('\n')
    header_user = {value_hdr: value_usr}
    ws = websocket.create_connection(value_host, sslopt={"cert_reqs": ssl.CERT_NONE}, header = header_user)
    #header_user = {'hdr-usr': 'SOLMELIA\FDBZ001'}
    #ws = websocket.create_connection("wss://OPCLOUD-SRV-DEV.solmelia.corp/hdr/app/", sslopt={"cert_reqs": ssl.CERT_NONE}, header = header_user)
    return ws

#Open Document with appid

def open_app(ws,appID):
    ws.send(json.dumps({
	"handle": -1,
	"method": "OpenDoc",
	"params": [
        appID
        #"f62c1f44-454e-4f9a-ac95-caab8890a7a3"
        ],
	"id": 2
    }))
    return ws

# Getting App script

def get_script(ws):
    ws.send(json.dumps({
	"handle": 1,
	"method": "GetScript",
	"params": [],
	"id": 2
    }))
    return ws

# Hide App Script

def set_script(ws,script):
    ws.send(json.dumps({
	"handle": 1,
	"method": "SetScript",
	"params": [script],
	"id": 1
    }))
    return ws

# Reload Qlik Sense App

def do_reload(ws):
    ws.send(json.dumps({
	"handle": 1,
	"method": "DoReload",
	"params": [],
	"id": 1
    }))
    return ws

# Get Qlik Sense App Reload Progress

def get_progress(ws):
    ws.send(json.dumps({
	"handle": -1,
	"method": "GetProgress",
	"params": [1],
	"id": 1
    }))
    return ws

# Save Qlik Sense App

def do_save(ws):
    ws.send(json.dumps({
	"handle": 1,
	"method": "DoSave",
	"params": [],
	"id": 1
    }))
    return ws

# Publish Qlik Sense App

def do_publish(ws,streamID,appName):
    ws.send(json.dumps({
    "jsonrpc": "2.0",
    "id": 2,
    "method": "Publish",
    "handle": 1,
    "params": [
        #"b09be8ee-c807-4aa3-8bf6-4cc7729200a8",
        #"Golf Quest_Published"
        streamID,
        appName
    ]
    }))
    return ws

# Publish Qlik Sense App

def do_replace(ws,sourceAppID,targetAppID):
    ws.send(json.dumps({
    "jsonrpc": "2.0",
    "id": 2,
    "method": "ReplaceAppFromID",
    "handle": -1,
    "params": [
        #"b09be8ee-c807-4aa3-8bf6-4cc7729200a8",
        #"Golf Quest_Published"
        targetAppID,
        sourceAppID,
        []
    ]
    }))
    return ws