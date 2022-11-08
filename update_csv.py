import pandas as pd
import pyautogui

pyautogui.PAUSE = 0.0001 # Makes thing faster
import pyperclip

from tkinter import *
df = pd.read_csv("points_data.csv") # data controlling the points
script_setup='exec(open("./algorithms/base_setup.py").read())'

""" script_create_particles = open("./algorithms/create_sourceAndparticles.py", "r").read() # script for creating points and particles
script_delete_particles = open("./algorithms/delete_sourceAndparticles.py", "r").read() # script to delete particles
script_setup = open("./algorithms/base_setup.py", "r").read() # script to initialize
 """

def write_values(): # Used to write down the value on the csv
    df = pd.read_csv("points_data.csv")

    selected_tracer=int(clicked.get())
    print(selected_tracer)
    df.loc[selected_tracer, 'center_x'] = str(w1.get())
    df.loc[selected_tracer, 'center_y'] = str(w2.get())
    df.loc[selected_tracer, 'center_z'] = str(w3.get())
    df.loc[selected_tracer, 'number_points'] = str(w4.get())
    df.loc[selected_tracer, 'radius_points'] = str(w5.get())
    df.loc[selected_tracer, 'diffCoeff'] = str(w6.get())
    df.loc[selected_tracer, 'Velocity direction'] = str(w7.get()) # !!! This is wrong, should not behave like this. Modify it once you have the data for the POD. You should make sure there is another update loop and update the velocity only if it is changed (add another "Velocity changed" checker, to avoid changing it every time we modift the tracer)
   
    df.loc[selected_tracer, 'updated']=str(1)

    df.to_csv("points_data.csv", index=False)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def update_colors():
    df = pd.read_csv("points_data.csv")
    selected_tracer=int(clicked.get())

    df.loc[selected_tracer, 'colorR'] = str(wr.get()) 
    df.loc[selected_tracer, 'colorG'] = str(wg.get()) 
    df.loc[selected_tracer, 'colorB'] = str(wb.get()) 

    drop.configure(foreground="#"+str(rgb_to_hex((wr.get(),wg.get(),wb.get()))))
    df.to_csv("points_data.csv", index=False)
    select_python_shell_paraview("""exec(open("./algorithms/update_color.py").read())""")


def update_window(event): # Used to choose the right line to modify the csv 
    df = pd.read_csv("points_data.csv")

    selected_tracer=int(clicked.get())
    print(df.loc[selected_tracer, 'center_x'])

    w1.set(df.loc[selected_tracer, 'center_x'])
    w2.set(df.loc[selected_tracer, 'center_y'])
    w3.set(df.loc[selected_tracer, 'center_z'])
    w4.set(df.loc[selected_tracer, 'number_points'])
    w5.set(df.loc[selected_tracer, 'radius_points'])
    w6.set(df.loc[selected_tracer, 'diffCoeff'])
    wr.set(df.loc[selected_tracer, 'colorR'])
    wg.set(df.loc[selected_tracer, 'colorG'])
    wb.set(df.loc[selected_tracer, 'colorB'])

    drop.configure(foreground="#"+str(rgb_to_hex((wr.get(),wg.get(),wb.get()))))


def select_python_shell_paraview(script): # Paraview has some weird complicated way of handling different python frameworks, between clients, server, etc. A quick and dirty way to overcome it is to use this method to enter the value we want in the python shell directly

    initial_position=pyautogui.position()
    start = pyautogui.locateCenterOnScreen('python_shell_text.png')
    print(start)
    pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image
    pyautogui.moveRel(0,100)
    pyautogui.click()
    pyautogui.hotkey('right')
    pyautogui.hotkey('right')
    pyautogui.hotkey('right') # To avoid any issue
    pyperclip.copy(script)
    pyautogui.hotkey("ctrl","v")
    pyautogui.press('enter')
    pyautogui.moveTo(initial_position)

master = Tk()
master.title("Particle Tracer Manager")


def delete_particle():
    selected_tracer=int(clicked.get())
    df = pd.read_csv("points_data.csv")
    if not df.loc[selected_tracer, 'exist?']: 
        print("THESE PARTICLES DO NOT EXIST")
    else:
        f=open('./algorithms/delete_sourceAndparticles_button.py',"r")
        f_temp=open('./algorithms/delete_sourceAndparticles_button_temp.py',"w")
        lines = f.read()
        f_temp.write(lines.format(str(selected_tracer)))
        f.close()
        f_temp.close()
        select_python_shell_paraview("""exec(open("./algorithms/delete_sourceAndparticles_button_temp.py").read())""")

        df.loc[selected_tracer, 'exist?']=str(0)
        df.to_csv("points_data.csv", index=False)



