import PySimpleGUI as sg
import os.path
import pytrimmer as pyt
import essential_py as esp
import datetime as datetime
from time import sleep

sg.theme("DarkGrey15")

header = [
    [
        sg.Text("Source Directory: "),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-", expand_x=True),
        sg.FolderBrowse(),
    ]
]
main_body = [
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-", expand_x=True, expand_y=True)
    ]
]
footer = [
    [
        sg.ProgressBar(max_value=25, expand_x=True, border_width=2, bar_color=('red', 'white'), key='-STATUS-')
    ],
    [
        sg.Button('Trim Select File', key='-STRIP FILE-'),
        sg.Button('Trim Entire Directory', key='-STRIP DIR-')
    ],
    [
        sg.Image(os.path.join('\\\\truenas\\Storasaurus\\Personal Files\\Nerd Shit\\Coding Projects\\PlayOnVideoCleaner\\vT_256.png'), subsample=4)
    ]
]
layout = [
    [
        sg.Column(header, expand_x=True, element_justification='center')
    ],
    [   
        sg.Column(main_body, expand_x=True, expand_y=True)
    ],
    [
        sg.Column(footer, expand_x=True, element_justification='center')
    ]
]

icon_path = os.path.join(os.getcwd(), "vT_256.png")

window = sg.Window("vTrim", layout, grab_anywhere_using_control=True, icon=icon_path, titlebar_background_color='black', titlebar_text_color='white', use_custom_titlebar=True)
progress_bar = window['-STATUS-']

# Create an event loop
def main():
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-FOLDER-":
            try:
                # Get list of files in folder
                file_list = os.listdir(values["-FOLDER-"])
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(values["-FOLDER-"], f))
                and f.lower().endswith((".mp4"))
            ]
            window["-FILE LIST-"].update(fnames)

        elif event == "-STRIP FILE-":
            try:
                filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
                
                esp.wrout(f'Trimming File: {filename}')
                pyt.strip(values['-FOLDER-'], os.path.join(values['-FOLDER-'], 'TRIMMED'), values["-FILE LIST-"][0], 12, -5)

                progress_bar.update_bar(1,1)

            except Exception as e:
                esp.wrout(f'[{datetime.datetime.today().strftime("%Y-%m-%d")}][There was an error trimming the file ({filename})] | [{e}]')
                pass
        elif event == "-STRIP DIR-":
            try:
                n = 1
                esp.wrout(f'Trimming Directory: {values["-FOLDER-"]}')
                video_list = pyt.list_dir(values['-FOLDER-'])

                for video in video_list:
                    pyt.strip(values['-FOLDER-'], os.path.join(values['-FOLDER-'], 'TRIMMED'), video, 12, -5)
                    progress_bar.update_bar(n, len(video_list))
                    n += 1

            except Exception as e:
                esp.wrout(f'[{datetime.datetime.today().strftime("%Y-%m-%d")}][There was an error trimming the directory ({values["-FOLDER-"]})] | [{e}]')
                pass

    window.close()

if (__name__ == '__main__'):
    try:
        main()
    except Exception as e:
        esp.wrout(f"General Failure {e}")