from pose import Pose, Library
import PySimpleGUI as sg

def open_library():
    layout_col1 = [
        [sg.Text("This is where the library will go")]
    ]

    layout_col2 = [
        [sg.Text("This is where the images and description will appear")]
    ]

    layout_library = [
        [sg.Text('Asana Library', key='open')],
        [sg.Column(layout_col1), sg.VSeparator(), sg.Column(layout_col2)],
        [sg.Button('Quit')]
    ]

    window_lib = sg.Window('Asana Library', layout_library, size=(800, 600), modal=True)
    while True:
            event = window_lib.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
    window_lib.close()

def open_routine_build():
    layout_build = [ 
        [sg.Text('This is where the routine builder will go')],
        [sg.Button('Quit')]
    ]
    window_build = sg.Window('Routine Builder', layout_build, size=(800, 600))
    while True:
            event = window_build.read()
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break
    window_build.close()

def open_begin():
    layout_begin = [
        [sg.Text("Welcome to Asana Buddy!", justification='center')],
        [sg.Button('Asana Library'), sg.Button('Routine Builder')],
        [sg.Button('Quit')]
    ]

    window = sg.Window('Asana Buddy', layout_begin, size=(400,300))        
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        if event == 'Asana Library':
            open_library()
        if event == 'Routine Builder':
            open_routine_build()
    window.close()

def main():
    standing = Library("standing")
    seated = Library("seated")
    supine = Library("supine")
    prone = Library("prone")
    arm_leg = Library("arm & leg")
    balance_inversion = Library("arm balance & inversion")
    mountain = Pose("mountain", "tadasana", "standing", "neutral")

    open_begin()

main()