import PySimpleGUI as sg
print("everyCalc event log")
sg.theme("DefaultNoMoreNagging")
loading_window = sg.Popup("everyCalc\n© Erik's Gadgets, 2023")
window = sg.Window(title="Menu", layout=[[sg.Text("everyCalc")],[sg.Button("Basic Calculator")],[sg.Button("Conversion Calculator")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Basic Calculator":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("everyCalc")],[sg.Button("Default")],[sg.Button("Input-Based")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
    if event == "Return [1]":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("everyCalc")],[sg.Button("Basic Calculator")],[sg.Button("Conversion Calculator")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Conversion Calculator":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("everyCalc")],[sg.Button("Decimal to Octal")],[sg.Button("Decimal to Hexadecimal")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
    if event == "Decimal to Octal":
        window.close()
        window = sg.Window(title="Decimal to Octal [Conversion]", layout=[[sg.Text("everyCalc")],[sg.Input()],[sg.Button("Convert!")],[sg.Button("Return [3]")],[sg.Text("© Erik's Gadgets")]])
        calctype = 3
    if event == "Decimal to Hexadecimal":
        window.close()
        window = sg.Window(title="Decimal to Hexadecimal [Conversion]", layout=[[sg.Text("everyCalc")],[sg.Input()],[sg.Button("Convert!")],[sg.Button("Return [3]")],[sg.Text("© Erik's Gadgets")]])
        calctype = 4
    if event == "Convert!":
        if calctype == 3:
            do1 = oct(int(values[0]))
            do2 = []
            for char in do1:
                do2.append(char)
            do3 = ""
            del do2[0]
            del do2[0]
            for i in do2:
                do3 += i
            sg.Popup(str(values[0]) + " = " + do3)
        if calctype == 4:
            do1 = hex(int(values[0]))
            do2 = []
            for char in do1:
                do2.append(char)
            do3 = ""
            del do2[0]
            del do2[0]
            for i in do2:
                do3 += i
            sg.Popup(str(values[0]) + " = " + do3)
    if event == "Input-Based":
        window.close()
        calctype = 1
        window = sg.Window(title="Input-Based Calculator [Basic]", layout=[[sg.Text("EveryCalc")],[sg.Input(), sg.Button("=")],[sg.Button("Return [2]")],[sg.Text("© Erik's Gadgets")]])
    if event == "=":
        if calctype == 1:
            sg.Popup("Your Answer Is: " + str(eval(values[0])) + "\n" + str(values[0]) + " = " + str(eval(values[0])))
        if calctype == 2:
            sg.Popup("Your Answer Is: " + str(eval(equation)) + "\n" + str(equation) + " = " + str(eval(equation)))
    if event == "Return [3]":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("everyCalc")],[sg.Button("Decimal to Octal")],[sg.Button("Decimal to Hexadecimal")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
    if event == "Return [2]":
        window.close()
        window = sg.Window(title="Menu", layout=[[sg.Text("everyCalc")],[sg.Button("Default")],[sg.Button("Input-Based")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]],margins=(100, 50))
    if event == "Default":
        calctype = 2
        window.close()
        equation = ""
        window = sg.Window(title="Input-Based Calculator [Basic]", layout=[[sg.Text("EveryCalc")],[sg.Button("**"),sg.Button("."),sg.Button("0"),sg.Button("/")],[sg.Button("9"),sg.Button("8"),sg.Button("7"),sg.Button("*")],[sg.Button("6"),sg.Button("5"),sg.Button("4"),sg.Button("-")],[sg.Button("3"),sg.Button("2"),sg.Button("1"),sg.Button("+")],[sg.Button("="), sg.Button("Preview"), sg.Button("C")],[sg.Button("Return [2]")],[sg.Text("© Erik's Gadgets")]])
    if event == ".":
        if calctype == 2:
            equation += "."
    if event == "Preview":
        sg.Popup(str(equation))
    if event == "0":
        if calctype == 2:
            equation += "0"
    if event == "1":
        if calctype == 2:
            equation += "1"
    if event == "2":
        if calctype == 2:
            equation += "2"
    if event == "3":
        if calctype == 2:
            equation += "3"
    if event == "+":
        if calctype == 2:
            equation += "+"
    if event == "C":
        if calctype == 2:
            equation = ""
    if event == "4":
        if calctype == 2:
            equation += "4"
    if event == "-":
        if calctype == 2:
            equation += "-"
    if event == "5":
        if calctype == 2:
            equation += "5"
    if event == "6":
        if calctype == 2:
            equation += "6"
    if event == "*":
        if calctype == 2:
            equation += "*"
    if event == "7":
        if calctype == 2:
            equation += "7"
    if event == "8":
        if calctype == 2:
            equation += "8"
    if event == "9":
        if calctype == 2:
            equation += "9"
    if event == "/":
        if calctype == 2:
            equation += "/"
    if event == ".":
        if calctype == 2:
            equation += "."
    if event == "**":
        if calctype == 2:
            equation += "**"
window.close()
