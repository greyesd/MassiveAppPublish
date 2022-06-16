
from AppConnection import app_connection
from HideAppScript import HideAppScript
from PublishApp import PublishApp
from ReloadAppScript import ReloadAppScript
from ReplaceApp import ReplaceApp
from UnhideAppScript import UnhideAppScript


def main():
    print("0. Exit")
    print("1. Hide App (Not published)")
    print("2. Unhide App (Not published)")
    print("3. Reload App")
    print("4. Publish App")
    print("5. Massive App Publish (No need to hide)")
    print("6. Massive App Publish (Hidding)")
    #print("6. Massive App Hidding")
    print("Select Action:")
    option = input()
    return option

def appInfo(i):
    if i==1:
        print("Introduce appID:")
        appID = input()
        return appID
    elif i==2:
        print("Introduce the appID you want to publish:")
        appID = input()
        return appID
    else:
        print("Introduce the list of appID you want to replace:")
        appID = input()
        return appID

def streamInfo():
    print("Introduce streamID:")
    streamID = input()
    return streamID

def appName():
    print("Introduce App Name:")
    appName = input()
    return appName

if __name__ == "__main__":
    option = "Yes"
    while option!="0" and option is not None:
        option = main()
        if option=="1":
            '''appID = appInfo(1)
            moving = app_connection(appID)
            if "result" in moving["json"].keys():
                ws = HideAppScript(moving)
                ws.close()
            else:
                print(moving["json"]["error"]["message"])'''
        elif option=="2":
            '''appID = appInfo(1)
            moving = app_connection(appID)
            if "result" in moving["json"].keys():
                ws = UnhideAppScript(moving)
                ws.close()
            else:
                print(moving["json"]["error"]["message"])'''
        elif option=="3":
            '''appID = appInfo(1)
            moving = app_connection(appID)
            if "result" in moving["json"].keys():
                ws = ReloadAppScript(moving)
                ws.close()
            else:
                print(moving["json"]["error"]["message"])'''
        elif option=="4":
            '''appID = appInfo(1)
            streamID = streamInfo()
            appName = appName()
            moving = app_connection(appID)
            if "result" in moving["json"].keys():
                ws = PublishApp(moving,streamID,appName)
                ws.close()
            else:
                print(moving["json"]["error"]["message"])'''
        elif option=="5":
            sourceAppID = appInfo(2)
            moving = app_connection(sourceAppID)
            with open("MassiveAppPublish.txt","r") as apps:
                for lines in apps:
                    targetAppID=lines.rstrip('\n')
                    ws = ReplaceApp(moving,option,sourceAppID,targetAppID)
                ws.close()
        elif option=="6":
            '''sourceAppID = appInfo(2)
            moving = app_connection(sourceAppID)
            with open("MassiveAppPublish.txt","r") as apps:
                for lines in apps:
                    targetAppID=lines.rstrip('\n')
                    ws = ReplaceApp(moving,option,sourceAppID,targetAppID)
                ws.close()'''
        elif option=="0":
            print("The End.")
        else:
            print("Invalid option.")