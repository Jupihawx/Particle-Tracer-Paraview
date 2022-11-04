import pandas as pd
  
from tkinter import *
df = pd.read_csv("points_data.csv")

def write_values(): # Used to write down the value on the csv
    df = pd.read_csv("points_data.csv")

    selected_tracer=int(clicked.get())
    print(selected_tracer)
    df.loc[selected_tracer, 'center_x'] = str(w1.get())
    df.loc[selected_tracer, 'center_y'] = str(w2.get())
    df.loc[selected_tracer, 'center_z'] = str(w3.get())
    df.loc[selected_tracer, 'number_points'] = str(w4.get())
    df.loc[selected_tracer, 'radius_points'] = str(w5.get())
    df.loc[selected_tracer, 'updated']=str(1)
    df.loc[selected_tracer, 'diffCoeff'] = str(w6.get())
    df.loc[selected_tracer, 'Velocity direction'] = str(w7.get()) # !!! This is wrong, should not behave like this. Modify it once you have the data for the POD. You should make sure there is another update loop and update the velocity only if it is changed (add another "Velocity changed" checker, to avoid changing it every time we modift the tracer)
    df.to_csv("points_data.csv", index=False)

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


master = Tk()
master.title("Particle Tracer Manager")

# Select the particle tracer (== the line on the csv)
point_text= Label(text="Point selected") 
point_text.pack()
point_selection= ["0","1","2","3","4","5"]
clicked = StringVar()
clicked.set( "0" )
drop = OptionMenu( master , clicked , *point_selection,command=update_window )
drop.pack()

# Inputs to modify the values
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


Button(master, text='Update', command=write_values,pady=30,padx=30).pack()

mainloop()

