import win32gui
import pyautogui
from pynput.mouse import Listener
import PySimpleGUI as sg

keysList = [1, 2, 3, 4, 5, 6, 7, 8]
textFile = "C:\\Users\\Alex\\Desktop\\Projets\\multiple-account-manager\\personnages.txt"
startRecording = True

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

def on_click(x, y, button, pressed):
    if(startRecording) :
        print(x, y, button, pressed)
    else :
        return False

# Charger les personnages déjà enregistrés
file = open(textFile, "r")
file_contents = file.read()
personnages = file_contents.splitlines()

window = sg.Window("Hello World", layout, finalize=True)

for i in range(len(personnages)):
    window.Element(keysList[i]).Update(personnages[i])

while True:
    event, values = window.read()
    listener = Listener(on_click=on_click)
    
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