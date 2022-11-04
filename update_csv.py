import pandas as pd
  
from tkinter import *
df = pd.read_csv("points_data.csv")

def write_values():
    df.loc[0, 'center_x'] = str(w1.get())
    df.loc[0, 'center_y'] = str(w2.get())
    df.loc[0, 'center_z'] = str(w3.get())
    df.loc[0, 'number_points'] = str(w4.get())
    df.loc[0, 'radius_points'] = str(w5.get())
    df.loc[0, 'updated']=str(1)
    df.loc[0, 'diffCoeff'] = str(w6.get())
    print(df)
    df.to_csv("points_data.csv", index=False)

master = Tk()
w1 = Scale(master, from_=-300, to=300,orient=HORIZONTAL,length=300, label='X',width=30)
w1.set(-150)
w1.pack()
w2 = Scale(master, from_=-300, to=300,orient=HORIZONTAL,length=300, label='Y',width=30)
w2.set(0)
w2.pack()
w3 = Scale(master, from_=0, to=500,orient=HORIZONTAL,length=300, label='Z',width=30)
w3.set(50)
w3.pack()
w4 = Scale(master, from_=0, to=300,orient=HORIZONTAL,length=300, label='Number of points',width=30)
w4.set(50)
w4.pack()
w5 = Scale(master, from_=0, to=30,orient=HORIZONTAL,length=300, label='Radius',width=30)
w5.set(5)
w5.pack()
w6 = Scale(master, from_=0, to=50,orient=HORIZONTAL,length=300, label='Diffusion coefficient',width=30)
w6.set(1)
w6.pack()
Button(master, text='Update', command=write_values,pady=30,padx=30).pack()

mainloop()

