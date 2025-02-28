# Unnamed Programmable Buttons GUI
Simple program using tkinter that allows you to create a grid of buttons that preform your specified task. 
Scales infinitely based on how many buttons you list.

![python_VO0iKDx313](https://github.com/user-attachments/assets/302b7774-8eff-4a83-b728-5e48460271e3)



----
Can input: 
- Executables such as 'notepad.exe'
- Full directories such as 'C:\ users\some music file.ogg'     or   '/usr/txt_document.txt'

Dependencies: 
- Tkinter (pip install tk)
- Tkinter tooltips (pip install tkinter-tooltip)

# Instructions: 
Edit the Main.pyw file 

0) Ensure tkinter dependencies are installed. 
1) In the Main.pyw, edit the "button_list" variable and insert a list that has:
    - the button name, 
    - the directory/file that is opened, 
    - and the description (optional, will show up as tooltip).
   
    >['Button name', 'directory or executable', 'Tooltip description'],  

   Repeat for desired number of buttons

2) Change optional desired parameters underneath the list to customize the button attributes such as colors, button dimensions, size, columns, etc. 


# Examples

Example of the default example layout: 

![python_LqgTqNjdzu](https://github.com/user-attachments/assets/12379886-a10c-4ff6-8230-3c0046d4c472)

Example of a reasonable layout:

![python_u2AbXj8BqU](https://github.com/user-attachments/assets/d6f9c6ec-1d73-4bb6-b832-ca63787caf4a)




Example of a ~~ugly~~ customized layout 

![python_QkpouZ7ZoA](https://github.com/user-attachments/assets/2d362e13-e458-4ded-b24b-412ffded7d2c)
