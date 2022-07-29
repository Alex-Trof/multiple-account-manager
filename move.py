import win32gui, win32com.client
import pyautogui
import pythoncom
import time
from pynput.mouse import Listener, Controller, Button
from pynput.keyboard import Key, Listener
import PySimpleGUI as sg
import pywinauto


keysList = [1, 2, 3, 4, 5, 6, 7, 8]
textFile = "C:\\Users\\Alex\\Desktop\\Projets\\multiple-account-manager\\personnages.txt"
startRecording = True
click = []
windowsList = {}

layout = [
    [sg.Text('Perso principal', size =(15, 1)), sg.InputText(key=keysList[0])],
    [sg.Text('Deuxième perso', size =(15, 1)), sg.InputText(key=keysList[1])],
    [sg.Text('Troisième perso', size =(15, 1)), sg.InputText(key=keysList[2])],
    [sg.Text('Quatrième perso', size =(15, 1)), sg.InputText(key=keysList[3])],
    [sg.Text('Cinquième perso', size =(15, 1)), sg.InputText(key=keysList[4])],
    [sg.Text('Siwxième perso', size =(15, 1)), sg.InputText(key=keysList[5])],
    [sg.Text('Septième perso', size =(15, 1)), sg.InputText(key=keysList[6])],
    [sg.Text('Huitième perso', size =(15, 1)), sg.InputText(key=keysList[7])],
    [sg.Button('Enregistrer'), sg.Button('Cancel')],
    [sg.Text('Mode déplacement', size =(15, 1))],
    [sg.Button('On'), sg.Button('Off')]
]

# Charger les personnages déjà enregistrés
file = open(textFile, "r")
file_contents = file.read()
personnages = file_contents.splitlines()

# Récupère la list des fenêtres ouvertes
# PB ici !
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        windowsName = win32gui.GetWindowText( hwnd )
        windowsList[windowsName] = hwnd

win32gui.EnumWindows( winEnumHandler, None )

def setWindow(persoName):
    for key, value in windowsList.items():
        if(persoName in key):
            print(persoName, value)
            shell=win32com.client.Dispatch("WScript.Shell",pythoncom.CoInitialize())
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(value)

def clique(x, y):
    if(startRecording) :
        print(x, y)
        for i in range(len(personnages)):
            if(len(personnages[i]) != 0):
                setWindow(personnages[i])
                time.sleep(1)
                #pywinauto.mouse.click(button='left', coords=(x, y)) 
        setWindow(personnages[0])  
    else :
        return False

def on_press(key):
    print('{0} release'.format(
        key))
    if key == Key.ctrl_l:
        x,y = pyautogui.position()
        clique(x, y)

window = sg.Window("Hello World", layout, finalize=True)

for i in range(len(personnages)):
    window.Element(keysList[i]).Update(personnages[i])

while True:
    event, values = window.read()
    listener = Listener(on_press=on_press)

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Enregistrer':
        file = open(textFile, "w+")
        file.truncate(0)
        for key, value in values.items():
            file.write(value + "\n")   
        file.close()

    if event == 'On':
        startRecording = True
        listener.start()

    if event == 'Off':
        startRecording = False
        listener.stop() 