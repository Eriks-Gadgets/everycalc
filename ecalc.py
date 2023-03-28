import PySimpleGUI as sg
sg.theme("DefaultNoMoreNagging")
loading_window = sg.Popup("EveryCalc\n© Erik's Gadgets, 2023")
window = sg.Window(title="Menu", layout=[[sg.Text("EveryCalc")],[sg.Button("Basic Calculator")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    if event == "Basic Calculator":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("EveryCalc")],[sg.Button("Input-Based")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
window.close()
