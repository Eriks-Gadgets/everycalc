import PySimpleGUI as sg
sg.theme("DefaultNoMoreNagging")
loading_window = sg.Popup("EveryCalc\n© Erik's Gadgets, 2023")
window = sg.Window(title="Menu", layout=[[sg.Text("EveryCalc")],[sg.Button("Basic Calculator")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Basic Calculator":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("EveryCalc")],[sg.Button("Input-Based")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
    if event == "Return [1]":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("EveryCalc")],[sg.Button("Basic Calculator")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Input-Based":
        window.close()
        calctype = 1
        window = sg.Window(title="Input-Based Calculator [Basic]", layout=[[sg.Text("EveryCalc")],[sg.Input(), sg.Button("=")],[sg.Button("Return [1.1]")],[sg.Text("© Erik's Gadgets")]])
    if event == "=":
        if calctype == 1:
            sg.Popup("Your Answer Is: " + str(eval(values[0])) + "\n" + str(values[0]) + " = " + str(eval(values[0])))
    if event == "Return [1.1]":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("EveryCalc")],[sg.Button("Input-Based")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
window.close()
