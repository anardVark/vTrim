from cx_Freeze import setup, Executable

base = None  

executables = [Executable("main.py", base=base)]

#Future me test if this works without idna imported
packages = ["idna", "PySimpleGUI", "os", "datetime", "moviepy", "time"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "vTrim",
    options = options,
    version = "0.0.6",
    description = 'Trim the intros and outros of individual or whole directories of videos.',
    executables = executables
)