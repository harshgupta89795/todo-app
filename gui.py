import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a Todo")
input_box=sg.InputText(tooltip="Enter todo")
add_button=sg.Button("Add")

window=sg.Window("My To-Do App",[[label],[input_box,add_button]])
window.read()
window.close()
