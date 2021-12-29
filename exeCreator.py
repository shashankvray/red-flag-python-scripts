# python exeCreator.py build
from cx_Freeze import setup, Executable

base = None    
filename = input("Enter the filename(relative) or path(elsewhere) to create its .exe: (without the file extension) -   ")
packages = list(map(str, input(f"Enter the packages used/imported in your {filename}.py file in a single line separated with space(\" \"):\n").split()))
executables = [Executable(filename + ".py", base=base)]

options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<Shashank V Ray>",
    options = options,
    version = "1.0",
    description = "Python File",
    executables = executables
)
