import win32gui
import pyautogui
from pynput.mouse import Listener
import PySimpleGUI as sg

personnages = {}

layout = [
    [sg.Text('Perso principal', size =(15, 1)), sg.InputText()],
    [sg.Text('Deuxième perso', size =(15, 1)), sg.InputText()],
    [sg.Text('Troisième perso', size =(15, 1)), sg.InputText()],
    [sg.Text('Quatrième perso', size =(15, 1)), sg.InputText()],
    [sg.Text('Cinquième perso', size =(15, 1)), sg.InputText()],
    [sg.Text('Siwxième perso', size =(15, 1)), sg.InputText()],
    [sg.Text('Septième perso', size =(15, 1)), sg.InputText()],
    [sg.Text('Huitième perso', size =(15, 1)), sg.InputText()],
    [sg.Button('Valider'), sg.Button('Cancel')]
]

window = sg.Window("Hello World", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Valider':
        for key, value in values.items():
            print(value)