def create_particle():
    selected_tracer=int(clicked.get())
    df = pd.read_csv("points_data.csv")
    if df.loc[selected_tracer, 'exist?']: 
        print("THESE PARTICLES ALREADY EXIST")
    else:
        f=open('./algorithms/create_sourceAndparticles_button.py',"r")
        f_temp=open('./algorithms/create_sourceAndparticles_button_temp.py',"w")
        lines = f.read()
        f_temp.write(lines.format(str(selected_tracer),str(selected_tracer+1)))
        f.close()
        f_temp.close()
        select_python_shell_paraview("""exec(open("./algorithms/create_sourceAndparticles_button_temp.py").read())""")

        df.loc[selected_tracer, 'exist?']=str(1)
        df.to_csv("points_data.csv", index=False)

def load_scene():
    scene=str(w7.get())
    f=open('./algorithms/change_scene.py',"r")
    f_temp=open('./algorithms/change_scene_temp.py',"w")
    lines = f.read()
    f_temp.write(lines.format(str(scene)))
    f.close()
    f_temp.close()
    select_python_shell_paraview("""exec(open("./algorithms/change_scene_temp.py").read())""")







Button(master, text='INITIALIZE', command=lambda :select_python_shell_paraview('exec(open("./algorithms/base_setup.py").read())'),pady=3,padx=30).pack()

# Select the particle tracer (== the line on the csv)
point_text= Label(text="Point selected") 
point_text.pack()
point_selection= ["0","1","2","3","4","5"]
clicked = StringVar()
clicked.set( "0" )
drop = OptionMenu( master , clicked , *point_selection,command=update_window )
drop.pack()

creation_deletion_buttons= Frame(master)
creation_deletion_buttons.pack(side=TOP)
Button(creation_deletion_buttons, text='Create selected particle', command=create_particle,pady=10,padx=10).pack(side=LEFT)
Button(creation_deletion_buttons, text='Delete selected particle', command=delete_particle,pady=10,padx=10).pack(side=LEFT)


topFrame= Frame(master)
topFrame.pack(side=TOP)
# Inputs to modify the values
wr = Scale(topFrame, from_=0, to=255,orient=HORIZONTAL,length=100, label='R',width=30)
wr.set(df.loc[0, 'colorR']) #this lines are just to initialize on the first opening 
wr.pack(side=LEFT)

wg = Scale(topFrame, from_=0, to=255,orient=HORIZONTAL,length=100, label='G',width=30)
wg.set(df.loc[0, 'colorG']) #this lines are just to initialize on the first opening 
wg.pack(side=LEFT)

wb = Scale(topFrame, from_=0, to=255,orient=HORIZONTAL,length=100, label='B',width=30)
wb.set(df.loc[0, 'colorB']) #this lines are just to initialize on the first opening 
wb.pack(side=LEFT)

drop.configure(foreground="#"+str(rgb_to_hex((wr.get(),wg.get(),wb.get())))) #Initialize the drop color

Button(master, text='Update', command=update_colors,pady=5,padx=5).pack()


w1 = Scale(master, from_=-300, to=300,orient=HORIZONTAL,length=300, label='X',width=30)
w1.set(df.loc[0, 'center_x']) #this lines are just to initialize on the first opening 
w1.pack()
w2 = Scale(master, from_=-300, to=300,orient=HORIZONTAL,length=300, label='Y',width=30)
w2.set(df.loc[0, 'center_y'])
w2.pack()
w3 = Scale(master, from_=0, to=500,orient=HORIZONTAL,length=300, label='Z',width=30)
w3.set(df.loc[0, 'center_z'])
w3.pack()
w4 = Scale(master, from_=0, to=300,orient=HORIZONTAL,length=300, label='Number of points',width=30)
w4.set(df.loc[0, 'number_points'])
w4.pack()
w5 = Scale(master, from_=0, to=30,orient=HORIZONTAL,length=300, label='Radius',width=30)
w5.set(df.loc[0, 'radius_points'])
w5.pack()
w6 = Scale(master, from_=0, to=50,orient=HORIZONTAL,length=300, label='Diffusion coefficient',width=30)
w6.set(df.loc[0, 'diffCoeff'])
w6.pack()
w7 = Scale(master, from_=-180, to=180,orient=HORIZONTAL,length=300, label='Velocity direction (°)',width=30)
#w7.set(0)
w7.pack()





Button(master, text='Change velocity', command=load_scene,pady=30,padx=30).pack()

Button(master, text='Update', command=write_values,pady=30,padx=30).pack()

master.attributes('-topmost', True) #To always have window on top

mainloop()

