""" 
Unnamed Programmable Buttons GUI
Version 0.5, July 2024
Programmed by Sondered03

Dependencies: 
Tkinter (pip install tk)
Tkinter tooltips (pip install tkinter-tooltip)

Possible improvements: 
- Tooltips (Current implimentation is buggy and sometimes doesn't work)
- Individual button colors. 
- Console Bar at the top. 
- Redisign utilizing QT


----
Instructions: Change button_list with desired values. 
0) Ensure tkinter dependencies are installed. 
1) Go to "button_list" and list:
    - the button name, 
    - the directory/file that is opened, 
    - and the description (optional, will show up as tooltip). 
    Separate each with a embeded list '[]' and a comma ','
        ['Button name', 'directory or executable', 'Tooltip description'],
2) Change optional desired parameters underneath

Can input: 
- Executables: 'notepad.exe'
- Full directories: 'C:\ users\some music file.ogg'     or   '/usr'

Does not support scripts. You can get around this by making a bat/bash or python scripts as a file then pasting the file directory as a button.
"""


# Buttons
button_list = [
    #[Name , Directory, Description],
    ['Notepad', 'notepad.exe', 'Opens Notepad'],
    ['Cmd', 'cmd.exe', 'Opens The Command Prompt'],
    ['Open directory', 'C:']
    ['Do thing', '',],
    ['Open File', '',],
]

# Number of buttons in a row.
columns = 3

# Padding in between buttons
padding = 2
border_thickness = 1

# Button appearance (Accepts Hex )
button_color = 'grey'
text_color = 'white'
background_color = '#333333'

# Font Settings
font_name = ''
font_size = 12

# Manual button dimensions. (Setting to 0 scales buttons based on font and name size)
box_x = 12
box_y = 0


# Additional Settings
program_name = 'GUI Program'        # Default title
program_size = ''   # Default program dimensions (Example: '500x500')
tooltip_delay = 0.2     # Time for tooltip to appear





########################
# Do not edit past this point
########################

import os
import tkinter as tk
from tktooltip import ToolTip


def buttonP(filepath):
    # On click button, opens the file. 
    print("Opening: ", filepath)
    tkroot.title(("Opened: " + filepath))
    os.startfile(filepath)
    return


tkroot = tk.Tk()
tkroot.title(program_name)
tkroot.geometry(program_size)
tkroot.configure(bg=background_color)
coln = rown = errors = 0

# Generates boxes based on how many values are in button_list.
for i in range(len(button_list)):

    # Shifts row when column hits the column limit
    if coln == columns:
        coln = 0
        rown += 1

    # Frame creation
    frame = tk.Frame(master=tkroot, relief=tk.RAISED,borderwidth=border_thickness)
    frame.grid(row=rown, column=coln)
    

    # Creation of button.
    # Iterates through each button_list entry and applies the specifiied button traits along with the function to open the file as a result. 
    try: 
        button = tk.Button(master=frame, bg=button_color, fg=text_color, width=box_x, height=box_y, font=(font_name,font_size), text=f"{button_list[i][0]}", command=lambda v=button_list[i][1]: buttonP(v) ) 

        try: 
            # Hover Tooltip 
            button_list[i][2]
            ToolTip(button, msg=(button_list[i][2]), delay=tooltip_delay)
        except:
            # Default tooltip if no input is entered
            ToolTip(button, msg=("Opens "+ button_list[i][1]), delay=tooltip_delay)


        # Changes position of grid for next button
        button.grid(padx=padding,pady=padding)
        coln += 1

    except:
        # If an error is found with reading a button it is disregarded.
        errors += 1 
        print("Error reading button number:", i+1,)
        pass
    
if errors > 1:
    print("You have", errors, "button errors. Please ensure that you have a valid button name and directory.")

tkroot.mainloop()

