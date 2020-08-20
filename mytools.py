import os
import pyttsx3

pyttsx3.speak("Welcome to My Tools Program")

while True:

    pyttsx3.speak("What would you like to open from the following ?")
    print("What would you like to open from the following ?")

    print()
    # options
    print("Browsers")
    print("Google Chrome Browser")
    print("Firefox Browser")
    print("Internet Explorer Browser\n")

    print("Entertainment")
    print("Windows Media Player")
    print("Windows Video Player")
    print("Vlc Player")
    print("Photos")
    print("Music\n")

    print("Tools")
    print("Notepad")
    print("Calculator")
    print("Special Charachter Map")
    print("Calendar")
    print("Maps")
    print("Camera")
    print("Tips")
    print("Weather")
    print("Clock")
    print("File Explorer\n")

    print("Work Tools")
    print("Projection")
    print("Outlook Mail")
    print("Chat")
    print("Screenshot")
    print("Paint")
    print("Notes")
    print("Cortana\n")

    print("System Tools")
    print("Task Manager")
    print("control Panel")
    print("Microsoft Store")
    print("Settings")
    print("Windows Parental Control")
    print("Windows Security")
    print("Microsoft Support\n")

    print("Close Program\n")
    print("Note: If any of the following program is not Opening / Running Please Check environment variable.")
    print()
    # input

    pyttsx3.speak("Please Type here")
    print("Please Type here: ", end='')
    p = input().lower()
    pyttsx3.speak(p)



    if (("open in p") or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("task manager" in p) or ("tasklist" in p)):
     #  pyttsx3.speak("opening task manager")
        os.system("taskmgr")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("google" in p) or ("chrome" in p)):
     #  pyttsx3.speak(" opening google chrome")
        os.system("chrome")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("firefox" in p) or ("browser" in p)):
        os.system("firefox")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("microsoft edge" in p) or ("microsoft edge browser" in p) or ("edge browser" in p) or ("internet explorer" in p)):
        os.system("start microsoft-edge:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("windows media player" in p) or ("media player" in p)):
        os.system("wmplayer")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("vlc player" in p) or (" video player" in p)):
        os.system("vlc")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("text editor" in p) or ("notepad" in p)):
        os.system("notepad")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("calculator" in p) or ("calc" in p)):
        os.system("calc")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("file explorer" in p) or ("explorer" in p)):
        os.system("explorer")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("control panel" in p) or ("control manager" in p)):
        os.system("control")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("special charachter" in p) or ("charachter map" in p) or ("special charachter map" in p)):
        os.system("charmap")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("calendar" in p)):
        os.system("start outlookcal:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("microsoft" in p) or ("microsoft store" in p) or ("store" in p)):
        os.system("start microsoft:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("Maps" in p) or ("Map" in p)):
        os.system("start bingmaps:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("camera" in p)):
        os.system("start microsoft.windows.camera:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("camera" in p)):
        os.system("start mswindowsmusic:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("mail" in p) or ("outlook mail" in p)):
        os.system("start outlookmail:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("projection" in p) or ("microsoft projection" in p)):
        os.system("start ms-projection:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("cortana" in p) or ("microsoft cortana" in p)):
        os.system("start ms-cortana:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("chat" in p) or ("microsoft chat" in p) or ("chatting" in p)):
        os.system("start ms-chat:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("video player" in p) or ("windows video player" in p) or ("videos" in p) or ("video" in p)):
        os.system("start mswindowsvideo:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("photos" in p) or ("photo" in p)):
        os.system("start ms-photos:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("settings" in p) or ("setting" in p)):
        os.system("start ms-settings:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("windows parental control" in p) or ("parental control" in p)):
        os.system("start ms-wpc:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("defender" in p) or ("windows security" in p) or ("security" in p)):
        os.system("start windowsdefender:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("weather" in p)):
        os.system("start bingweather:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("screenshot" in p) or ("snipping tool" in p)):
        os.system("start ms-screensketch:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("paint" in p) or ("microsoft paint" in p)):
        os.system("start ms-paint:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("onenote" in p) or ("notes" in p) or ("note" in p)):
        os.system("start onenote:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("clock" in p) or ("time" in p)):
        os.system("start ms-clock:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("support" in p) or ("microsoft support" in p) or ("microsoft contact support" in p)):
        os.system("start ms-contact-support:")
    elif (("open" in p) or ("run" in p) or ("launch" in p) or ("execute" in p)) and (("tips" in p) or ("tip" in p)):
        os.system("start ms-get-started:")
    elif ("exit" in p) or ("quit" in p) or ("close" in p) or ("shutdown" in p) or ("shut it down" in p) or ("close program" in p):
        os.system("exit")
        break

    else:
       print("Value not found\n Please try again")




